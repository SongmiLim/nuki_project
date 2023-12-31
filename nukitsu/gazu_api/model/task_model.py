from PySide2 import QtCore, QtGui
from PySide2.QtCore import Signal, Qt


class TaskModel(QtCore.QAbstractTableModel):
    task_done = Signal(bool)
    __task_status = None

    def __init__(self):
        super().__init__()
        self.todo_datas = []
        self.header_title = ["Task Type", "Status", "Ver", "Ext", "Updated At"]
        self.color_dict = {
            "Done": QtGui.QColor("red"),
        }
        self.selection_model = []
        self.selected_datas = []

    @property
    def task_status(self):
        return self.__task_status

    @task_status.setter
    def task_status(self, value):
        self.__task_status = value
        self.task_done.emit(self.__task_status)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.todo_datas[index.row()][index.column()]
        elif role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter
        elif role == QtCore.Qt.AccessibleTextRole:
            return self.todo_datas[index.row()][index.column()]
        elif role == QtCore.Qt.BackgroundColorRole:
            return QtGui.QColor(0, 0, 0, 100)
        elif role == QtCore.Qt.TextColorRole and index.column() == 1:
            task_type = self.todo_datas[index.row()][index.column()]
            if task_type in self.color_dict:
                return self.color_dict[task_type]

    def rowCount(self, index) -> int:
        if not index.isValid():
            return len(self.todo_datas) - 1
        return 0

    def columnCount(self, index) -> int:
        if not index.isValid():
            return len(self.header_title)

    def headerData(self, column, orientation, role) -> str:
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.header_title[column]
