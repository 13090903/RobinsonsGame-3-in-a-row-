from PyQt5.QtCore import QRect, QCoreApplication, QMetaObject, Qt
from PyQt5.QtGui import QFont, QPainter, QPen, QColor
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QWidget, QLabel, QPushButton, QLineEdit, QComboBox
from PyQt5.uic.properties import QtWidgets

import Cell
import Game
from Color import Color
from GameField import GameField


class MainMenu(object):
    def __init__(self):
        self.widgetWin1 = None

    def setup_ui(self, Win1):
        Win1.setObjectName("Win1")
        Win1.resize(450, 800)
        self.widgetWin1 = QWidget(Win1)
        self.widgetWin1.setObjectName("widgetWin1")

        Win1.setCentralWidget(self.widgetWin1)
        self.retranslate_ui(Win1)
        QMetaObject.connectSlotsByName(Win1)

    @staticmethod
    def retranslate_ui(Win1):
        _translate = QCoreApplication.translate
        Win1.setWindowTitle(_translate("Win1", "MainWindow"))


class Settings(object):
    def __init__(self):
        self.text2 = None
        self.widgetWin2 = None

    def setup_ui(self, Win2):
        Win2.setObjectName("Win2")
        Win2.resize(450, 800)
        self.widgetWin2 = QWidget(Win2)
        self.widgetWin2.setObjectName("widgetWin2")

        Win2.setCentralWidget(self.widgetWin2)
        self.retranslate_ui(Win2)
        QMetaObject.connectSlotsByName(Win2)

    @staticmethod
    def retranslate_ui(Win2):
        _translate = QCoreApplication.translate
        Win2.setWindowTitle(_translate("Win2", "MainWindow"))


class Rules(object):
    def __init__(self):
        self.text3 = None
        self.widgetWin3 = None

    def setup_ui(self, Win3):
        Win3.setObjectName("Win3")
        Win3.resize(450, 800)
        self.widgetWin3 = QWidget(Win3)
        self.widgetWin3.setObjectName("widgetWin3")
        self.text3 = QLabel(self.widgetWin3)
        self.text3.move(15, 270)
        self.text3.setFont(QFont("Times New Roman", 20))
        self.text3.setObjectName("text3")

        Win3.setCentralWidget(self.widgetWin3)

        self.retranslate_ui(Win3)
        QMetaObject.connectSlotsByName(Win3)

    def retranslate_ui(self, Win3):
        _translate = QCoreApplication.translate
        text = " Уничтожайте поэтапно квадратики, стоящие рядом, одного и того же цвета по два \nи больше. Сосредоточьтесь в первую очередь на этой задаче. Старайтесь убирать \nабсолютно все квадратики с поля на каждом уровне, в противном случае Вам \nпридется пользоваться вспомогательными средствами, которых очень мало. \nЗадействуйте кнопки с буквой R только в самом крайнем случае."
        Win3.setWindowTitle(_translate("Win3", "MainWindow"))
        self.text3.setText(_translate("Win3", text))


class GameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.win = None
        self.painter = QPainter(self)
        self.field_size = 12
        self.field = GameField(self.field_size)
        self.widgetWin4 = None

    def setup_ui(self, Win4):
        Win4.setObjectName("Win4")
        Win4.resize(450, 800)
        self.widgetWin4 = QWidget(Win4)
        self.widgetWin4.setObjectName("widgetWin4")

        Win4.setCentralWidget(self.widgetWin4)
        self.retranslate_ui(Win4)
        QMetaObject.connectSlotsByName(Win4)

        self.win = QLabel("You Win!")
        self.win.setGeometry(800, 500, 300, 100)
        self.win.setFont(QFont("Times New Roman", 42))
        self.win.setVisible(False)

    def draw_window(self, p):
        p.setBrush(Qt.NoBrush)
        pen = QPen(QColor(0, 0, 0))
        pen.setWidth(3)
        p.setPen(pen)
        p.setFont(QFont("Times New Roman", 20))
        p.drawText(700, 635, "Points: " + str(self.points))
        p.drawText(700, 665, "Purpose: " + str(self.purpose))
        p.drawRect(50, 50, 100 + self.field_size * Cell.cell_size * 2, 200 + self.field_size * Cell.cell_size)
        pen.setColor(QColor(255, 255, 0))
        pen.setWidth(2)
        p.setPen(pen)
        p.drawRect(95, 95, self.field_size * Cell.cell_size * 2 + 10, self.field_size * Cell.cell_size + 10)

    def draw_field(self, p):
        for i in range(self.field_size):
            for j in range(self.field_size * 2):
                cell = self.field.field[i][j]
                if cell.color == Color.RED:
                    p.setBrush(Qt.red)
                    p.drawEllipse(100 + j * cell.size, 100 + i * cell.size, cell.size, cell.size)
                elif cell.color == Color.BLUE:
                    p.setBrush(Qt.blue)
                    p.drawEllipse(100 + j * cell.size, 100 + i * cell.size, cell.size, cell.size)
                elif cell.color == Color.GREEN:
                    p.setBrush(Qt.green)
                    p.drawEllipse(100 + j * cell.size, 100 + i * cell.size, cell.size, cell.size)

    @staticmethod
    def retranslate_ui(Win4):
        _translate = QCoreApplication.translate
        Win4.setWindowTitle(_translate("Win4", "MainWindow"))


class Win1(QMainWindow, MainMenu):
    def __init__(self, parent=None):
        super(Win1, self).__init__(parent)
        self.setup_ui(self)


class Win2(QMainWindow, Settings):
    def __init__(self, parent=None):
        super(Win2, self).__init__(parent)
        self.setup_ui(self)


