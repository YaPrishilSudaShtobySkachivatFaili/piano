# coding: utf-8
import sys
from PyQt5 import uic
import player
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QApplication, QMainWindow


class BTField(QWidget):
    def __init__(self):
        super(Canvas, self).__init__()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.b1()
        elif event.key() == Qt.Key_W:
            self.b2()
        elif event.key() == Qt.Key_E:
            self.b3()
        elif event.key() == Qt.Key_R:
            self.b4()
        elif event.key() == Qt.Key_T:
            self.b5()
        elif event.key() == Qt.Key_Y:
            self.b6()
        elif event.key() == Qt.Key_U:
            self.b7()

    def b1(self):
        media = QtCore.QUrl.fromLocalFile('/media/1.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.player.play = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def b2(self):
        media = QtCore.QUrl.fromLocalFile('/media/2.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.player.play = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def b3(self):
        media = QtCore.QUrl.fromLocalFile('/media/3.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.player.play = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def b4(self):
        media = QtCore.QUrl.fromLocalFile('/media/4.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.player.play = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def b5(self):
        media = QtCore.QUrl.fromLocalFile('/media/5.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.player.play = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def b6(self):
        media = QtCore.QUrl.fromLocalFile('/media/6.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.player.play = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)

    def b7(self):
        media = QtCore.QUrl.fromLocalFile('/media/7.mp3')
        content = QtMultimedia.QMediaContent(media)
        self.player.play = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("untitled1.ui", self)
        self.setCentralWidget(BTField())
        self.setWindowTitle('Фортепиано')
        self.pb1.clicked.connect(self.centralWidget().b1)
        self.pb2.clicked.connect(self.centralWidget().b2)
        self.pb3.clicked.connect(self.centralWidget().b3)
        self.pb4.clicked.connect(self.centralWidget().b4)
        self.pb5.clicked.connect(self.centralWidget().b5)
        self.pb6.clicked.connect(self.centralWidget().b6)
        self.pb7.clicked.connect(self.centralWidget().b7)


if __name__ == '__main__':  # Основной цикл
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
