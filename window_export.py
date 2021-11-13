# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_export.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from datetime import date
from sqlite3.dbapi2 import Date
from PySide2 import QtCore, QtGui, QtWidgets
from function import consultarDados


class Ui_ExportWindow(object):
    def setupUi(self, ExportWindow):
        ExportWindow.setObjectName("ExportWindow")
        ExportWindow.resize(458, 419)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Ico/pdf.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExportWindow.setWindowIcon(icon)
        ExportWindow.setStyleSheet("border-radius: 10px;")
        self.centralwidget = QtWidgets.QWidget(ExportWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_export = QtWidgets.QFrame(self.centralwidget)
        self.frame_export.setGeometry(QtCore.QRect(0, -20, 801, 541))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(9)
        self.frame_export.setFont(font)
        self.frame_export.setStyleSheet("background:\"white\";")
        self.frame_export.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_export.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_export.setObjectName("frame_export")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame_export)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 100, 381, 265))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setMouseTracking(False)
        self.calendarWidget.setTabletTracking(False)
        self.calendarWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.calendarWidget.setAcceptDrops(False)
        self.calendarWidget.setStyleSheet("color:\"#777\";")
        self.calendarWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.frame = QtWidgets.QFrame(self.frame_export)
        self.frame.setGeometry(QtCore.QRect(0, 20, 461, 101))
        self.frame.setStyleSheet("background-color: #0081D5;\n"
"border-radius: 0px;")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.titulo_export = QtWidgets.QLabel(self.frame)
        self.titulo_export.setGeometry(QtCore.QRect(40, 24, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(27)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.titulo_export.setFont(font)
        self.titulo_export.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.titulo_export.setStyleSheet("font: 57 27.10pt \"Roboto Black\";\n"
"color: \"#fff\";\n"
"text-transform: uppercase;\n"
"background:transparent;\n"
"border:0")
        self.titulo_export.setObjectName("titulo_export")
        self.btn_relatorio = QtWidgets.QPushButton(self.frame_export)
        self.btn_relatorio.setGeometry(QtCore.QRect(240, 380, 181, 35))
        self.btn_relatorio.setStyleSheet("QPushButton {\n"
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
        self.btn_relatorio.setObjectName("btn_relatorio")
        self.label_get_data = QtWidgets.QLabel(self.frame_export)
        self.label_get_data.setGeometry(QtCore.QRect(40, 390, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Quicksand")
        font.setPointSize(15)
        self.label_get_data.setFont(font)
        self.label_get_data.setText("")
        self.label_get_data.setObjectName("label_get_data")
        self.frame.raise_()
        self.btn_relatorio.raise_()
        self.label_get_data.raise_()
        self.calendarWidget.raise_()
        ExportWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExportWindow)
        QtCore.QMetaObject.connectSlotsByName(ExportWindow)

    def retranslateUi(self, ExportWindow):
        _translate = QtCore.QCoreApplication.translate
        ExportWindow.setWindowTitle(_translate("ExportWindow", "Exportação de Relatório"))
        self.titulo_export.setText(_translate("ExportWindow", "Exportar Relatório"))
        self.btn_relatorio.setText(_translate("ExportWindow", "Exportar Relatório"))
        
        self.btn_relatorio.pressed.connect(lambda: 
                self.requisicao(
                        self.calendarWidget.selectedDate().toString("yyyy-MM-dd")))

        # value = self.calendarWidget.selectedDate()
        self.calendarWidget.clicked.connect(lambda: self.getData(
                self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
                ))

    def getData(self, date):
            print(date)
            # consultar dado
            pass
        
 
    def requisicao(self, date):
        print(date)
        consultarDados(date)
