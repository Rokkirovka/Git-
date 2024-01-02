import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import QPointF
from random import randint


class Circle(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)
        self.r = 0
        self.lst = []

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for i in self.lst:
            qp.setBrush(i[1])
            qp.drawEllipse(*i[0])
        qp.end()

    def draw(self):
        r = randint(5, 100)
        p = QPointF(randint(30, 370), randint(30, 370))
        c = QColor(*(randint(0, 255) for _ in range(3)))
        self.lst.append(((p, r, r), c))
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
