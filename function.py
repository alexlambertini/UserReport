from typing import Text
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
                print('Data found in records: {}'.format(len(sql)))

                # file para registro usando data atual
                file_data = 'registro-{}.txt'.format(date)

                # for dados in sql:
                # apenas para registro - inicio da escrita
                # print('Beign writing {} to txt'.format(sql))
                # --- organizando os dados
                # --- muito cuidado, pois esta sempre sobrescrevendo no dia.
                # 
                tmp = []
                file = open(file_data, 'w')
                        
                for data in range(0, len(sql)):
                        # print(data[4])
                        nome = sql[data][0]
                        mensagem = sql[data][4]
                        # # build report
                        report = 'Nome: {}\n'.format(nome)
                        report += 'Mensagem: {}'.format(mensagem)
                        print(str(report))
                        file.write(str(report))
                file.flush()
        except Exception as err:
                print(err)
                ShowPopup("Alerta","Não foi possível consultar dados")

if __name__ == "__main__":
        consultarDados('2021-11-09')