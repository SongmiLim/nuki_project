# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comment_ui.ui'
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
        MainWindow.resize(461, 382)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 260, 63, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 260, 61, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 260, 81, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(380, 260, 81, 20))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 280, 441, 30))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.projectEdit = QLineEdit(self.layoutWidget)
        self.projectEdit.setObjectName(u"projectEdit")

        self.horizontalLayout.addWidget(self.projectEdit)

        self.assetEdit = QLineEdit(self.layoutWidget)
        self.assetEdit.setObjectName(u"assetEdit")

        self.horizontalLayout.addWidget(self.assetEdit)

        self.assetTypeEdit = QLineEdit(self.layoutWidget)
        self.assetTypeEdit.setObjectName(u"assetTypeEdit")

        self.horizontalLayout.addWidget(self.assetTypeEdit)

        self.newNameEdit = QLineEdit(self.layoutWidget)
        self.newNameEdit.setObjectName(u"newNameEdit")

        self.horizontalLayout.addWidget(self.newNameEdit)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(40, 330, 381, 33))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.addButton = QPushButton(self.layoutWidget1)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_2.addWidget(self.addButton)

        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(70, 70, 321, 161))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"type", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"status", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"project", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"asset", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"\ub4f1\ub85d", None))
    # retranslateUi

