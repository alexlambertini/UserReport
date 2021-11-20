from typing import Text
from PySide2.QtWidgets import QMessageBox
from PySide2 import QtGui
import sqlite3 
import codecs

def ShowPopup(titulo, mensagem):

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

                # file para registro usando data atual
                file_data = 'registro-{}.txt'.format(date)

                with codecs.open(file_data, 'w', 'utf-8') as file:             


                        # apenas para registro - inicio da escrita
                        print('Beign writing {} to txt'.format(sql))

                        # --- organizando os dados
                        # --- muito cuidado, pois esta sempre sobrescrevendo no dia.
                        for data in range(0, len(sql)):

                           Nome = sql[data][0]
                           Email = sql[data][1]
                           DD = sql[data][2]
                           Telefone = sql[data][3]
                           Relatorio = sql[data][4]

                           report = "Nome: {}\n".format(Nome)
                           report += "E-mail: {}\n".format(Email)
                           report += "Telefone: {}\n".format(str(DD) + '-' + str(Telefone + "\n"))
                           report += "Relatório: {}\n\n".format("\n" + Relatorio)
                           report += '-' *200 + '\n\n'
                           file.write(report)


                        # fim da escrita.
                        print('End writing {} to txt'.format(sql))
                        file.flush()

                        ShowPopup("Informação","Dados exportados com sucesso!")

        except Exception as err:
                print(err)
                ShowPopup("Alerta","Não foi possível consultar dados")
