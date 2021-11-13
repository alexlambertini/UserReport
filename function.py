from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui
import sqlite3

def ShowPopup(titulo, mensagem):
        print("não foi")
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowIcon(QtGui.QIcon('ico/relatorio.ico'))
        msgBox.setWindowTitle(titulo)
        msgBox.setText(mensagem)
        msgBox.setStandardButtons(QMessageBox.Ok)
   
        msgBox.exec_()


def consultarDados():
        try:
                banco = sqlite3.connect('relatorios.db')
                cursor = banco.cursor()
                cursor.execute("SELECT * FROM dados")

                sql = cursor.fetchall()

                ''''
                pessoas = [({'nome': '?', 'email': '?', 'DD': '?', 'telefone': '?', 'caso': '?', 'data': '?'}),

                for dados in sql:
                   with open('relatorio.txt', 'w') as f:
                      f.writelines(dados)
                      f.write('\n')
                '''


        except:
                ShowPopup("Alerta","Não foi possível consultar dados")