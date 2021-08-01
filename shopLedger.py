# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb
import pymysql
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QVBoxLayout, QMainWindow, QPushButton, QMessageBox ,QHBoxLayout, QRadioButton, QAbstractItemView, QTableWidgetItem
import datetime
import sys
import os
import copy


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color:rgb(163, 203, 230)")
        MainWindow.setWindowIcon(QtGui.QIcon('C:/Users/Prince-Dev/Desktop/shop/shopicon.png'))
        self.screenShape = QtWidgets.QDesktopWidget().screenGeometry()
        MainWindow.resize(self.screenShape.width(), self.screenShape.height())

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_tab_widget = QtWidgets.QTabWidget(self.centralwidget)
        self.main_tab_widget.setGeometry(QtCore.QRect(9, 39, 1501, 771))
        self.main_tab_widget.setMouseTracking(False)
        self.main_tab_widget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.main_tab_widget.setAutoFillBackground(False)
        self.main_tab_widget.setMinimumSize(500,500)
        self.main_tab_widget.setStyleSheet("background-color:rgb(184, 197, 207)")
        self.main_tab_widget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.main_tab_widget.setTabsClosable(False)
        self.main_tab_widget.setMovable(False)
        self.main_tab_widget.setObjectName("main_tab_widget")

        # self.con =  mdb.connect('remotemysql.com','4VKTDZ2lGH','2ulQoNpik0','4VKTDZ2lGH')
        # self.cur =  self.con.cursor()

        self.local_con = mdb.connect('localhost','root','PrinceGoyal49','shopledger')
        self.local_con_cur = self.local_con.cursor()

        self.selected_agency = None

        self.ledger_tab_widget = QtWidgets.QWidget()
        self.ledger_tab_widget.setObjectName("ledger_tab_widget")

        self.tableWidget_2 = QtWidgets.QTableWidget(self.ledger_tab_widget)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 70, 1141, 550))
        self.tableWidget_2.setMinimumSize(QtCore.QSize(500, 0))
        self.tableWidget_2.setStyleSheet("color:black;background-color:white;")
        self.tableWidget_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tableWidget_2.setDragEnabled(False)
        # self.tableWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        # self.tableWidget_2.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.tableWidget_2.setAlternatingRowColors(True)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_2.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)

        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(20)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.label_search = QtWidgets.QLabel(self.ledger_tab_widget)
        self.label_search.setGeometry(QtCore.QRect(20, 30, 181, 31))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)

        self.label_search.setFont(font)
        self.label_search.setStyleSheet("background-color:white;")
        self.label_search.setFrameShape(QtWidgets.QFrame.Box)
        self.label_search.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_search.setObjectName("label_search")

        self.label_selected_agency = QLabel(self.ledger_tab_widget)
        self.label_selected_agency.setGeometry(QtCore.QRect(150, 5, 881, 21))

        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)

        self.label_selected_agency.setFont(font)
        self.label_selected_agency.setStyleSheet("background-color:white;")
        self.label_selected_agency.setFrameShape(QtWidgets.QFrame.Box)
        self.label_selected_agency.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_selected_agency.setObjectName("label_selected_agency")

        self.Line_edit_search = QtWidgets.QLineEdit(self.ledger_tab_widget)
        self.Line_edit_search.setGeometry(QtCore.QRect(220, 30, 811, 31))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)

        self.Line_edit_search.setFont(font)
        self.Line_edit_search.setStyleSheet("background-color:white;")
        self.Line_edit_search.setText("")
        self.Line_edit_search.setObjectName("Line_edit_search")
        self.list_of_agencies = []
        self.fetch_agency_names()
        self.set_completer()

        self.listWidget_2 = QtWidgets.QListWidget(self.ledger_tab_widget)
        self.listWidget_2.setGeometry(QtCore.QRect(1170, 70, 311, 401))

        font = QtGui.QFont()
        font.setPointSize(12)

        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("background-color:white;")
        self.listWidget_2.setObjectName("listWidget_2")

        item = QtWidgets.QListWidgetItem()
        self.label_2 = QtWidgets.QLabel(self.ledger_tab_widget)
        self.label_2.setGeometry(QtCore.QRect(1230, 40, 181, 21))

        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:white;")
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.ledger_tab_widget)
        self.pushButton.setGeometry(QtCore.QRect(1060, 30, 101, 31))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color:red;background-color:white;")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.ledger_tab_widget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 680, 131, 51))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color:white;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.ledger_tab_widget)
        self.pushButton_3.setGeometry(QtCore.QRect(300, 680, 131, 51))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color:white;")
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_5 = QtWidgets.QPushButton(self.ledger_tab_widget)
        self.pushButton_5.setGeometry(QtCore.QRect(850, 680, 131, 51))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color:white;")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_4 = QtWidgets.QPushButton(self.ledger_tab_widget)
        self.pushButton_4.setGeometry(QtCore.QRect(1020, 680, 131, 51))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("background-color:white;")
        self.pushButton_4.setObjectName("pushButton_4")

        self.calendarWidget = QtWidgets.QCalendarWidget(self.ledger_tab_widget)
        self.calendarWidget.setGeometry(QtCore.QRect(1170, 480, 312, 191))
        self.calendarWidget.setStyleSheet("background-color:LIGHTBLUE;")
        self.calendarWidget.setObjectName("calendarWidget")

        self.main_tab_widget.addTab(self.ledger_tab_widget, "")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(620, -10, 291, 41))

        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(620, 30, 281, 20))
        self.label_3.setObjectName("label_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1532, 21))
        self.menubar.setObjectName("menubar")

        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")

        self.menuView_2 = QtWidgets.QMenu(self.menubar)
        self.menuView_2.setObjectName("menuView_2")

        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")

        self.menuSave_as = QtWidgets.QMenu(self.menuFile)
        self.menuSave_as.setObjectName("menuSave_as")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")

        self.actionPrint_Preview = QtWidgets.QAction(MainWindow)
        self.actionPrint_Preview.setObjectName("actionPrint_Preview")

        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")

        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")

        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")

        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")

        self.actionPrint_Preview_2 = QtWidgets.QAction(MainWindow)
        self.actionPrint_Preview_2.setObjectName("actionPrint_Preview_2")

        self.actionPrint_2 = QtWidgets.QAction(MainWindow)
        self.actionPrint_2.setObjectName("actionPrint_2")

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")

        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")

        self.actionClose_2 = QtWidgets.QAction(MainWindow)
        self.actionClose_2.setObjectName("actionClose_2")

        self.actionPDF = QtWidgets.QAction(MainWindow)
        self.actionPDF.setObjectName("actionPDF")

        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")

        self.actionFull_Screen = QtWidgets.QAction(MainWindow)
        self.actionFull_Screen.setObjectName("actionFull_Screen")

        self.actionFont = QtWidgets.QAction(MainWindow)
        self.actionFont.setObjectName("actionFont")

        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.actionShortcut_commands = QtWidgets.QAction(MainWindow)
        self.actionShortcut_commands.setObjectName("actionShortcut_commands")

        self.menuView.addAction(self.actionCut)
        self.menuView.addAction(self.actionCopy)
        self.menuView.addAction(self.actionPaste)
        self.menuView.addAction(self.actionFont)

        self.menuView_2.addAction(self.actionFull_Screen)

        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionShortcut_commands)

        self.menuSave_as.addAction(self.actionPDF)

        self.menuFile.addAction(self.actionPrint_Preview_2)
        self.menuFile.addAction(self.actionPrint_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.menuSave_as.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_2)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuView_2.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.main_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def date_updater(self):
        now = datetime.datetime.now()
        self.date = now.strftime("%Y-%m-%d  %A %I:%M:%S")
        self.label_date_value = QLabel('Date & Day : ' + self.date)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "LEDGER"))

        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DATE & DAY"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "BILL NO./ SLIP NO."))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DEBITED"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CREDITED"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "BALANCE"))

        self.label_search.setText(_translate("MainWindow", "Search by AGENCY Name"))

        self.label_selected_agency.setText(_translate("MainWindow", "Selected agency : "))

        __sortingEnabled = self.listWidget_2.isSortingEnabled()

        self.listWidget_2.setSortingEnabled(False)

        self.list_widget_update()

        self.listWidget_2.setSortingEnabled(__sortingEnabled)

        self.label_2.setText(_translate("MainWindow", "LIST OF AGENCIES"))

        self.pushButton.setText(_translate("MainWindow", "Proceed"))
        self.pushButton.clicked.connect(self.search_ledger)

        self.pushButton_2.setText(_translate("MainWindow", "Add New Agency"))
        self.pushButton_2.clicked.connect(self.add_agency)

        self.pushButton_3.setText(_translate("MainWindow", "Add Record"))

        self.pushButton_3.clicked.connect(self.add_record)

        self.pushButton_4.setText(_translate("MainWindow", "Delete Agency"))
        self.pushButton_4.clicked.connect(self.delete_agency)

        self.pushButton_5.setText(_translate("MainWindow", "Delete Record"))
        self.pushButton_5.clicked.connect(self.delete_record)

        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.ledger_tab_widget), _translate("MainWindow", "Ledger"))

        self.label.setText(_translate("MainWindow", "K.L. TRADERS"))

        self.label_3.setText(_translate("MainWindow", "GSTIN : "))

        self.menuView.setTitle(_translate("MainWindow", "Edit"))

        self.menuView_2.setTitle(_translate("MainWindow", "View"))

        self.menuHelp.setTitle(_translate("MainWindow", "Help"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))

        self.menuSave_as.setTitle(_translate("MainWindow", "Save as"))

        self.actionOpen.setText(_translate("MainWindow", "Recent"))

        self.actionPrint_Preview.setText(_translate("MainWindow", "Print Preview"))

        self.actionPrint.setText(_translate("MainWindow", "Print"))

        self.actionClose.setText(_translate("MainWindow", "Close"))

        self.actionCopy.setText(_translate("MainWindow", "Copy"))

        self.actionPaste.setText(_translate("MainWindow", "Paste"))

        self.actionPrint_Preview_2.setText(_translate("MainWindow", "Print Preview"))

        self.actionPrint_2.setText(_translate("MainWindow", "Print"))

        self.actionSave.setText(_translate("MainWindow", "Save"))

        self.actionclose.setText(_translate("MainWindow", "close"))

        self.actionClose_2.setText(_translate("MainWindow", "Close"))

        self.actionPDF.setText(_translate("MainWindow", "PDF"))

        self.actionCut.setText(_translate("MainWindow", "Cut"))

        self.actionFull_Screen.setText(_translate("MainWindow", "Full Screen Mode"))

        self.actionFont.setText(_translate("MainWindow", "Font"))

        self.actionAbout.setText(_translate("MainWindow", "About"))

        self.actionShortcut_commands.setText(_translate("MainWindow", "Shortcut commands"))

    def list_widget_update(self):
        _translate = QtCore.QCoreApplication.translate
        self.short_name_list_agencies = []

        try:
            self.local_con_cur.execute('Select agency_name from agency_detail_list;')
        except Exception:
            return

        agency_name_list = self.local_con_cur.fetchall()

        for tuple in agency_name_list:
            for agency in tuple:
                if agency != '':
                    self.short_name_list_agencies.append(agency)
        self.short_name_list_agencies.sort()
        n = 0


        #
        # while n<500:
        #     try:
        #         item = self.listWidget_2.item(n)
        #         self.listWidget_2.takeItem(self.listWidget_2.row(item))
        #         n += 1
        #     except Exception:
        #         break
        self.listWidget_2.clear()

        # del self.listWidget_2

        # self.listWidget_2 = QtWidgets.QListWidget(self.ledger_tab_widget)
        # self.listWidget_2.setGeometry(QtCore.QRect(1170, 70, 311, 401))
        #
        # font = QtGui.QFont()
        # font.setPointSize(12)
        #
        # self.listWidget_2.setFont(font)
        # self.listWidget_2.setStyleSheet("background-color:white;")
        # self.listWidget_2.setObjectName("listWidget_2")

        for agency in self.short_name_list_agencies:
            item = QtWidgets.QListWidgetItem()
            item.setText(_translate('MainWindow', agency))
            self.listWidget_2.addItem(item)
            self.listWidget_2.update()

        # if action == 'deleted':
        #     for agency in self.short_name_list_agencies:
        #         if self.listWidget_2.item(self.j).text() != agency:
        #             self.cur.execute('Drop table %s_ledger' % (agency))
        #             self.cur.execute('Delete from agency_detail_list where short_name = "%s";' % (agency))
        #
        #             self.local_con_cur.execute('Drop table %s_ledger' % (agency))
        #             self.local_con_cur.execute('Delete from agency_detail_list where short_name = "%s";' % (agency))
        # if action == 'added':
        #     for agency in self.short_name_list_agencies:
        #         if self.listWidget_2.item(self.j).text() != agency:
        #             item.setText(_translate('MainWindow', agency))
        #             self.listWidget_2.addItem(item)
        #             self.j += 1
        #             continue
        #
        #         item = self.listWidget_2.item(self.j)
        #         item.setText(_translate('MainWindow', agency))
        #         self.j += 1
        self.listWidget_2.itemClicked.connect(self.list_item_clicked)

    def list_item_clicked(self, item):
        self.Line_edit_search.setText(''.join(item.text()))
        self.label_selected_agency.setText(''.join(item.text()))
        self.pushButton.click()

    def search_ledger(self):
        self.select_agency()
        self.label_selected_agency.setText('Selected agency : ')
        self.label_selected_agency.setText(self.label_selected_agency.text()+'  '+self.selected_agency)
        try:
            self.local_con_cur.execute('Select short_name from agency_detail_list where agency_name = "%s";' % (self.selected_agency))

            short_name_selected_agency = self.local_con_cur.fetchall()

            if not short_name_selected_agency:
                self.label_selected_agency.setText("Selected agency : INVALID NAME")
                self.selected_agency = None
                self.tableWidget_2.setRowCount(0)
                raise Exception()
        except Exception:
            return

        # short_name_selected_agency = self.cur.fetchall()
        for tuple in short_name_selected_agency:
            for agency in tuple:
                self.selected_agency_short_name = agency

        try:
            self.local_con_cur.execute('select * from %s_ledger' % (self.selected_agency_short_name))
        except Exception:

            return


        full_ledger = self.local_con_cur.fetchall()
        i = 0
        self.tableWidget_2.setRowCount(0)
        for tuple in full_ledger:
            row_count = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_count)
            self.tableWidget_2.setItem(i,0,QTableWidgetItem(tuple[0]))
            self.tableWidget_2.setItem(i,1,QTableWidgetItem(str(tuple[1])))
            self.tableWidget_2.setItem(i,2,QTableWidgetItem(str(tuple[2])))
            self.tableWidget_2.setItem(i,3,QTableWidgetItem(str(tuple[3])))
            self.tableWidget_2.setItem(i,4,QTableWidgetItem(str(tuple[4])))
            i += 1

        self.balance = tuple[4]

    def btn_refresh_handler(self):
        self.search_ledger()
        self.fetch_agency_names()
        self.set_completer()

    def fetch_agency_names(self):
        try:
            self.local_con_cur.execute('Select agency_name from agency_detail_list;')
            self.local_con_cur.execute('Select agency_name from agency_detail_list;')
        except Exception:
            return

        agency_list = self.local_con_cur.fetchall()

        self.list_of_agencies = []
        for tuple in agency_list:
            for agency in tuple:
                self.list_of_agencies.append(agency)

    def set_completer(self):
        self.completer = QtWidgets.QCompleter(self.list_of_agencies)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.Line_edit_search.setCompleter(self.completer)

    def select_agency(self):
        self.selected_agency = ''.join(self.Line_edit_search.text())

    def add_record(self):
        self.date_updater()
        self.add_record_dialog = QDialog(self)
        self.add_record_dialog.show()
        self.add_record_dialog.setWindowTitle("Add Record")
        self.add_record_dialog.setGeometry(200,200,300,100)
        self.add_record_dialog.setWindowIcon(QtGui.QIcon('C:/Users/Prince-Dev/Desktop/shop/shopicon.png'))

        if self.selected_agency == None:
            QMessageBox.about(self,'Error', 'Please Select An Agency first')
            self.add_record_dialog.close()

        vbox = QVBoxLayout(self)

        hbox = QHBoxLayout()

        hbox.addWidget(self.label_date_value)
        new_label_selected_agency = QLabel(self.label_selected_agency.text())
        vbox.addWidget(new_label_selected_agency)
        vbox.addLayout(hbox)

        hbox_radio = QHBoxLayout()

        self.label_action = QLabel("Action :")

        self.radio_btn_debited = QRadioButton("Debit")
        self.radio_btn_debited.toggled.connect(self.radio_btn_toggled)
        self.radio_btn_credited = QRadioButton('Credit')
        self.radio_btn_credited.toggled.connect(self.radio_btn_toggled)

        hbox_radio.addWidget(self.label_action)
        hbox_radio.addWidget(self.radio_btn_debited)
        hbox_radio.addWidget(self.radio_btn_credited)

        vbox.addLayout(hbox_radio)

        hbox_slip = QHBoxLayout()
        self.line_edit_slip_no = QLineEdit()
        self.line_edit_slip_no.setPlaceholderText("Enter Slip No.")
        self.line_edit_slip_no.setDisabled(True)

        self.line_edit_bill_no = QLineEdit()
        self.line_edit_bill_no.setPlaceholderText("Enter Bill No.")
        self.line_edit_bill_no.setDisabled(True)

        hbox_slip.addWidget(self.line_edit_bill_no)
        hbox_slip.addWidget(self.line_edit_slip_no)

        vbox.addLayout(hbox_slip)

        hbox_amount = QHBoxLayout()

        self.line_edit_debit_amount = QLineEdit()
        self.line_edit_debit_amount.setPlaceholderText("Enter Debit Amount")
        self.line_edit_debit_amount.setDisabled(True)

        hbox_amount.addWidget(self.line_edit_debit_amount)

        self.line_edit_credit_amount = QLineEdit()
        self.line_edit_credit_amount.setPlaceholderText("Enter Credit Amount")
        self.line_edit_credit_amount.setDisabled(True)

        hbox_amount.addWidget(self.line_edit_credit_amount)

        vbox.addLayout(hbox_amount)

        self.btn_add_record_to_db = QPushButton("Add")

        vbox.addWidget(self.btn_add_record_to_db)

        self.add_record_dialog.setLayout(vbox)

    def radio_btn_toggled(self):
        self.line_edit_slip_no.setDisabled(True)
        self.line_edit_bill_no.setDisabled(True)
        self.line_edit_debit_amount.setDisabled(True)
        self.line_edit_credit_amount.setDisabled(True)

        if self.radio_btn_debited.isChecked():
            self.btn_add_record_to_db.setText('Debit')
            self.line_edit_debit_amount.setDisabled(False)
            self.line_edit_bill_no.setDisabled(False)

        if self.radio_btn_credited.isChecked():
            self.btn_add_record_to_db.setText('Credit')
            self.line_edit_credit_amount.setDisabled(False)
            self.line_edit_slip_no.setDisabled(False)

        self.btn_add_record_to_db.clicked.connect(self.add_record_to_db)

    def add_record_to_db(self):

        self.date_updater()
        if self.btn_add_record_to_db.text() == 'Debit':
            if self.line_edit_bill_no.text() == '' or int(self.line_edit_debit_amount.text()) == '':
                QMessageBox.about(self,'Data Error', 'Please Enter the Required Information')
                return
            self.balance = self.balance + int(self.line_edit_debit_amount.text())
            try:
                self.local_con_cur.execute('Insert into %s_ledger'
                            ' values("%s", "%s", %d, %d, %d)' % (self.selected_agency_short_name, self.date, self.line_edit_bill_no.text(), int(self.line_edit_debit_amount.text()), 0 , self.balance))

            except Exception:
                return


            self.local_con.commit()

            QMessageBox.about(self,'Added Successfully', 'Record Added Successfully (Bill No. no : %s , Amount: %d, Balance: %d)'%( self.line_edit_bill_no.text(),int(self.line_edit_debit_amount.text()), self.balance))
            self.add_record_dialog.close()

        elif self.btn_add_record_to_db.text() == 'Credit':
            if self.line_edit_slip_no.text() == '' or int(self.line_edit_credit_amount.text()) == '':
                QMessageBox.about(self,'Data Error', 'Please Enter the Required Information')
                return

            self.balance = self.balance - int(self.line_edit_credit_amount.text())
            try:
                self.local_con_cur.execute('Insert into %s_ledger'
                            ' values("%s","%s", %d, %d, %d)' % (self.selected_agency_short_name, self.date, self.line_edit_slip_no.text(), 0, int(self.line_edit_credit_amount.text()) , self.balance))

            except Exception:
                return


            self.local_con.commit()

            QMessageBox.about(self,'Added Successfully', 'Record Added Successfully (slip no : %s , Amount: %d, Balance: %d)'%( self.line_edit_slip_no.text(),int(self.line_edit_credit_amount.text()), self.balance))
            self.add_record_dialog.close()
        self.btn_add_record_to_db.setText('')
        self.search_ledger()

    def delete_agency(self):
        if self.selected_agency == None:
            QMessageBox.about(self,'Error', 'Please Select An Agency first')
            return
        buttonReply = QMessageBox.question(self, 'Confirm Delete', "Are You Sure You Want to delete %s_ledger?" % (self.selected_agency_short_name), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            try:
                self.local_con_cur.execute('Drop table %s_ledger' % (self.selected_agency_short_name))
                self.local_con_cur.execute('Delete from agency_detail_list where short_name = "%s";' % (self.selected_agency_short_name))
                result = True

            except Exception:
                result = False
                return



            self.local_con.commit()
            self.search_ledger()
            self.list_widget_update()
        else:
            return

    def delete_record(self):
        if self.selected_agency == None:
            QMessageBox.about(self,'Error', 'Please Select An Agency first')
            return
        self.add_delete_record_dialog = QDialog(self)
        self.add_delete_record_dialog.show()
        self.add_delete_record_dialog.setWindowTitle("Delete Record")
        self.add_delete_record_dialog.setGeometry(200,200, 600,200)
        self.add_delete_record_dialog.setWindowIcon(QtGui.QIcon('C:/Users/Prince-Dev/Desktop/shop/shopicon.png'))

        hbox = QHBoxLayout()
        vbox = QVBoxLayout(self)

        self.label_date = QLabel("Select Date")
        self.line_edit_date = QLineEdit()
        self.line_edit_date.setPlaceholderText("YYYY-MM-DD")
        self.delete_rcd_set_completer()

        hbox.addWidget(self.label_date)
        hbox.addWidget(self.line_edit_date)

        vbox.addLayout(hbox)

        self.btn_delete_rcd = QPushButton("Delete")
        self.btn_delete_rcd.clicked.connect(self.delete_rcd_clicked)

        vbox.addWidget(self.btn_delete_rcd)

        self.add_delete_record_dialog.setLayout(vbox)

    def delete_rcd_set_completer(self):
        try:
            self.local_con_cur.execute('Select date_and_day from %s_ledger;' % (self.selected_agency_short_name))
        except Exception:
            return

        self.date_list = self.local_con_cur.fetchall()

        self.list_of_dates = []
        for tuple in self.date_list:
            for date in tuple:
                self.list_of_dates.append(date)


        self.completer_date = QtWidgets.QCompleter(self.list_of_dates)
        self.completer_date.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.line_edit_date.setCompleter(self.completer_date)

    def delete_rcd_clicked(self):

        buttonReply = QMessageBox.question(self, 'Confirm Delete', "Are You Sure You Want to delete %s record?" % (''.join(self.line_edit_date.text())), QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            try:
                self.local_con_cur.execute('Delete from %s_ledger where date_and_day = "%s"' % (self.selected_agency_short_name, ''.join(self.line_edit_date.text())))

            except Exception:
                return


            self.local_con.commit()
            buttonReply = QMessageBox.about(self, 'Deleted Successfully', "Successfully Deleted")
            self.add_delete_record_dialog.close()
            self.search_ledger()
        else:
            return

    def add_agency(self):
        self.add_agency_dialog = QDialog(self)
        self.add_agency_dialog.show()
        self.add_agency_dialog.setWindowTitle("Add New Agency")
        self.add_agency_dialog.setGeometry(200,200, 600,200)
        self.add_agency_dialog.setWindowIcon(QtGui.QIcon('C:/Users/Prince-Dev/Desktop/shop/shopicon.png'))
        vbox = QVBoxLayout()

        label_agency_name = QLabel("Enter the Agency Name")
        vbox.addWidget(label_agency_name)

        self.line_edit_agency_name = QLineEdit()
        self.line_edit_agency_name.setPlaceholderText("Enter the Name of Agency here")
        vbox.addWidget(self.line_edit_agency_name)

        label_agency_short_name = QLabel("Enter the Short unique Agency Name")
        vbox.addWidget(label_agency_short_name)

        self.line_edit_agency_short_name = QLineEdit()
        self.line_edit_agency_short_name.setPlaceholderText("Enter the short unique Name of Agency here")
        vbox.addWidget(self.line_edit_agency_short_name)

        label_company_name = QLabel("Enter the Company Name of Product")
        vbox.addWidget(label_company_name)

        self.line_edit_company_name = QLineEdit()
        self.line_edit_company_name.setPlaceholderText("Enter Company Name like haldiram, Bikano etc")
        vbox.addWidget(self.line_edit_company_name)

        label_dealer_name = QLabel("Enter the Dealer Name")
        vbox.addWidget(label_dealer_name)

        self.line_edit_dealer_name = QLineEdit()
        self.line_edit_dealer_name.setPlaceholderText("Enter the Name of the Dealer here")
        vbox.addWidget(self.line_edit_dealer_name)

        label_contact_number = QLabel("Enter the Dealer Contact")
        vbox.addWidget(label_contact_number)

        self.line_edit_contact_number = QLineEdit()
        self.line_edit_contact_number.setPlaceholderText("Enter the Contact No. of the Dealer here")
        vbox.addWidget(self.line_edit_contact_number)

        label_dealer_address = QLabel("Enter the Dealer Address")
        vbox.addWidget(label_dealer_address)

        self.line_edit_dealer_address = QLineEdit()
        self.line_edit_dealer_address.setPlaceholderText("Enter the Address of the Dealer here")
        vbox.addWidget(self.line_edit_dealer_address)

        label_dealer_gstin = QLabel("Enter the Dealer GST No")
        vbox.addWidget(label_dealer_gstin)

        self.line_edit_dealer_gstin = QLineEdit()
        self.line_edit_dealer_gstin.setPlaceholderText("Enter the GST No of the Dealer here")
        vbox.addWidget(self.line_edit_dealer_gstin)

        add_button = QPushButton("Add Agency")
        add_button.clicked.connect(self.add_to_db)

        vbox.addWidget(add_button)

        self.add_agency_dialog.setLayout(vbox)

    def add_to_db(self):
        self.date_updater()
        try:
            self.local_con_cur.execute('INSERT INTO agency_detail_list(Agency_Name, Short_Name, Company_Name, Dealer_Name, Contact_No, Address, GST_no)'
                      'VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s");' % (''.join(self.line_edit_agency_name.text()),
                                                                            ''.join(self.line_edit_agency_short_name.text()),
                                                                            ''.join(self.line_edit_company_name.text()),
                                                                            ''.join(self.line_edit_dealer_name.text()),
                                                                            ''.join(self.line_edit_contact_number.text()),
                                                                            ''.join(self.line_edit_dealer_address.text()),
                                                                            ''.join(self.line_edit_dealer_gstin.text())))

            self.local_con_cur.execute('Create table %s_ledger'
                        '(date_and_day varchar(50) NOT NULL ,'
                        'bill_slip_no varchar(50),'
                        'debited int(10) NOT NULL,'
                        'credited int(10) NOT null,'
                        'balance int(10) NOT null);' % (''.join(self.line_edit_agency_short_name.text())))
            self.local_con_cur.execute('Insert into %s_ledger'
                        ' values("%s", "0", 0, 0, 0)' % (''.join(self.line_edit_agency_short_name.text()), self.date)
            )
            result = True
        except Exception:
            result = False
            return




        self.local_con.commit()

        QMessageBox.about(self,'Added', "Added Agency "+str(self.line_edit_agency_name.text()))

        self.add_agency_dialog.close()
        self.list_widget_update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
