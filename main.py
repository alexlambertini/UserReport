import sqlite3
from PySide2 import QtCore, QtGui, QtWidgets
from requests.api import get
from window_export import Ui_ExportWindow
from datetime import date
from pycep_correios import get_address_from_cep, WebService, exceptions
from function import ShowPopup


class Ui_MainWindow(object):
    
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ExportWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(901, 592)
        MainWindow.setFixedSize(901,592)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Ico/relatorio.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_relatorio = QtWidgets.QFrame(self.centralwidget)
        self.frame_relatorio.setEnabled(True)
        self.frame_relatorio.setGeometry(QtCore.QRect(0, 0, 931, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_relatorio.sizePolicy().hasHeightForWidth())
        self.frame_relatorio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.frame_relatorio.setFont(font)
        self.frame_relatorio.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.frame_relatorio.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_relatorio.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_relatorio.setObjectName("frame_relatorio")
        self.image = QtWidgets.QLabel(self.frame_relatorio)
        self.image.setGeometry(QtCore.QRect(0, 0, 391, 591))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("Images/image-woman.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_relatorio)
        self.tabWidget.setGeometry(QtCore.QRect(400, 10, 551, 591))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(True)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setStyleSheet("background: #fff;\n"
"border:0 none;\n"
"font: 9pt \"Roboto Medium\";\n"
"color:#666;\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_relatorio = QtWidgets.QWidget()
        self.tab_relatorio.setObjectName("tab_relatorio")
        self.Titulo = QtWidgets.QLabel(self.tab_relatorio)
        self.Titulo.setGeometry(QtCore.QRect(30, 30, 430, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Titulo.setFont(font)
        self.Titulo.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Titulo.setStyleSheet("font: 57 22.9pt \"Roboto Black\";\n"
"color: \"#0081D5\";")
        self.Titulo.setObjectName("Titulo")
        self.input_nome = QtWidgets.QLineEdit(self.tab_relatorio)
        self.input_nome.setGeometry(QtCore.QRect(30, 110, 430, 38))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.input_nome.setFont(font)
        self.input_nome.setTabletTracking(False)
        self.input_nome.setAccessibleDescription("")
        self.input_nome.setStyleSheet("QLineEdit {\n"
"    background-color:\"#FAFAFA\";\n"
"    border-radius:8px;\n"
"    border:1px solid;\n"
"    border-color: rgb(239, 239, 239);\n"
"    color:\"#444\";\n"
"    font: 10.5pt \"Quicksand\";\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border:1px solid \"#0099FC\"\n"
"}\n"
"")
        self.input_nome.setText("")
        self.input_nome.setObjectName("input_nome")
        self.label_nome_2 = QtWidgets.QLabel(self.tab_relatorio)
        self.label_nome_2.setGeometry(QtCore.QRect(32, 90, 47, 13))
        self.label_nome_2.setStyleSheet("font: 57 10.5pt \"Roboto Medium\";\n"
"color:\"#333333\"")
        self.label_nome_2.setObjectName("label_nome_2")
        self.input_email = QtWidgets.QLineEdit(self.tab_relatorio)
        self.input_email.setGeometry(QtCore.QRect(30, 190, 430, 38))
        self.input_email.setStyleSheet("QLineEdit {\n"
"    background-color:\"#FAFAFA\";\n"
"    border-radius:8px;\n"
"    border:1px solid;\n"
"    border-color: rgb(239, 239, 239);\n"
"    color:\"#444\";\n"
"    font: 10.5pt \"Quicksand\";\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border:1px solid \"#0099FC\"\n"
"}\n"
"")
        self.input_email.setObjectName("input_email")
        self.label_email = QtWidgets.QLabel(self.tab_relatorio)
        self.label_email.setGeometry(QtCore.QRect(32, 170, 47, 13))
        self.label_email.setStyleSheet("font: 57 10.5pt \"Roboto\";\n"
"color:\"#333333\"")
        self.label_email.setObjectName("label_email")
        self.label_ddd = QtWidgets.QLabel(self.tab_relatorio)
        self.label_ddd.setGeometry(QtCore.QRect(32, 250, 61, 16))
        self.label_ddd.setStyleSheet("font: 57 10.5pt \"Roboto\";\n"
"color:\"#333333\"")
        self.label_ddd.setObjectName("label_ddd")
        self.input_ddd = QtWidgets.QLineEdit(self.tab_relatorio)
        self.input_ddd.setGeometry(QtCore.QRect(30, 270, 61, 38))
        self.input_ddd.setStyleSheet("QLineEdit {\n"
"    background-color:\"#FAFAFA\";\n"
"    border-radius:8px;\n"
"    border:1px solid;\n"
"    border-color: rgb(239, 239, 239);\n"
"    color:\"#444\";\n"
"    font: 10.5pt \"Quicksand\";\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border:1px solid \"#0099FC\"\n"
"}\n"
"")
        self.input_ddd.setObjectName("input_ddd")
        self.input_telefone = QtWidgets.QLineEdit(self.tab_relatorio)
        self.input_telefone.setGeometry(QtCore.QRect(110, 270, 351, 38))
        self.input_telefone.setStyleSheet("QLineEdit {\n"
"    background-color:\"#FAFAFA\";\n"
"    border-radius:8px;\n"
"    border:1px solid;\n"
"    border-color: rgb(239, 239, 239);\n"
"    color:\"#444\";\n"
"    font: 10.5pt \"Quicksand\";\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border:1px solid \"#0099FC\"\n"
"}\n"
"")
        self.input_telefone.setObjectName("input_telefone")
        self.label_telefone = QtWidgets.QLabel(self.tab_relatorio)
        self.label_telefone.setGeometry(QtCore.QRect(112, 250, 61, 16))
        self.label_telefone.setStyleSheet("font: 57 10.5pt \"Roboto\";\n"
"color:\"#333333\"")
        self.label_telefone.setObjectName("label_telefone")
        self.label_relatorio = QtWidgets.QLabel(self.tab_relatorio)
        self.label_relatorio.setGeometry(QtCore.QRect(32, 330, 61, 16))
        self.label_relatorio.setStyleSheet("font: 57 10.5pt \"Roboto Medium\";\n"
"color:\"#333333\"")
        self.label_relatorio.setObjectName("label_relatorio")
        self.textbox_caso = QtWidgets.QTextEdit(self.tab_relatorio)
        self.textbox_caso.setGeometry(QtCore.QRect(30, 350, 430, 141))
        self.textbox_caso.setStyleSheet("QTextEdit {\n"
"    background-color:\"#FAFAFA\";\n"
"    border-radius:8px;\n"
"    border:1px solid;\n"
"    border-color: rgb(239, 239, 239);\n"
"    color:\"#444\";\n"
"    font: 10.5pt \"Quicksand\";\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border:1px solid \"#0099FC\"\n"
"}\n"
"")
        self.textbox_caso.setTabChangesFocus(False)
        self.textbox_caso.setObjectName("textbox_caso")
        self.btn_salvar = QtWidgets.QPushButton(self.tab_relatorio)
        self.btn_salvar.setGeometry(QtCore.QRect(370, 510, 90, 30))
        self.btn_salvar.setStyleSheet("QPushButton {\n"
"    background-color:\"#0081D5\";\n"
"    border-radius: 5px;\n"
"    color:\"white\";\n"
"    font: 75 11pt \"Roboto Medium\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:\"#0093F2\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:\"#0075C1\"\n"
"}")
        self.btn_salvar.setObjectName("btn_salvar")
        self.btn_exportar = QtWidgets.QPushButton(self.tab_relatorio)
        self.btn_exportar.setGeometry(QtCore.QRect(270, 510, 90, 30))
        self.btn_exportar.setStyleSheet("QPushButton {\n"
"    background-color:\"#3AB44E\";\n"
"    border-radius: 5px;\n"
"    color:\"white\";\n"
"    font: 75 11pt \"Roboto Medium\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:\"#62CC74\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:\"#34A045\"\n"
"}")
        self.btn_exportar.setObjectName("btn_exportar")
        self.tabWidget.addTab(self.tab_relatorio, "")
        self.tab_correios = QtWidgets.QWidget()
        self.tab_correios.setObjectName("tab_correios")
        self.Titulo_Cep = QtWidgets.QLabel(self.tab_correios)
        self.Titulo_Cep.setGeometry(QtCore.QRect(30, 30, 430, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.Titulo_Cep.setFont(font)
        self.Titulo_Cep.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Titulo_Cep.setStyleSheet("font: 57 22.9pt \"Roboto Black\";\n"
"color: \"#0081D5\";\n"
"text-transform: uppercase;\n"
"")
        self.Titulo_Cep.setObjectName("Titulo_Cep")
        self.input_cep = QtWidgets.QLineEdit(self.tab_correios)
        self.input_cep.setGeometry(QtCore.QRect(30, 110, 430, 38))
        self.input_cep.setStyleSheet("QLineEdit {\n"
"    background-color:\"#FAFAFA\";\n"
"    border-radius:8px;\n"
"    border:1px solid;\n"
"    border-color: rgb(239, 239, 239);\n"
"    color:\"#444\";\n"
"    font: 10.5pt \"Quicksand\";\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border:2px solid \"#E3E3E3\"\n"
"}\n"
"")
        self.input_cep.setObjectName("input_cep")
        self.label_cep = QtWidgets.QLabel(self.tab_correios)
        self.label_cep.setGeometry(QtCore.QRect(30, 90, 47, 13))
        self.label_cep.setStyleSheet("font: 57 10.5pt \"Roboto Medium\";\n"
"color:\"#333333\";\n"
"background: transparent;")
        self.label_cep.setObjectName("label_cep")
        self.input_cidade = QtWidgets.QLineEdit(self.tab_correios)
        self.input_cidade.setGeometry(QtCore.QRect(50, 230, 291, 38))
        self.input_cidade.setStyleSheet("QLineEdit {\n"
"    background-color:\"#FAFAFA\";\n"
"    border-radius:8px;\n"
"    border:1px solid;\n"
"    border-color: rgb(239, 239, 239);\n"
"    color:\"#444\";\n"
"    font: 10.5pt \"Quicksand\";\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border:2px solid \"#E3E3E3\"\n"
"}\n"
"")
        self.input_cidade.setObjectName("input_cidade")
        self.label_cidade = QtWidgets.QLabel(self.tab_correios)
        self.label_cidade.setGeometry(QtCore.QRect(52, 208, 47, 13))
        self.label_cidade.setStyleSheet("font: 57 10.5pt \"Roboto\";\n"
"color:\"#333333\"")
        self.label_cidade.setObjectName("label_cidade")
        self.label_logradouro = QtWidgets.QLabel(self.tab_correios)
        self.label_logradouro.setGeometry(QtCore.QRect(52, 295, 81, 21))
        self.label_logradouro.setStyleSheet("font: 57 10.5pt \"Roboto\";\n"
"color:\"#333333\";\n"
"background: transparent;")
        self.label_logradouro.setObjectName("label_logradouro")
        self.input_logradouro = QtWidgets.QLineEdit(self.tab_correios)
        self.input_logradouro.setGeometry(QtCore.QRect(50, 320, 380, 38))
        self.input_logradouro.setStyleSheet("QLineEdit {\n"
"    background-color:\"#FAFAFA\";\n"
"    border-radius:8px;\n"
"    border:1px solid;\n"
"    border-color: rgb(239, 239, 239);\n"
"    color:\"#444\";\n"
"    font: 10.5pt \"Quicksand\";\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border:2px solid \"#E3E3E3\"\n"
"}\n"
"")
        self.input_logradouro.setObjectName("input_logradouro")
        self.label_bairro = QtWidgets.QLabel(self.tab_correios)
        self.label_bairro.setGeometry(QtCore.QRect(52, 380, 81, 21))
        self.label_bairro.setStyleSheet("font: 57 10.5pt \"Roboto\";\n"
"color:\"#333333\";\n"
"background: transparent;")
        self.label_bairro.setObjectName("label_bairro")
        self.input_bairro = QtWidgets.QLineEdit(self.tab_correios)
        self.input_bairro.setGeometry(QtCore.QRect(50, 410, 380, 38))
        self.input_bairro.setStyleSheet("QLineEdit {\n"
"    background-color:\"#FAFAFA\";\n"
"    border-radius:8px;\n"
"    border:1px solid;\n"
"    border-color: rgb(239, 239, 239);\n"
"    color:\"#444\";\n"
"    font: 10.5pt \"Quicksand\";\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border:2px solid \"#E3E3E3\"\n"
"}\n"
"")
        self.input_bairro.setObjectName("input_bairro")
        self.input_estado = QtWidgets.QLineEdit(self.tab_correios)
        self.input_estado.setGeometry(QtCore.QRect(360, 230, 71, 38))
        self.input_estado.setStyleSheet("QLineEdit {\n"
"    background-color:\"#FAFAFA\";\n"
"    border-radius:8px;\n"
"    border:1px solid;\n"
"    border-color: rgb(239, 239, 239);\n"
"    color:\"#444\";\n"
"    font: 10.5pt \"Quicksand\";\n"
"    padding-left:10px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border:2px solid \"#E3E3E3\"\n"
"}\n"
"")
        self.input_estado.setObjectName("input_estado")
        self.label_estado = QtWidgets.QLabel(self.tab_correios)
        self.label_estado.setGeometry(QtCore.QRect(362, 208, 61, 21))
        self.label_estado.setStyleSheet("font: 57 10.5pt \"Roboto\";\n"
"color:\"#333333\";\n"
"background: transparent;")
        self.label_estado.setObjectName("label_estado")
        self.label = QtWidgets.QLabel(self.tab_correios)
        self.label.setGeometry(QtCore.QRect(30, 180, 431, 301))
        self.label.setStyleSheet("\n"
"border:3px solid #f5f5f5;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab_correios)
        self.pushButton.setGeometry(QtCore.QRect(370, 500, 91, 30))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color:\"#3AB44E\";\n"
"    border-radius: 5px;\n"
"    color:\"white\";\n"
"    font: 75 11pt \"Roboto Medium\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:\"#62CC74\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:\"#34A045\"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.btn_buscar_cep = QtWidgets.QPushButton(self.tab_correios)
        self.btn_buscar_cep.setGeometry(QtCore.QRect(381, 114, 75, 30))
        self.btn_buscar_cep.setStyleSheet("QPushButton {\n"
"    background-color:\"#F1f1f1\";\n"
"    border-radius: 5px;\n"
"    color:\"#666\";\n"
"    font: 75 11pt \"Roboto Medium\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:\"#E7E7E7\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:\"#D2D2D2\"\n"
"}")
        self.btn_buscar_cep.setObjectName("btn_buscar_cep")
        self.label.raise_()
        self.Titulo_Cep.raise_()
        self.input_cep.raise_()
        self.label_cep.raise_()
        self.input_cidade.raise_()
        self.label_cidade.raise_()
        self.label_logradouro.raise_()
        self.input_logradouro.raise_()
        self.label_bairro.raise_()
        self.input_bairro.raise_()
        self.input_estado.raise_()
        self.label_estado.raise_()
        self.pushButton.raise_()
        self.btn_buscar_cep.raise_()
        self.tabWidget.addTab(self.tab_correios, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Relatório Empresarial"))
        self.Titulo.setText(_translate("MainWindow", "RELATÓRIO DE ATENDIMENTO"))
        self.label_nome_2.setText(_translate("MainWindow", "Nome:"))
        self.label_email.setText(_translate("MainWindow", "E-mail:"))
        self.label_ddd.setText(_translate("MainWindow", "DDD:"))
        self.label_telefone.setText(_translate("MainWindow", "Telefone:"))
        self.label_relatorio.setText(_translate("MainWindow", "Relatório:"))
        self.textbox_caso.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Quicksand\'; font-size:10.5pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btn_salvar.setText(_translate("MainWindow", "&Salvar"))
        self.btn_exportar.setText(_translate("MainWindow", "&Exportar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_relatorio), _translate("MainWindow", "Relatório"))
        self.Titulo_Cep.setText(_translate("MainWindow", "Busca de cep"))
        self.label_cep.setText(_translate("MainWindow", "CEP:"))
        self.label_cidade.setText(_translate("MainWindow", "Cidade:"))
        self.label_logradouro.setText(_translate("MainWindow", "Logradouro:"))
        self.label_bairro.setText(_translate("MainWindow", "Bairro:"))
        self.label_estado.setText(_translate("MainWindow", "Estado:"))
        self.pushButton.setText(_translate("MainWindow", "Copiar"))
        self.btn_buscar_cep.setText(_translate("MainWindow", "Buscar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_correios), _translate("MainWindow", "Correios"))


        # Gravando dados no banco
        def gravar_dados():
            try:
                nome = self.input_nome.text()
                email = self.input_email.text()
                ddd = self.input_ddd.text()


                telefone = self.input_telefone.text()
                caso = self.textbox_caso.toPlainText()
                data_atual = date.today()
                banco = sqlite3.connect('relatorios.db')
                cursor = banco.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS dados (nome text, email text, ddd integer, telefone integer, caso text,  data integer)")

                
                # Verificando Campos
                if nome == '':
                   ShowPopup("Infomação","Campo nome Vazio")

                elif caso == '':
                   ShowPopup("Informação","Campo Relatório Vazio")

                else:
                        cursor.execute("INSERT INTO dados (nome, email, ddd, telefone, caso, data) VALUES (?,?,?,?,?,?)", (nome , email, ddd, telefone, caso, data_atual))
                        cursor.close()
                        banco.commit()
                        
                        #Limpando Campos
                        self.input_nome.setText('')
                        self.input_email.setText('')
                        self.input_ddd.setText('')
                        self.input_telefone.setText('')
                        self.textbox_caso.setText('')

                        ShowPopup("Infomação","Dados gravados com sucesso!")

            except:

                ShowPopup("Alerta","Não foi possível gravar dados")

        
        def buscarcep(cep):
        
                try:
        
                   cep = self.input_cep.text()
                   address = get_address_from_cep(cep, webservice=WebService.CORREIOS)
                   print(address)
                   

                except exceptions.InvalidCEP as eic:
                   print(eic)

                except exceptions.InvalidCEP as eic:
                   print(eic)

                except exceptions.CEPNotFound as ecnf:
                   print(ecnf)

                except exceptions.ConnectionError as errc:
                   print(errc)

                except exceptions.Timeout as errt:
                   print(errt)

                except exceptions.HTTPError as errh:
                   print(errh)

                except exceptions.BaseException as e:
                   print(e)
        

        # Action buttons
        self.btn_exportar.clicked.connect(self.openWindow)
        self.btn_salvar.clicked.connect(gravar_dados)
        self.btn_buscar_cep.clicked.connect(buscarcep)


if __name__ == "__main__":
   import sys
   app = QtWidgets.QApplication(sys.argv)
   Principal = QtWidgets.QMainWindow()
   ui = Ui_MainWindow()
   ui.setupUi(Principal)
   Principal.show()
   sys.exit(app.exec_())
