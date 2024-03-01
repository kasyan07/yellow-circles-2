from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import QtCore, QtWidgets
import sys
import random


class UiMainWindow(object):
    def setupui(self, window):
        window.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(window)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 350, 180, 40))
        self.pushButton.setText('Нарисовать окружность')
        window.setCentralWidget(self.centralwidget)


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.setupui(self)
        self.drawing = False
        self.setWindowTitle('Окружность')
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.drawing = True
        self.update()

    def paintEvent(self, event):
        self.size = random.randint(10, 100)
        if self.drawing:
            painter = QPainter()
            painter .begin(self)
            painter.setPen(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            painter.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.x, self.y = random.randint(0, 500), random.randint(0, 500)
            painter.drawEllipse(self.x, self.y, self.size, self.size)
            painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
