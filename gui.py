from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(862, 531)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 831, 501))
        self.frame.setStyleSheet("QFrame{\n"
"    border-radius: 7px;\n"
"    background-color: #1B1D23;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(290, 350, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border-radius: 7px;\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.send_messg = QtWidgets.QPushButton(self.frame)
        self.send_messg.setGeometry(QtCore.QRect(290, 400, 261, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.send_messg.setFont(font)
        self.send_messg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_messg.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 7px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.send_messg.setObjectName("send_messg")

        self.clear_bar = QtWidgets.QPushButton(self.frame)
        self.clear_bar.setGeometry(QtCore.QRect(560, 400, 261, 90))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.clear_bar.setFont(font)
        self.clear_bar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clear_bar.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 7px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.clear_bar.setObjectName("clear_bar")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(-1, 0, 831, 31))
        self.frame_3.setStyleSheet("QFrame{\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #2C313C;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.exit_win = QtWidgets.QPushButton(self.frame_3)
        self.exit_win.setGeometry(QtCore.QRect(790, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.exit_win.setFont(font)
        self.exit_win.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_win.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.exit_win.setObjectName("exit_win")
        self.hide_win = QtWidgets.QPushButton(self.frame_3)
        self.hide_win.setGeometry(QtCore.QRect(750, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hide_win.setFont(font)
        self.hide_win.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hide_win.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.hide_win.setDefault(False)
        self.hide_win.setObjectName("hide_win")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 40, 271, 451))
        self.frame_4.setStyleSheet("QFrame{\n"
"    color: white;\n"
"    border-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(0, 0, 271, 60))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.audio_checkbox = QtWidgets.QCheckBox(self.frame_4)
        self.audio_checkbox.setGeometry(QtCore.QRect(70, 225, 271, 60))
        self.audio_checkbox.setFont(font)
        self.audio_checkbox.setObjectName("audio_cb")
        self.audio_checkbox.setStyleSheet("color: white;\n"
"border-radius: 7px;\n"
"background-color: #2C313C;\n"
"")
        
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(290, 41, 531, 301))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.listWidget.setFont(font)
        self.listWidget.setTabletTracking(False)
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setStyleSheet("color: white;\n"
"border-radius: 7px;\n"
"background-color: #2C313C;\n"
"")
        self.listWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.listWidget.setLineWidth(1)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.listWidget.setAutoScroll(True)
        self.listWidget.setTabKeyNavigation(False)
        self.listWidget.setProperty("showDropIndicator", True)
        self.listWidget.setDragDropOverwriteMode(False)
        self.listWidget.setAlternatingRowColors(False)
        self.listWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setWordWrap(True)
        self.listWidget.setSelectionRectVisible(False)
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send_messg.setText(_translate("MainWindow", "Отправить"))
        self.clear_bar.setText(_translate("MainWindow", "Очистить"))
        self.exit_win.setText(_translate("MainWindow", "X"))
        self.hide_win.setText(_translate("MainWindow", "_"))
        self.label.setText(_translate("MainWindow", "Добро пожаловать!\n Это GUI голосового помощника\nВерсия - 1.4"))
        self.audio_checkbox.setText("Голосовой ввод")
        self.listWidget.setSortingEnabled(False)








