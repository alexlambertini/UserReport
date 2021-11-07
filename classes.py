from PyQt5.QtCore import showbase
from PyQt5.QtWidgets import QMessageBox

class ShowPopup:
    def __init__(self, titulo, mensagem):

        self.msg = QMessageBox()
        self.msg.setWindowTitle = titulo
        self.msg.setText = mensagem

        self.msg.exec_()

   