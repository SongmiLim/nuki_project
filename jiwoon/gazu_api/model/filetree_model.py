from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt, Signal
import gazu
import json
import os

basedir = os.path.dirname(__file__)
user_data = os.path.join(basedir, '../data/user.json')



class TreeModel(QStandardItemModel):
    item_clicked = Signal(str)

    def __init__(self):
        super().__init__()
        self.tree_clicked_info = None

    def production_tree(self):
        self.clear()
        tasks = gazu.user.all_tasks_to_do()
        project_list = []
        for i in tasks:
            comp_task = i['task_type_name']
            if comp_task == 'Compositing':  # Compositing task 만 view 에 보여주기
                self.project = None
                self.projectItem = QStandardItem(i['project_name'])
                if i['project_name'] not in project_list:
                    project_list.append(i['project_name'])
                    self.project = i['project_name']
                    self.appendRow(self.projectItem)
                    self.sequence_tree()
                if len(i['project_name']) > 18:  # project name 글자가 길 경우 라벨로 풀 네임 보여주기
                    self.projectItem.setToolTip(i['project_name'])

    def sequence_tree(self):
        tasks = gazu.user.all_tasks_to_do()
        self.seq_list = []
        for i in tasks:
            comp_task = i['task_type_name']
            if comp_task == 'Compositing':  # Compositing task 만 view 에 보여주기
                self.sequence_list = []
                self.seqItem = QStandardItem(i['sequence_name'])
                if i['project_name'] == self.project and i['sequence_name'] not in self.seq_list:
                    self.seq_list.append(i['sequence_name'])
                    self.sequence_list.append(i['sequence_name'])
                    self.projectItem.appendRow(self.seqItem)
                    self.shot_tree()

    def shot_tree(self):
        tasks = gazu.user.all_tasks_to_do()
        for i in tasks:
            comp_task = i['task_type_name']
            if comp_task == 'Compositing':  # Compositing task 만 view 에 보여주기
                self.shot_list = []
                self.shotItem = QStandardItem(i['entity_name'])
                if i['project_name'] == self.project and i['sequence_name'] in self.sequence_list and i[
                    'entity_name'] not in self.shot_list:
                    self.shot_list.append(i['entity_name'])
                    self.seqItem.appendRow(self.shotItem)

    def headerData(self, section, orientation, role):
        if (orientation == Qt.Horizontal and role == Qt.DisplayRole):
            # if (section == 0): return ' '  # header 기본값 없애주기
            if (section == 0):  # header에 user id 넣어주기
                with open(user_data, 'r') as f:
                    data = json.load(f)
                    user_id = data['user_id'].split('@')
                    return user_id[0]

    def filetree_item_clicked(self, index):  # 로컬 파일에 연결 함수
        depth = self.item_depth(index)

        self.item = self.itemFromIndex(index)
        path_list = []
        # if 'SH' in shot_name:  # 영화 제목에 들어가면... ? 조건 수식 더 만들어보기
        if depth == 3:  # 3번째 깊이에 있는 아이템만 선택 가능
            project_name = self.item.parent().parent().text()  # 프로젝트 단계
            seq_name = self.item.parent().text()  # 시퀀스 단계
            shot_name = self.item.text()  # 샷 단계

            path_list.append(project_name)
            path_list.append(seq_name)
            path_list.append(shot_name)

            text = '/'.join(path_list)
            self.item_clicked.emit(text)

        elif depth == 1 or depth == 2:  # 프로젝트, 시퀀스 선택 시 아무런 동작 일어나지 않도록 하기
            pass


    # def select_filetree(self, index):  # 샷 연결 함수
    #     depth = self.item_depth(index)
    #     self.item = self.itemFromIndex(index)
    #     path_list = []
    #     if depth == 3:  # 3번째 깊이에 있는 아이템만 선택 가능
    #         # print(depth)
    #         # print('shot select')
    #         project_name = self.item.parent().parent().text()  # 프로젝트 단계
    #         seq_name = self.item.parent().text()  # 시퀀스 단계
    #         shot_item = self.item.text()  # 샷 단계
    #         path_list.append(project_name)
    #         path_list.append(seq_name)
    #         path_list.append(shot_item)
    #
    #         self.tree_clicked_info = '/'.join(path_list)
    #         print(self.tree_clicked_info)
    #
    #     elif depth == 1 or depth == 2:  # 프로젝트, 시퀀스 선택 시 아무런 동작 일어나지 않도록 하기
    #         pass


    def item_depth(self, index):  # 아이템 깊이 알아보는 함수
        depth = 0
        while index.isValid():
            index = index.parent()
            depth += 1
        return depth
