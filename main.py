
import sys
from gui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from stt import STT
import tts
import AI
import conversations


# начать прослушивание команд
#stt.va_listen(va_respond)

# Интерфейс программы и обработчик событий внутри него
class Bot(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # Отключаем стандартные границы окна программы
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        # Обработчики основных кнопок + кнопок с панели
        self.ui.send_messg.clicked.connect(self.send_message)
        self.ui.exit_win.clicked.connect(lambda: self.close())
        self.ui.clear_bar.clicked.connect(self.clear_dialog)
        self.ui.hide_win.clicked.connect(lambda: self.showMinimized())
        self.ui.audio_checkbox.stateChanged.connect(self.change_audio_mode)

        self.audio_mode = None
        self.thread = None
        self.stt = STT()
        self.tts = tts.TTS()
        self.tts.start()




   
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass




    # Обработчик сигналов из потока
    def bot_message(self, text: str):
        # Обработка сообщений бота

        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeft)
        item.setText(f"Кеша:\n{text}")
        self.ui.listWidget.addItem(item)



    # Отправить сообщение в диалог
    def send_message(self):
        message_text = self.ui.lineEdit.text()
        if len(message_text) > 0:
            # Добавляем свое сообщение в ListWidget
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignRight)
            item.setText(f"(ВЫ):\n{message_text}")
            self.ui.listWidget.addItem(item)
            AI.va_respond(message_text)
            

    def clear_dialog(self):
        self.ui.listWidget.clear()
        conversations.history = []
        conversations.switch_key = False
    
    def change_audio_mode(self, state):
        self.audio_mode = state
        if state == QtCore.Qt.Checked:
            self.stt.start()
        else:
            self.stt.requestInterruption()


    

app = QtWidgets.QApplication(sys.argv)
myapp = Bot()
myapp.show()
tts.tts_gui_init(myapp)
sys.exit(app.exec_())
