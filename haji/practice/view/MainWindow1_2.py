# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow1_2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(826, 520)
        palette = QPalette()
        brush = QBrush(QColor(201, 216, 229, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(149, 179, 202, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 781, 421))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_projectname = QLabel(self.widget)
        self.label_projectname.setObjectName(u"label_projectname")

        self.horizontalLayout.addWidget(self.label_projectname)

        self.searchEdit = QLineEdit(self.widget)
        self.searchEdit.setObjectName(u"searchEdit")
        self.searchEdit.setPlaceholderText('What project are you looking for?..')

        self.horizontalLayout.addWidget(self.searchEdit)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_project = QLabel(self.widget)
        self.label_project.setObjectName(u"label_project")

        self.horizontalLayout_2.addWidget(self.label_project)

        self.projectEdit = QLineEdit(self.widget)
        self.projectEdit.setObjectName(u"projectEdit")

        self.horizontalLayout_2.addWidget(self.projectEdit)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_name = QLabel(self.widget)
        self.label_name.setObjectName(u"label_name")

        self.horizontalLayout_3.addWidget(self.label_name)

        self.nameEdit = QLineEdit(self.widget)
        self.nameEdit.setObjectName(u"nameEdit")

        self.horizontalLayout_3.addWidget(self.nameEdit)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_description = QLabel(self.widget)
        self.label_description.setObjectName(u"label_description")

        self.horizontalLayout_6.addWidget(self.label_description)

        self.descriptionEdit = QLineEdit(self.widget)
        self.descriptionEdit.setObjectName(u"descriptionEdit")

        self.horizontalLayout_6.addWidget(self.descriptionEdit)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 1, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.loadbtn = QPushButton(self.widget)
        self.loadbtn.setObjectName(u"loadbtn")
        palette1 = QPalette()
        brush2 = QBrush(QColor(80, 115, 148, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        brush3 = QBrush(QColor(247, 247, 247, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        brush4 = QBrush(QColor(190, 190, 190, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.loadbtn.setPalette(palette1)
        font = QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.loadbtn.setFont(font)

        self.horizontalLayout_7.addWidget(self.loadbtn)

        self.editbtn = QPushButton(self.widget)
        self.editbtn.setObjectName(u"editbtn")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.editbtn.setPalette(palette2)
        self.editbtn.setFont(font)

        self.horizontalLayout_7.addWidget(self.editbtn)

        self.deletebtn = QPushButton(self.widget)
        self.deletebtn.setObjectName(u"deletebtn")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.deletebtn.setPalette(palette3)
        self.deletebtn.setFont(font)

        self.horizontalLayout_7.addWidget(self.deletebtn)

        self.clearbtn = QPushButton(self.widget)
        self.clearbtn.setObjectName(u"clearbtn")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        self.clearbtn.setPalette(palette4)
        self.clearbtn.setFont(font)

        self.horizontalLayout_7.addWidget(self.clearbtn)


        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 2)

        self.tableView = QTableView(self.widget)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 826, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_projectname.setText(QCoreApplication.translate("MainWindow", u"PROJECT NAME : ", None))
        self.label_project.setText(QCoreApplication.translate("MainWindow", u"Project :", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name : ", None))
        self.label_description.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.loadbtn.setText(QCoreApplication.translate("MainWindow", u"LOAD", None))
        self.editbtn.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
        self.deletebtn.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.clearbtn.setText(QCoreApplication.translate("MainWindow", u"CLEAR", None))
    # retranslateUi

