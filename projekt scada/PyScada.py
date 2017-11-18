# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scadaUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(120, 460, 561, 81))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar {\n"
"border: 1px solid black;\n"
"text-align: top;\n"
"padding: 2px;\n"
"border-bottom-right-radius: 30px;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-right-radius: 30px;\n"
"border-top-left-radius: 30px;\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #fff,\n"
"stop: 0.4999 #eee,\n"
"stop: 0.5 #ddd,\n"
"stop: 1 #eee );\n"
"width: 15px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"stop: 0 #78d,\n"
"stop: 0.4999 #46a,\n"
"stop: 0.5 #45a,\n"
"stop: 1 #238 );\n"
"border-bottom-right-radius: 30px;\n"
"border-bottom-left-radius: 30px;\n"
"border-top-right-radius: 30px;\n"
"border-top-left-radius: 30px;\n"
"border: 1px solid black;\n"
"}"))
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 30)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.BottomToTop)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.nivel_min = QtGui.QFrame(self.centralwidget)
        self.nivel_min.setGeometry(QtCore.QRect(170, 460, 16, 81))
        self.nivel_min.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"padding: 2px;\n"
"background-color: #FFFAFA;"))
        self.nivel_min.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nivel_min.setFrameShadow(QtGui.QFrame.Raised)
        self.nivel_min.setObjectName(_fromUtf8("nivel_min"))
        self.nivel_max = QtGui.QFrame(self.centralwidget)
        self.nivel_max.setGeometry(QtCore.QRect(610, 460, 16, 81))
        self.nivel_max.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"padding: 2px;\n"
"background-color: #FFFAFA;\n"
"\n"
""))
        self.nivel_max.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nivel_max.setFrameShadow(QtGui.QFrame.Raised)
        self.nivel_max.setObjectName(_fromUtf8("nivel_max"))
        self.nivel_min_2 = QtGui.QFrame(self.centralwidget)
        self.nivel_min_2.setGeometry(QtCore.QRect(170, 430, 16, 16))
        self.nivel_min_2.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"padding: 2px;\n"
"background-color: #FFFAFA;"))
        self.nivel_min_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nivel_min_2.setFrameShadow(QtGui.QFrame.Raised)
        self.nivel_min_2.setObjectName(_fromUtf8("nivel_min_2"))
        self.nivel_max_2 = QtGui.QFrame(self.centralwidget)
        self.nivel_max_2.setGeometry(QtCore.QRect(610, 430, 16, 16))
        self.nivel_max_2.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"padding: 2px;\n"
"background-color: #FFFAFA;\n"
"\n"
""))
        self.nivel_max_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nivel_max_2.setFrameShadow(QtGui.QFrame.Raised)
        self.nivel_max_2.setObjectName(_fromUtf8("nivel_max_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(500, 60, 201, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 30, 187, 121))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(-1, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.button_alarms = QtGui.QPushButton(self.gridLayoutWidget)
        self.button_alarms.setCheckable(True)
        self.button_alarms.setObjectName(_fromUtf8("button_alarms"))
        self.gridLayout.addWidget(self.button_alarms, 3, 2, 1, 1)
        self.lcdMax = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdMax.setProperty("intValue", 90)
        self.lcdMax.setObjectName(_fromUtf8("lcdMax"))
        self.gridLayout.addWidget(self.lcdMax, 1, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)
        self.lcdMin = QtGui.QLCDNumber(self.gridLayoutWidget)
        self.lcdMin.setProperty("intValue", 15)
        self.lcdMin.setObjectName(_fromUtf8("lcdMin"))
        self.gridLayout.addWidget(self.lcdMin, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.sliderMin = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderMin.setProperty("value", 15)
        self.sliderMin.setOrientation(QtCore.Qt.Horizontal)
        self.sliderMin.setObjectName(_fromUtf8("sliderMin"))
        self.gridLayout.addWidget(self.sliderMin, 2, 2, 1, 1)
        self.sliderMax = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderMax.setProperty("value", 90)
        self.sliderMax.setOrientation(QtCore.Qt.Horizontal)
        self.sliderMax.setObjectName(_fromUtf8("sliderMax"))
        self.gridLayout.addWidget(self.sliderMax, 2, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(510, 270, 201, 71))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 160, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lcdNumber = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.progressBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber.display)
        QtCore.QObject.connect(self.sliderMax, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdMax.display)
        QtCore.QObject.connect(self.sliderMin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdMin.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Alarmy", None))
        self.label_2.setText(_translate("MainWindow", "Max", None))
        self.button_alarms.setText(_translate("MainWindow", "Potwierdź", None))
        self.label.setText(_translate("MainWindow", "Min", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Volumen de liquido en el tanque", None))
        self.label_4.setText(_translate("MainWindow", "Litros", None))

