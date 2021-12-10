from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from models import *
from PyQt5.uic import loadUiType
import urllib.request

import os
from os import path

ui, _ = loadUiType('views/untitled.ui')


class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_buttons()

    def handle_buttons(self):

        self.cancel_sto.clicked.connect(self.close)
        self.compute_stochastic_queue.clicked.connect(self.close)
        self.cancel.clicked.connect(self.close)
        self.compute_deterministic.clicked.connect(self.close)
        self.make_graph.clicked.connect(self.close)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

