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
                print('gg', self.p_list)
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
                print('DD', self.seq_list)
                self.shot_tree()

    def shot_tree(self):
        tasks = gazu.user.all_tasks_to_do()
        shot_list = []
        for i in tasks:
            shotItem = QStandardItem(i['entity_name'])
            if i['project_name'] in self.p_list and i['sequence_name'] in self.s_list and i['entity_name'] not in shot_list:
                shot_list.append(i['entity_name'])
                self.seqItem.appendRow(shotItem)
                print('hh', shot_list)

    def headerData(self, section, orientation, role):
        if (orientation == Qt.Horizontal and role == Qt.DisplayRole):
            if (section == 0): return ' ' # header 기본값 없애주기




