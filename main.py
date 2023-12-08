import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor


def except_hook(cls, exception, traceback):
    sys.__excepthook(cls, exception, traceback)
    
    
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.draw)
        self.draw_flag = False
        
    def draw(self):
        self.draw_flag = True
        self.update()
        
    def paintEvent(self, event):
        if self.draw_flag:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('yellow'))
            qp.setPen(QColor('orange'))
            for _ in range(randint(5, 10)):
                radius = randint(1, 100)
                qp.drawEllipse(randint(0, 800), randint(80, 600), radius, radius)
            qp.end()
                
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
