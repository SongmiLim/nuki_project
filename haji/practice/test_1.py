from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import  QAbstractTableModel, Qt
from MainWindow1_2 import Ui_MainWindow

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


class MyGazu(QMainWindow, Ui_MainWindow):
    _project = None
    _sequence = None
    _shot = None
    _asset = None
    _task_type = None
    _task = None
    _entity = None

    def __init__(self):
        gazu.client.set_host('http://192.168.3.117/api')
        gazu.log_in('admin@netflixacademy.com', 'netflixacademy')
        super().__init__()
        super().setupUi(self)
        self.md = TableModel()
        self.setWindowTitle('Load Asset_by project name')
        # load
        self.loadbtn.clicked.connect(self.load_project)
        self.searchEdit.returnPressed.connect(self.load_project)

        self.tableView.setModel(self.md)



    # def search_project(self):
    #     project = self.searchEdit.text().strip()
    #     if project:
    #         self.pj = gazu.project.get_project_by_name(project)
    #     self.load()

    def load_project (self):
        self.md.table.clear()
        project = self.searchEdit.text().strip()
        if project:
            self._project = gazu.project.get_project_by_name(project)
            # print(self._project)
            asset1 = gazu.asset.all_assets_for_project(self._project)
            # print(asset1)
            for asset in asset1:
                # print(asset)
                self.md.table.append((asset['name'], asset['description'], asset['created_at'], asset['updated_at']))
            # print(self.md.table)
        else:
            self.searchEdit.setPlaceholderText('Not Found...')

        self.md.layoutChanged.emit()
        self.tableView.resizeColumnsToContents()





app = QApplication()
window = MyGazu()
window.show()
app.exec_()