class Win3(QMainWindow, Rules):
    def __init__(self, parent=None):
        super(Win3, self).__init__(parent)
        self.setup_ui(self)


class Win4(QMainWindow, GameWindow):
    def __init__(self, parent=None):
        super(Win4, self).__init__()
        self.points = 0
        self.purpose = 3
        self.setup_ui(self)

    def paintEvent(self, e):
        self.painter.begin(self)
        self.draw_field(self.painter)
        self.draw_window(self.painter)
        self.painter.end()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            if (e.pos().y() - 100) // Cell.cell_size < self.field_size and (
                    e.pos().x() - 100) // Cell.cell_size < self.field_size * 2:
                tuple1 = ((e.pos().y() - 100) // Cell.cell_size, (e.pos().x() - 100) // Cell.cell_size)
                chain = Game.find_chain(self.field.field, tuple1)
                if len(chain) > 1:
                    for k in chain:
                        self.field.field[k[0] - 1][k[1] - 1].color = Color.NONE
                    Game.delete_empty_cells(self.field.field)
                    if len(chain) <= 8:
                        self.points += len(chain)
                    else:
                        self.points += 8 + 2 * (len(chain) - 8)
                    if self.points >= self.purpose:
                        self.win.setVisible(True)
                        self.window().close()

                    self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.shuffle_btn2 = None
        self.shuffle_btn1 = None
        self.shuffle_btn = None
        self.stacked = QStackedWidget(self)
        self.setCentralWidget(self.stacked)

        self.setGeometry(350, 200, 1200, 800)
        self.setWindowTitle('Epic Game')

        self.window_Win1 = Win1(self)
        self.window_Win2 = Win2(self)
        self.window_Win3 = Win3(self)
        self.window_Win4 = Win4(self)

        self.stacked.addWidget(self.window_Win1)
        self.stacked.addWidget(self.window_Win2)
        self.stacked.addWidget(self.window_Win3)
        self.stacked.addWidget(self.window_Win4)

        self.create_buttons(self.window_Win1)
        self.window_Win1.setStyleSheet('#Win1 {background-color: #FFD700;}')

    def create_shuffle_button(self, parent):
        self.shuffle_btn = QPushButton("R", parent)
        self.shuffle_btn.setGeometry(QRect(100, 600, 50, 50))
        self.shuffle_btn.setFont(QFont("Times New Roman", 20))
        self.shuffle_btn.clicked.connect(self.shuffle_btn_clicked)
        self.shuffle_btn.show()

        self.shuffle_btn1 = QPushButton("R", parent)
        self.shuffle_btn1.setGeometry(QRect(165, 600, 50, 50))
        self.shuffle_btn1.setFont(QFont("Times New Roman", 20))
        self.shuffle_btn1.clicked.connect(self.shuffle_btn_clicked1)
        self.shuffle_btn1.show()

        self.shuffle_btn2 = QPushButton("R", parent)
        self.shuffle_btn2.setGeometry(QRect(230, 600, 50, 50))
        self.shuffle_btn2.setFont(QFont("Times New Roman", 20))
        self.shuffle_btn2.clicked.connect(self.shuffle_btn_clicked2)
        self.shuffle_btn2.show()

    def shuffle_btn_clicked(self):
        Game.shuffle(self.window_Win4.field.field)
        self.shuffle_btn.setEnabled(False)
        self.update()

    def shuffle_btn_clicked1(self):
        Game.shuffle(self.window_Win4.field.field)
        self.shuffle_btn1.setEnabled(False)
        self.update()

    def shuffle_btn_clicked2(self):
        Game.shuffle(self.window_Win4.field.field)
        self.shuffle_btn2.setEnabled(False)
        self.update()

    def create_button_back(self, parent):
        btn_back = QPushButton("Back", parent)
        btn_back.setGeometry(QRect(0, 0, 75, 30))
        btn_back.clicked.connect(self.go_win1)
        btn_back.show()

    def create_buttons(self, parent):
        btn = QPushButton("Start", parent)
        btn.setGeometry(QRect(500, 200, 200, 40))

        btn_2 = QPushButton("Settings", parent)
        btn_2.setGeometry(QRect(500, 320, 200, 40))

        btn_3 = QPushButton("Rules", parent)
        btn_3.setGeometry(QRect(500, 440, 200, 40))

        btn.clicked.connect(self.go_win4)
        btn_2.clicked.connect(self.go_win2)
        btn_3.clicked.connect(self.go_win3)
        btn.show()
        btn_2.show()
        btn_3.show()

    @staticmethod
    def create_settings(parent):
        label = QLabel("Field size", parent)
        label.setGeometry(537, 230, 140, 80)
        label.setFont(QFont("Times New Roman", 20))
        combo = QComboBox(parent)
        combo.setGeometry(530, 300, 135, 50)
        combo.addItems(["6 x 12", "8 x 16", "10 x 20", "12 x 24"])
        combo.setFont(QFont("Times New Roman", 20))
        btn = QPushButton("Save", parent)
        btn.setGeometry(QRect(560, 360, 70, 40))
        combo.show()
        label.show()

    def go_win1(self):
        self.stacked.setCurrentIndex(0)

    def go_win2(self):
        self.stacked.setCurrentIndex(1)
        self.create_button_back(self.window_Win2)
        self.create_settings(self.window_Win2)

    def go_win3(self):
        self.stacked.setCurrentIndex(2)
        self.create_button_back(self.window_Win3)

    def go_win4(self):
        self.stacked.setCurrentIndex(3)
        self.create_button_back(self.window_Win4)
        self.create_shuffle_button(self.window_Win4)
