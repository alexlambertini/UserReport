from PySide2.QtWidgets import QMessageBox
from PySide2 import QtGui
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


def consultarDados(date):
        try:
                banco = sqlite3.connect('relatorios.db')
                cursor = banco.cursor()
                
                # filtering using date - WHERE date equal to current selection
                cursor.execute("SELECT * FROM dados WHERE data='{}'".format(date))
                print("SELECT * FROM dados WHERE data='{}'".format(date))

                sql = cursor.fetchall()

                '''
                pessoas = [({'nome': '?', 'email': '?', 'DD': '?', 'telefone': '?', 'caso': '?', 'data': '?'}),
                '''
                file_data = 'registro-{}.txt'.format(date)

                # for dados in sql:
                #         print(dados)
                with open(file_data, 'w') as file:             
                        print('Beign writing {} to txt'.format(sql))
                        file.write(str(sql))
                        print('End writing {} to txt'.format(sql))
                        file.flush()

        except Exception as err:
                print(err)
                ShowPopup("Alerta","Não foi possível consultar dados")
consultarDados('2021-11-13')