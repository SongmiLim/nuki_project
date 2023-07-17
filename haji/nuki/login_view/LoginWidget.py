# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginwidget.ui'
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
        MainWindow.resize(373, 290)
        palette = QPalette()
        brush = QBrush(QColor(85, 87, 83, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 70, 271, 41))
        self.lineEdit.setPlaceholderText('ID')
        palette1 = QPalette()
        brush1 = QBrush(QColor(211, 215, 207, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        self.lineEdit.setPalette(palette1)
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 120, 271, 41))
        self.lineEdit_2.setPlaceholderText('Password')
        self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        self.lineEdit_2.setPalette(palette2)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 40, 121, 20))
        palette3 = QPalette()
        brush2 = QBrush(QColor(238, 238, 236, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush3)
        brush4 = QBrush(QColor(255, 255, 255, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        brush5 = QBrush(QColor(190, 190, 190, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        brush6 = QBrush(QColor(0, 0, 0, 128))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.label.setPalette(palette3)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(200, 170, 131, 20))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        self.label_2.setPalette(palette4)
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 200, 111, 41))
        palette5 = QPalette()
        brush7 = QBrush(QColor(252, 175, 62, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush7)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        self.pushButton.setPalette(palette5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"KITSU Login", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Forgot Password?", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

