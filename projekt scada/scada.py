import logging
from PyQt4 import QtGui
from PyQt4.QtCore import QThread, SIGNAL
import sys
import PyScada
class loggerFactory:
    @staticmethod
    def getLogger(widget):
        logger = logging.getLogger(__name__)
        handler = QtHandler(widget)
        handler.setFormatter(
            logging.Formatter("%(name)s:%(funcName)s:%(threadName)s:%(lineno)d:%(asctime)s %(levelname)s: %(message)s"))
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
        return logger

class QtHandler(logging.Handler):

    def __init__(self, widget):
        super(QtHandler,self).__init__()
        self.widget = widget

    def emit(self, record):
        record = self.format(record)
        self.widget.addItem(record)

class simpleThread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        data=1
        kierunek = True
        while True:
            if data == 100 or data == 0:
                kierunek = not kierunek
            if kierunek :
                data=data +1
            else:
                data = data-1
            self.emit(SIGNAL("update(int)"), data)
            self.sleep(1)

class Scada(QtGui.QMainWindow, PyScada.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.connect(self.button_alarms,SIGNAL('clicked()'),self.start)
        self.progressBar.setMaximum(100)
        init_max=90
        init_min=10
        self.sliderMin.setValue(init_min)
        self.sliderMax.setValue(init_max)
        a = self.progressBar.geometry()
        self.connect(self.sliderMax, SIGNAL('valueChanged(int)'), self.accustomMaxBorder)
        self.connect(self.sliderMin, SIGNAL('valueChanged(int)'), self.accustomMinBorder)
        self.nivel_min_2.setStyleSheet("background-color: green;")
        self.nivel_max_2.setStyleSheet("background-color: green;")
        self.accustomMinBorder(init_min)
        self.accustomMaxBorder(init_max)
        self.logger = loggerFactory.getLogger(self.listWidget)

    def start(self):
        self.myThread = simpleThread()
        self.connect(self.myThread,SIGNAL('update(int)'),self.update)
        self.myThread.start()

    def update(self,liczba):
        self.progressBar.setValue(int(0))
        if liczba < self.sliderMax.value():
            self.nivel_max_2.setStyleSheet("background-color: green;")
            self.nivel_max_3.setStyleSheet("background-color: green;")

            self.logger.info("Testujemy")
        else:
            self.nivel_max_2.setStyleSheet("background-color: red;")
            self.nivel_max_3.setStyleSheet("background-color: red;")

        if liczba > self.sliderMin.value():
            self.nivel_min_2.setStyleSheet("background-color: green;")
            self.nivel_min_3.setStyleSheet("background-color: green;")
        else:
            self.nivel_min_2.setStyleSheet("background-color: red;")
            self.nivel_min_3.setStyleSheet("background-color: red;")
        self.progressBar.setValue(int(liczba))


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
    form = Scada()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()