import os

from PySide2 import QtCore, QtUiTools
from PySide2.QtWidgets import QMainWindow, QListView

from jiwoon.gazu_api.view.UI.nuki_host_widget import Ui_host_widget


class HostUI(QMainWindow, Ui_host_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # # UI
        # # filetree_view 영역
        # self.filetree.setStyleSheet('background-color: transparent; color: white')
        #
        #
        # # shot_list_view 영역
        # self.shot_list.setStyleSheet('background-color: transparent; font-size: 14px;')
        # self.shot_list.setViewMode(QListView.IconMode)
        # self.shot_list.setIconSize(QtCore.QSize(400, 200))
        # # self.shot_list.setUniformItemSizes(True)
        # self.shot_list.setGridSize(QtCore.QSize(180, 140))
        # # self.shot_list.setMovement(QListView.Static)
        #
        # # shot_detail_label 영역
        # self.label_proj.setStyleSheet('color: #ed8d20;')
        # self.label_seq.setStyleSheet('color: #ed8d20;')
        # self.label_shot.setStyleSheet('color: #ed8d20;')
        # self.label_frame_in.setStyleSheet('color: #ed8d20;')
        # self.label_frame_out.setStyleSheet('color: #ed8d20;')
        # self.label_resolution.setStyleSheet('color: #ed8d20;')
        # self.label_fps.setStyleSheet('color: #ed8d20;')
        # self.label_revision.setStyleSheet('color: #ed8d20;')
        #
        # # task_table 영역
        # self.task_table.setStyleSheet('color: white; background-color: transparent; font-size: 13px; font-weight: 200')
        # # self.task_table.setFixedSize(500, 800)