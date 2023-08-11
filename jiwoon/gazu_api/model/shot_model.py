from PySide2.QtCore import QAbstractListModel, Qt
from PySide2.QtGui import QColor


class ShotModel(QAbstractListModel):

    def __init__(self):
        super().__init__()
        self.datas = []
        self.todo_shots = []

    def data(self, index, role):
        if role == Qt.DisplayRole:  # 메인 텍스트
            return self.todo_shots[index.row()][0]  # shot 관련 정보를 [text, thumbnail] 로 받아와서 text는 [][0]로 받아온다

        if role == Qt.DecorationRole:  # 썸네일
            thumbnail = self.todo_shots[index.row()][1]  # thumbnail은 [][1]로 받아온다
            thumbnail_resized = thumbnail.scaled(150, 100, Qt.KeepAspectRatio)
            return thumbnail_resized

        if role == Qt.ForegroundRole:
            return QColor('white')

    def rowCount(self, index):
        return len(self.todo_shots)


