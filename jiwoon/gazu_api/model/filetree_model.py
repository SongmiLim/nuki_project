from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtCore import Qt
import gazu

gazu.client.set_host("http://192.168.3.117/api")
gazu.log_in("admin@netflixacademy.com", "netflixacademy")


class TreeModel(QStandardItemModel):
    def __init__(self):
        super().__init__()

    def production_tree(self):
        self.clear()
        tasks = gazu.user.all_tasks_to_do()
        project_list = []
        for i in tasks:
            self.p_list = []
            self.projectItem = QStandardItem(i['project_name'])
            if i['project_name'] not in project_list:
                project_list.append(i['project_name'])
                self.p_list.append(i['project_name'])
                self.appendRow(self.projectItem)
                # print('gg', self.p_list)
                self.sequence_tree()

    def sequence_tree(self):
        tasks = gazu.user.all_tasks_to_do()
        self.seq_list = []
        for i in tasks:
            self.s_list = []
            self.seqItem = QStandardItem(i['sequence_name'])
            if i['project_name'] in self.p_list and i['sequence_name'] not in self.seq_list:
                self.seq_list.append(i['sequence_name'])
                self.s_list.append(i['sequence_name'])
                self.projectItem.appendRow(self.seqItem)
                # print('DD', self.seq_list)
                self.shot_tree()

    def shot_tree(self):
        tasks = gazu.user.all_tasks_to_do()
        for i in tasks:
            self.shot_list = []
            self.shotItem = QStandardItem(i['entity_name'])
            if i['project_name'] in self.p_list and i['sequence_name'] in self.s_list and i[
                'entity_name'] not in self.shot_list:
                self.shot_list.append(i['entity_name'])
                self.seqItem.appendRow(self.shotItem)
                # print('hh', self.shot_list)
                # self.shot_detail_filetree()

    def headerData(self, section, orientation, role):
        if (orientation == Qt.Horizontal and role == Qt.DisplayRole):
            if (section == 0): return ' '  # header 기본값 없애주기

    def select_filetree(self, index):
        self.item = self.itemFromIndex(index)
        path_list = []
        shot_name = self.item.text()  # 샷 단계
        if 'SH' in shot_name:  # 영화 제목에 들어가면... ? 조건 수식 더 만들어보기
            project_name = self.item.parent().parent().text()  # 프로젝트 단계
            seq_name = self.item.parent().text()  # 시퀀스 단계

            path_list.append(project_name)
            path_list.append(seq_name)
            path_list.append(shot_name)
            self.shot_detail = '/'.join(path_list)
            print('!!shot_detail!!', self.shot_detail)
            # self.clicked_shot_detail_info(self.shot_detail)  # shot detail 정보 볼수 있는 함수에 연결

        else:
            pass