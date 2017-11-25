import logging
from PyQt4 import QtGui
from PyQt4.QtCore import QThread, SIGNAL
import sys
import PyScada
import numpy as np
import random as rd
import matplotlib
matplotlib.use("Qt4Agg")
from matplotlib.figure import Figure
from matplotlib.animation import TimedAnimation
from matplotlib.lines import Line2D
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import time
import threading
import OpenOPC
class loggerFactory:
    @staticmethod
    def getLogger(widget):
        logger = logging.getLogger(__name__)
        handler = QtHandler(widget)
        handler.setFormatter(
            logging.Formatter("%(levelname)s: %(asctime)s : %(message)s"))
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger

class QtHandler(logging.Handler):

    def __init__(self, widget):
        super(QtHandler,self).__init__()
        self.widget = widget

    def emit(self, record):
        record = self.format(record)
        item = QtGui.QListWidgetItem(record)
        if "WARNING" in item.text():
            item.setTextColor(QtGui.QColor("red"))
        elif "INFO" in item.text():
            item.setTextColor(QtGui.QColor("green"))
        elif "DEBUG" in item.text():
            item.setTextColor(QtGui.QColor("blue"))
        self.widget.addItem(item)

class simpleThread(QThread):
    def __init__(self, opc, logger):
        QThread.__init__(self)
        self.opc= opc
        self.logger = logger
        self.running = True
    def __del__(self):
        print "in thread closing opc"
        #self.opc.close()
        self.wait()

    def run(self):
        self.running = True
        data=1
        kierunek = True
        while self.running:
            if data == 100 or data == 0:
                kierunek = not kierunek
            if kierunek :
                data=data +1
            else:
                data = data-1
           # response = self.opc.read('Bucket Brigade.Real8')
          #  self.logger.debug("Message from OPC Server: value={0}, quality={1}, time={2}".format(*response))
            self.emit(SIGNAL("update(int)"), data)
            self.msleep(100)

class CustomFigCanvas(FigureCanvas, TimedAnimation):

    def __init__(self):

        self.addedData = []
        print(matplotlib.__version__)
        # The data
        self.xlim = 200
        self.n = np.linspace(0, self.xlim - 1, self.xlim)
        self.y = (self.n * 0.0) + 50
        # The window
        self.fig = Figure(figsize=(5,5), dpi=100)
        self.ax1 = self.fig.add_subplot(111)
        # self.ax1 settings
        self.ax1.set_xlabel('time')
        self.ax1.set_ylabel('raw data')
        self.line1 = Line2D([], [], color='blue')
        self.line1_tail = Line2D([], [], color='red', linewidth=2)
        self.line1_head = Line2D([], [], color='red', marker='o', markeredgecolor='r')
        self.ax1.add_line(self.line1)
        self.ax1.add_line(self.line1_tail)
        self.ax1.add_line(self.line1_head)
        self.ax1.set_xlim(0, self.xlim - 1)
        self.ax1.set_ylim(0, 100)

        FigureCanvas.__init__(self, self.fig)
        TimedAnimation.__init__(self, self.fig, interval = 50, blit = True)

    def new_frame_seq(self):
        return iter(range(self.n.size))

    def addData(self, value):
        self.addedData.append(value)

    def _step(self, *args):
        # Extends the _step() method for the TimedAnimation class.
        TimedAnimation._step(self, *args)
        self.draw()
    def zoomIn(self, value):
        bottom = self.ax1.get_ylim()[0]
        top = self.ax1.get_ylim()[1]
        bottom += value
        top -= value
        self.ax1.set_ylim(bottom,top)
        self.draw()

    def _draw_frame(self, framedata):
        margin = 2
        while(len(self.addedData) > 0):
            self.y = np.roll(self.y, -1)
            self.y[-1] = self.addedData[0]
            del(self.addedData[0])


        self.line1.set_data(self.n[ 0 : self.n.size - margin ], self.y[ 0 : self.n.size - margin ])
        self.line1_tail.set_data(np.append(self.n[-10:-1 - margin], self.n[-1 - margin]), np.append(self.y[-10:-1 - margin], self.y[-1 - margin]))
        self.line1_head.set_data(self.n[-1 - margin], self.y[-1 - margin])
        self._drawn_artists = [self.line1, self.line1_tail, self.line1_head]

        self.draw()


''' End Class '''

