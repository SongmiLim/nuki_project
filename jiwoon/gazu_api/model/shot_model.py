from PySide2 import QtCore
from PySide2.QtCore import QAbstractListModel, Signal, Qt


class shotModel(QAbstractListModel):
    # data_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.datas = []
        self.todo_shots = []

    def data(self, index, role):
        if role == Qt.DisplayRole:  # 메인 텍스트
            return self.todo_shots[index.row()]

        # if role == Qt.DecorationRole:
        #     return index.row()

    # def headerData(self, section, orientation, role=Qt.DisplayRole):
    #     if orientation == Qt.Horizontal and role == Qt.DisplayRole:
    #         return COLUMN_HEADERS[section]
    #     return super().headerData(section, orientation, role)
    #
    def rowCount(self, index):
        return len(self.todo_shots)
    #     """
    #     header_title에 따른 column의 length
    #     """
    #     return 2


    # def set_data(self, data):
    #     self.data = data
    #     self.data_changed.emit(data)

    # def get_data(self):
    #     return self.data
