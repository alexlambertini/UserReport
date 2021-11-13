from PySide2.QtCore import showbase
from PySide2.QtWidgets import QMessageBox

class ShowPopup:
    def __init__(self, titulo, mensagem):

        self.msg = QMessageBox()
        self.msg.setWindowTitle = titulo
        self.msg.setText = mensagem

        self.msg.exec_()

   