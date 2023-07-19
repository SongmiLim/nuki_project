from PySide2 import QtCore, QtGui
from PySide2.QtCore import QAbstractListModel, Signal, Qt, QModelIndex
from PySide2.QtGui import QColor


class TaskModel(QtCore.QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.todo_datas = []
        self.header_title = ["Task Type", "Status", "Ver", "Ext", "Updated At"]

        self.color_dict = {
            "Storyboard": QtGui.QColor(0, 255, 0),
            "Layout": QtGui.QColor("cyan"),
            "Animation": QtGui.QColor("red"),
            "Lighting": QtGui.QColor(255, 255, 0),
            "FX": QtGui.QColor(153, 153, 255),
            "Rendering": QtGui.QColor("magenta"),
            "Plate": QtGui.QColor(255, 102, 0),
            "Matchmove": QtGui.QColor(159, 255, 158),
            "Camera": QtGui.QColor(255, 153, 204),
        }

    def data(self, index, role):  # 해당 index에 data 가져오기
        # print(self.todo_tasks)
        # print(self.table)
        if role == Qt.DisplayRole:
            return self.todo_datas[index.row()][index.column()]

        elif role == QtCore.Qt.BackgroundColorRole:
            return QtGui.QColor(0, 0, 0, 100)

        elif role == QtCore.Qt.TextColorRole and index.column() == 0:
            task_type = self.todo_datas[index.row()][index.column()]
            if task_type in self.color_dict:
                return self.color_dict[task_type]

    def rowCount(self, index: QModelIndex):
        if not index.isValid():
            return 6
        return 0

    def columnCount(self, index):
        if not index.isValid():
            return len(self.header_title)


    # Custom Header
    def headerData(self, column: int, orientation: QtCore.Qt.Orientation, role: int = QtCore.Qt.DisplayRole):
        """
        section is the index of the column/row
        """
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.header_title[column]


