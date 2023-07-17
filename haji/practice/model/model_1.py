from PySide2.QtCore import  QAbstractTableModel, Qt
COLUMN_HEADERS = ['Name', 'Description', 'create-date', 'update-date']


class TableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.table = [[]]

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.table[index.row()][index.column()]

    def rowCount(self, index):
        return len(self.table)

    def columnCount(self, index):
        return len(self.table[0])
        # return 4

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return COLUMN_HEADERS[section]