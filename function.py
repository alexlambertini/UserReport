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
                print(sql[0][0])

                with open(file_data, 'w') as file:             
                        # apenas para registro - inicio da escrita
                        print('Beign writing {} to txt'.format(sql))
                        # --- organizando os dados
                        # --- muito cuidado, pois esta sempre sobrescrevendo no dia.
                        # 
                        file.write(str(sql))
                        # para debug apenas
                        print("Para nome -> {}".format(sql[0][0]))
                        print("Para email -> {}".format(sql[0][1]))
                        print("Para ddd -> {}".format(sql[0][2]))
                        print("Para telefone -> {}".format(sql[0][3]))
                        print("Para report -> {}".format(sql[0][4]))
                        print("Para data -> {}".format(sql[0][5]))

                        # fim da escrita.
                        print('End writing {} to txt'.format(sql))
                        file.flush()
        except Exception as err:
                print(err)
                ShowPopup("Alerta","Não foi possível consultar dados")

if __name__ == "__main__":
        consultarDados('2021-11-13')