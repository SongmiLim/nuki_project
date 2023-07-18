from PySide2 import QtCore
from PySide2.QtCore import QAbstractListModel, Signal, Qt


class Model(QAbstractListModel):
    # data_changed = Signal(str)

    def __init__(self):
        super().__init__()
        self.header_title = ["Task Type", "Status", "Ver", "Ext", "Updated At"]
        self.datas = []
        self.todo_tasks = []


    def data(self, index, role):
        if role == Qt.DisplayRole:  # 메인 텍스트
            new_data = self.datas[index.row()]
            return f'[{index.row() + 1}]' + ' name : ' + new_data

        # if role == Qt.DecorationRole:
        #     return index.row()

    # def headerData(self, section, orientation, role=Qt.DisplayRole):
    #     if orientation == Qt.Horizontal and role == Qt.DisplayRole:
    #         return COLUMN_HEADERS[section]
    #     return super().headerData(section, orientation, role)

    def rowCount(self, index):
        return len(self.datas)

    def columnCount(self, parent: QtCore.QModelIndex = QtCore.QModelIndex()):
        """
        header_title에 따른 column의 length
        """
        return len(self.header_title)

    def headerData(self, column: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
        """
        section is the index of the column/row
        """
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.header_title[column]

            return ""

    def set_data(self, data):
        self.data = data
        self.data_changed.emit(data)

    def get_data(self):
        return self.data