class Scada(QtGui.QMainWindow, PyScada.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.connect(self.button_alarms,SIGNAL('clicked()'),self.setAlarms)
        self.progressBar.setMaximum(100)
        init_max=90
        init_min=10
        self.sliderMin.setValue(init_min)
        self.sliderMax.setValue(init_max)
        self.connect(self.sliderMax, SIGNAL('valueChanged(int)'), self.accustomMaxBorder)
        self.connect(self.sliderMin, SIGNAL('valueChanged(int)'), self.accustomMinBorder)
        self.nivel_min_2.setStyleSheet("background-color: green;")
        self.nivel_max_2.setStyleSheet("background-color: green;")
        self.accustomMinBorder(init_min)
        self.accustomMaxBorder(init_max)
        self.logger = loggerFactory.getLogger(self.listWidget)
        self.figure = CustomFigCanvas()
        self.gridLayout_2.addWidget(self.figure)
        self.zoomIn = QtGui.QPushButton(text='zoom')
        self.gridLayout_2.addWidget(self.zoomIn,*(0,1))
        self.zoomIn.clicked.connect(self.zoomBtnAction)
        self.disconnectServer.setDisabled(True)
        self.opc = OpenOPC.open_client('localhost')
        self.opc.connect('Matrikon.OPC.Simulation')
        self.myThread = simpleThread(self.opc, self.logger)
        self.connect(self.connectServer, SIGNAL('clicked()'),self.connectToServer)
        self.connect(self.disconnectServer, SIGNAL('clicked()'), self.disconnectOPC)
        self.connect(self.myThread, SIGNAL('update(int)'), self.update)
        self.connect(self.comboBox, SIGNAL('currentIndexChanged(QString)'), self.setLogLevel)
        self.connect(self.clearLogs, SIGNAL('clicked()'), self.clearScrollText)

    def __del__(self):
        print "Disconnecting Server"
        self.opc.close()

    def connectToServer(self):
        self.myThread.start()
        response = ""
        for info in self.opc.info():
            response += "{0}:    {1}\n".format(*info)
        QtGui.QMessageBox.information(self, "OPC SERVER",
                                    response,
                                    QtGui.QMessageBox.Ok)
        self.connectServer.setDisabled(True)
        self.disconnectServer.setDisabled(False)
        self.logger.info("Connected with OPC Server")


    def disconnectOPC(self):
        self.connectServer.setDisabled(False)
        self.disconnectServer.setDisabled(True)
        self.myThread.running = False
        while self.myThread.isRunning():
            print "thread running, waiting for terminate"
            self.logger.debug("thread running, waiting for terminate")
        self.myThread.terminate()
        self.logger.info("Disconnected with OPC Server")
        print "thread terminated"
        QtGui.QMessageBox.information(self, "OPC SERVER",
                                    "Successfully disconnected!",
                                    QtGui.QMessageBox.Ok)
    def setLogLevel(self, level):
        print "level: " + level
        level_dict = {"DEBUG" : logging.DEBUG, "INFO" : logging.INFO, "WARNING" : logging.WARNING, "ERROR" : logging.ERROR}
        self.logger.setLevel(level_dict[str(level)])

    def clearScrollText(self):
        self.listWidget.clear()

    def setAlarms(self):
        #self.myThread = simpleThread(self.opc)
        #self.connect(self.myThread,SIGNAL('update(int)'),self.update)
        #self.myThread.start()
        pass

    def zoomBtnAction(self):
        print("zoom in")
        self.figure.zoomIn(5)

    def update(self,liczba):
        self.figure.addData(liczba)
        if liczba < self.sliderMax.value():
            self.nivel_max_2.setStyleSheet("background-color: green;")
            self.nivel_max_3.setStyleSheet("background-color: green;")
        else:
            self.nivel_max_2.setStyleSheet("background-color: red;")
            self.nivel_max_3.setStyleSheet("background-color: red;")
            self.logger.warning("ALARM : Vehicle is over the max value")

        if liczba > self.sliderMin.value():
            self.nivel_min_2.setStyleSheet("background-color: green;")
            self.nivel_min_3.setStyleSheet("background-color: green;")
        else:
            self.nivel_min_2.setStyleSheet("background-color: red;")
            self.nivel_min_3.setStyleSheet("background-color: red;")
            self.logger.warning("ALARM : Vehicle is under the min value")
        self.progressBar.setValue(int(liczba))
        self.listWidget.scrollToBottom()



    def accustomMinBorder(self, value):
        postionStart=self.progressBar.geometry().getRect()[0]
        pbWidth = self.progressBar.geometry().getRect()[2]
        geo_min= self.nivel_min_3.geometry()
        pbWidthCorrected = pbWidth - geo_min.width()
        geo_min.moveTo(int(postionStart + float(value)/float(99)*pbWidthCorrected),geo_min.y())
        self.nivel_min_3.setGeometry(geo_min)

    def accustomMaxBorder(self, value):
        postionStart=self.progressBar.geometry().getRect()[0]
        pbWidth = self.progressBar.geometry().getRect()[2]
        geo_max= self.nivel_max_3.geometry()
        pbWidthCorrected = pbWidth - geo_max.width()
        geo_max.moveTo(int(postionStart + float(value)/float(99)*pbWidthCorrected),geo_max.y())
        self.nivel_max_3.setGeometry(geo_max)


def main():
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('cleanlooks'))
    form = Scada()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()