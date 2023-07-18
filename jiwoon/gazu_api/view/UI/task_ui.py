# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'asset_view.ui'
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
        self.label.setGeometry(QRect(40, 260, 63, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 260, 61, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 260, 81, 20))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(360, 260, 81, 20))
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 10, 441, 241))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 280, 441, 30))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.projectEdit = QLineEdit(self.widget)
        self.projectEdit.setObjectName(u"projectEdit")

        self.horizontalLayout.addWidget(self.projectEdit)

        self.assetEdit = QLineEdit(self.widget)
        self.assetEdit.setObjectName(u"assetEdit")

        self.horizontalLayout.addWidget(self.assetEdit)

        self.assetTypeEdit = QLineEdit(self.widget)
        self.assetTypeEdit.setObjectName(u"assetTypeEdit")

        self.horizontalLayout.addWidget(self.assetTypeEdit)

        self.newNameEdit = QLineEdit(self.widget)
        self.newNameEdit.setObjectName(u"newNameEdit")

        self.horizontalLayout.addWidget(self.newNameEdit)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(40, 330, 381, 33))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.loadButton = QPushButton(self.widget1)
        self.loadButton.setObjectName(u"loadButton")

        self.horizontalLayout_2.addWidget(self.loadButton)

        self.addButton = QPushButton(self.widget1)
        self.addButton.setObjectName(u"addButton")

        self.horizontalLayout_2.addWidget(self.addButton)

        self.modifyButton = QPushButton(self.widget1)
        self.modifyButton.setObjectName(u"modifyButton")

        self.horizontalLayout_2.addWidget(self.modifyButton)

        self.deleteButton = QPushButton(self.widget1)
        self.deleteButton.setObjectName(u"deleteButton")

        self.horizontalLayout_2.addWidget(self.deleteButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"project", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"asset", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"asset_type", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"new_name", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"\ubd88\ub7ec\uc624\uae30", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"\ub4f1\ub85d", None))
        self.modifyButton.setText(QCoreApplication.translate("MainWindow", u"\uc218\uc815", None))
        self.deleteButton.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
    # retranslateUi

