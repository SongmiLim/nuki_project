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
        MainWindow.resize(419, 311)
        palette = QPalette()
        brush = QBrush(QColor(53, 53, 53, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(85, 87, 83, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        brush2 = QBrush(QColor(146, 148, 149, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ID_lineedit = QLineEdit(self.centralwidget)
        self.ID_lineedit.setObjectName(u"ID_lineedit")
        self.ID_lineedit.setGeometry(QRect(50, 70, 301, 41))
        palette1 = QPalette()
        brush3 = QBrush(QColor(238, 238, 236, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush4 = QBrush(QColor(237, 141, 32, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Highlight, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Link, brush4)
        brush5 = QBrush(QColor(238, 238, 236, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Highlight, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Link, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        brush6 = QBrush(QColor(190, 190, 190, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Highlight, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Link, brush4)
        brush7 = QBrush(QColor(0, 0, 0, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.ID_lineedit.setPalette(palette1)
        font1 = QFont()
        font1.setPointSize(11)
        self.ID_lineedit.setFont(font1)
        self.pw_lineedit = QLineEdit(self.centralwidget)
        self.pw_lineedit.setObjectName(u"pw_lineedit")
        self.pw_lineedit.setGeometry(QRect(50, 120, 301, 41))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Highlight, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Highlight, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Highlight, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.pw_lineedit.setPalette(palette2)
        self.pw_lineedit.setFont(font1)
        self.sign_in_label = QLabel(self.centralwidget)
        self.sign_in_label.setObjectName(u"sign_in_label")
        self.sign_in_label.setGeometry(QRect(130, 30, 161, 31))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        brush8 = QBrush(QColor(255, 255, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush8)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush8)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.sign_in_label.setPalette(palette3)
        font2 = QFont()
        font2.setFamily(u"Noto Sans CJK JP")
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.sign_in_label.setFont(font2)
        self.signin_btn = QPushButton(self.centralwidget)
        self.signin_btn.setObjectName(u"signin_btn")
        self.signin_btn.setGeometry(QRect(50, 240, 301, 41))
        palette4 = QPalette()
        brush10 = QBrush(QColor(191, 114, 27, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush8)
        brush11 = QBrush(QColor(252, 175, 62, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush11)
        brush12 = QBrush(QColor(48, 140, 198, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Highlight, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush8)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette4.setBrush(QPalette.Inactive, QPalette.Highlight, brush12)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush10)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        brush13 = QBrush(QColor(145, 145, 145, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush7)
#endif
        self.signin_btn.setPalette(palette4)
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(False)
        font3.setWeight(50)
        self.signin_btn.setFont(font3)
        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(50, 160, 311, 20))
        palette5 = QPalette()
        brush14 = QBrush(QColor(237, 90, 32, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush14)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        self.error_label.setPalette(palette5)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(50, 200, 301, 39))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.remember_checkbox = QCheckBox(self.layoutWidget)
        self.remember_checkbox.setObjectName(u"remember_checkbox")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush3)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        brush15 = QBrush(QColor(46, 52, 54, 128))
        brush15.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush15)
#endif
        self.remember_checkbox.setPalette(palette6)
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setWeight(50)
        self.remember_checkbox.setFont(font4)

        self.horizontalLayout.addWidget(self.remember_checkbox)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ID_lineedit.setText("")
        self.pw_lineedit.setText("")
        self.sign_in_label.setText(QCoreApplication.translate("MainWindow", u"KITSU SIGN IN", None))
        self.signin_btn.setText(QCoreApplication.translate("MainWindow", u"SIGN IN", None))
        self.error_label.setText(QCoreApplication.translate("MainWindow", u"Error message Error message Error msg", None))
        self.remember_checkbox.setText(QCoreApplication.translate("MainWindow", u"Remember Me", None))
    # retranslateUi

