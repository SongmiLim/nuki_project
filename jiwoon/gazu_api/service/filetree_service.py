from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt
import gazu
from jiwoon.gazu_api.model.filetree_model import TreeModel
from jiwoon.gazu_api.service.shot_service import ShotService
from jiwoon.gazu_api.view.task_view import MainUI

class FileTreeService:
    gazu.client.set_host("http://192.168.3.117/api")
    gazu.log_in("admin@netflixacademy.com", "netflixacademy")

    def __init__(self, model, view):
        super().__init__()
        self.model = model
        self.view = view

        self.view.filetree.header()

        if not self.view.filetree.isSortingEnabled():
            self.view.filetree.setSortingEnabled(True) # 할당된 순서대로 표시 후 헤더 누르면 오름차순 정렬

        # self.filetree.expandAll()  # 실행 시 모든 Tree 확장되어 실행하게 함
        self.view.filetree.expandToDepth(0)  # seq 까지만 확장


        # def clicked_shot_detail_info(self, str):
        #     # 선택한 샷 정보 받아오기
        #     shot_info_list = str.split('/')
        #     self.project = shot_info_list[0]
        #     self.sequence = shot_info_list[1]
        #     self.shot = shot_info_list[2]
        #
        #     print(self.project)
        #     print(self.sequence)
        #     print(self.shot)