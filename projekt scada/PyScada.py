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
        MainWindow.resize(863, 640)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("QWidget { background-color:rgb(235, 234, 255) }"))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(771, 581))
        self.tabWidget.setMaximumSize(QtCore.QSize(771, 581))
        self.tabWidget.setStyleSheet(_fromUtf8("QWidget { background-color:rgb(235, 234, 255)}"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.panel_operatora = QtGui.QWidget()
        self.panel_operatora.setObjectName(_fromUtf8("panel_operatora"))
        self.groupBox_2 = QtGui.QGroupBox(self.panel_operatora)
        self.groupBox_2.setGeometry(QtCore.QRect(500, 210, 211, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(19, 20, 161, 61))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lcdNumber = QtGui.QLCDNumber(self.horizontalLayoutWidget)
        self.lcdNumber.setFrameShape(QtGui.QFrame.Box)
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
        self.groupBox = QtGui.QGroupBox(self.panel_operatora)
        self.groupBox.setGeometry(QtCore.QRect(510, 30, 201, 151))
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
        self.groupBox_3 = QtGui.QGroupBox(self.panel_operatora)
        self.groupBox_3.setGeometry(QtCore.QRect(70, 330, 601, 161))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.progressBar = QtGui.QProgressBar(self.groupBox_3)
        self.progressBar.setGeometry(QtCore.QRect(20, 60, 560, 60))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(_fromUtf8("QProgressBar {\n"
"border: 1px solid black;\n"
"text-align: top;\n"
"padding: 3px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
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
"border-bottom-right-radius: 15px;\n"
"border-bottom-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"border-top-left-radius: 15px;\n"
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
        self.nivel_min_3 = QtGui.QFrame(self.groupBox_3)
        self.nivel_min_3.setEnabled(True)
        self.nivel_min_3.setGeometry(QtCore.QRect(90, 60, 10, 60))
        self.nivel_min_3.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"padding: 2px;\n"
"background-color: red;"))
        self.nivel_min_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nivel_min_3.setFrameShadow(QtGui.QFrame.Raised)
        self.nivel_min_3.setObjectName(_fromUtf8("nivel_min_3"))
        self.nivel_max_3 = QtGui.QFrame(self.groupBox_3)
        self.nivel_max_3.setEnabled(False)
        self.nivel_max_3.setGeometry(QtCore.QRect(500, 60, 10, 60))
        self.nivel_max_3.setAutoFillBackground(False)
        self.nivel_max_3.setStyleSheet(_fromUtf8("QFrame {\n"
"border: 1px solid black;\n"
"text-align: top;\n"
"padding: 3px;\n"
"border-bottom-right-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"border-top-left-radius: 10px;\n"
"\n"
"background-color: red\n"
"}"))
        self.nivel_max_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nivel_max_3.setFrameShadow(QtGui.QFrame.Raised)
        self.nivel_max_3.setObjectName(_fromUtf8("nivel_max_3"))
        self.nivel_min_2 = QtGui.QFrame(self.groupBox_3)
        self.nivel_min_2.setGeometry(QtCore.QRect(60, 30, 16, 16))
        self.nivel_min_2.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"padding: 2px;\n"
"background-color: #FFFAFA;"))
        self.nivel_min_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nivel_min_2.setFrameShadow(QtGui.QFrame.Raised)
        self.nivel_min_2.setObjectName(_fromUtf8("nivel_min_2"))
        self.nivel_max_2 = QtGui.QFrame(self.groupBox_3)
        self.nivel_max_2.setGeometry(QtCore.QRect(530, 30, 16, 16))
        self.nivel_max_2.setStyleSheet(_fromUtf8("border: 1px solid black;\n"
"padding: 2px;\n"
"background-color: #FFFAFA;\n"
"\n"
""))
        self.nivel_max_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.nivel_max_2.setFrameShadow(QtGui.QFrame.Raised)
        self.nivel_max_2.setObjectName(_fromUtf8("nivel_max_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.panel_operatora)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 20, 181, 111))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 161, 81))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.connectServer = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.connectServer.setObjectName(_fromUtf8("connectServer"))
        self.verticalLayout.addWidget(self.connectServer)
        self.disconnectServer = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.disconnectServer.setObjectName(_fromUtf8("disconnectServer"))
        self.verticalLayout.addWidget(self.disconnectServer)
        self.tabWidget.addTab(self.panel_operatora, _fromUtf8(""))
        self.plot = QtGui.QWidget()
        self.plot.setObjectName(_fromUtf8("plot"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.plot)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 771, 561))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget.addTab(self.plot, _fromUtf8(""))
        self.log = QtGui.QWidget()
        self.log.setObjectName(_fromUtf8("log"))
        self.gridLayoutWidget_3 = QtGui.QWidget(self.log)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 771, 481))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_6 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.listWidget = QtGui.QListWidget(self.gridLayoutWidget_3)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout_6.addWidget(self.listWidget, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.log)
        self.label_3.setGeometry(QtCore.QRect(10, 490, 101, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.clearLogs = QtGui.QPushButton(self.log)
        self.clearLogs.setGeometry(QtCore.QRect(130, 520, 131, 31))
        self.clearLogs.setObjectName(_fromUtf8("clearLogs"))
        self.comboBox = QtGui.QComboBox(self.log)
        self.comboBox.setGeometry(QtCore.QRect(10, 520, 121, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.scroll = QtGui.QCheckBox(self.log)
        self.scroll.setGeometry(QtCore.QRect(280, 520, 81, 31))
        self.scroll.setObjectName(_fromUtf8("scroll"))
        self.tabWidget.addTab(self.log, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.sliderMax, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdMax.display)
        QtCore.QObject.connect(self.sliderMin, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdMin.display)
        QtCore.QObject.connect(self.progressBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.lcdNumber.display)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Położenie", None))
        self.label_4.setText(_translate("MainWindow", "[m]", None))
        self.groupBox.setTitle(_translate("MainWindow", "Alarmy", None))
        self.label_2.setText(_translate("MainWindow", "Max", None))
        self.button_alarms.setText(_translate("MainWindow", "Potwierdź", None))
        self.label.setText(_translate("MainWindow", "Min", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Display", None))
        self.progressBar.setFormat(_translate("MainWindow", "%p%", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "OPC DA Server", None))
        self.connectServer.setText(_translate("MainWindow", "Connect", None))
        self.disconnectServer.setText(_translate("MainWindow", "Disconnect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.panel_operatora), _translate("MainWindow", "Panel Operatorski", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plot), _translate("MainWindow", "Wykres", None))
        self.label_3.setText(_translate("MainWindow", "Set log level", None))
        self.clearLogs.setText(_translate("MainWindow", "Clear", None))
        self.comboBox.setItemText(0, _translate("MainWindow", "DEBUG", None))
        self.comboBox.setItemText(1, _translate("MainWindow", "INFO", None))
        self.comboBox.setItemText(2, _translate("MainWindow", "WARNING", None))
        self.comboBox.setItemText(3, _translate("MainWindow", "ERROR", None))
        self.scroll.setText(_translate("MainWindow", "scroll", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.log), _translate("MainWindow", "Log", None))

