from PyQt4 import QtGui
from PyQt4.QtCore import QThread, SIGNAL
import sys
import PyScada

class simpleThread(QThread):
    def __init__(self):
        """
        Make a new thread instance with the specified
        subreddits as the first argument. The subreddits argument
        will be stored in an instance variable called subreddits
        which then can be accessed by all other class instance functions

        :param subreddits: A list of subreddit names
        :type subreddits: list
        """
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
    """
    How the basic structure of PyQt GUI code looks and behaves like is
    explained in this tutorial
    http://nikolak.com/pyqt-qt-designer-getting-started/
    """

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.connect(self.button_alarms,SIGNAL('clicked()'),self.start)
        self.progressBar.setMaximum(100)

    def start(self):
        self.myThread = simpleThread()
        self.connect(self.myThread,SIGNAL('update(int)'),self.update)
        self.myThread.start()

    def update(self,liczba):
        self.progressBar.setValue(int(liczba))
def main():
    app = QtGui.QApplication(sys.argv)
    form = Scada()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()