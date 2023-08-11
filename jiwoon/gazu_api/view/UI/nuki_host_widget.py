# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuki_host_widget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_host_widget(object):
    def setupUi(self, host_widget):
        if not host_widget.objectName():
            host_widget.setObjectName(u"host_widget")
        host_widget.resize(320, 130)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(host_widget.sizePolicy().hasHeightForWidth())
        host_widget.setSizePolicy(sizePolicy)
        host_widget.setMinimumSize(QSize(320, 130))
        host_widget.setMaximumSize(QSize(320, 130))
        self.host_input = QLineEdit(host_widget)
        self.host_input.setObjectName(u"host_input")
        self.host_input.setGeometry(QRect(20, 50, 281, 28))
        self.host_label = QLabel(host_widget)
        self.host_label.setObjectName(u"host_label")
        self.host_label.setGeometry(QRect(20, 20, 63, 20))
        self.host_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.connect_btn = QPushButton(host_widget)
        self.connect_btn.setObjectName(u"connect_btn")
        self.connect_btn.setGeometry(QRect(220, 90, 84, 28))
        self.error_msg = QLabel(host_widget)
        self.error_msg.setObjectName(u"error_msg")
        self.error_msg.setEnabled(True)
        self.error_msg.setGeometry(QRect(130, 30, 171, 20))
        self.error_msg.setAutoFillBackground(False)
        self.error_msg.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(host_widget)

        QMetaObject.connectSlotsByName(host_widget)
    # setupUi

    def retranslateUi(self, host_widget):
        host_widget.setWindowTitle(QCoreApplication.translate("host_widget", u"Nuki", None))
        self.host_input.setText(QCoreApplication.translate("host_widget", u"http://", None))
        self.host_input.setPlaceholderText(QCoreApplication.translate("host_widget", u"Kitsu server address", None))
        self.host_label.setText(QCoreApplication.translate("host_widget", u"Host", None))
        self.connect_btn.setText(QCoreApplication.translate("host_widget", u"Connect", None))
        self.error_msg.setText(QCoreApplication.translate("host_widget", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

