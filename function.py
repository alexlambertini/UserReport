from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog, QMessageBox)
from PyQt5 import QtCore, QtGui, QtWidgets


if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Principal = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(Principal)
        Principal.show()
        sys.exit(app.exec_())

