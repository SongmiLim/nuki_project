import gazu
from PySide2.QtWidgets import QApplication, QMainWindow
from kiya.view.MainWindow1_2 import Ui_MainWindow
from kiya.model.model_1 import TableModel


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
        # print(type(self.md))
        self.setWindowTitle('Load Asset_by project name')
        # load
        self.loadbtn.clicked.connect(self.load_project)
        self.searchEdit.returnPressed.connect(self.load_project)
        self.tableView.setModel(self.md)

    def load_project (self):
        self.md.table.clear()
        project = self.searchEdit.text().strip()
        if project:
            self._project = gazu.project.get_project_by_name(project)
            asset1 = gazu.asset.all_assets_for_project(self._project)
            for asset in asset1:
                self.md.table.append((asset['name'], asset['description'], asset['created_at'], asset['updated_at']))
        else:
            self.searchEdit.setPlaceholderText('Not Found...')
        self.md.layoutChanged.emit()
        self.tableView.resizeColumnsToContents()


app = QApplication()
window = MyGazu()
window.show()
app.exec_()