import gazu
from PySide2.QtCore import QAbstractTableModel, Qt
from PySide2.QtWidgets import QApplication, QMainWindow
from vfxAPI.view.ui_asset_manage_view import Ui_MainWindow

class AssetAPI:
    __project = None
    __sequence = None
    __shot = None
    __asset = None
    __task_type = None
    __task = None
    __entity = None

    def __init__(self):
        gazu.client.set_host("http://192.168.3.117/api")
        gazu.log_in("admin@netflixacademy.com", "netflixacademy")

    @property
    def project(self):
        return self.__project

    @project.setter
    def project(self, name):
        self.__project = gazu.project.get_project_by_name(name)

    @property
    def sequence(self):
        return self.__sequence

    @sequence.setter
    def sequence(self, name):
        self.__sequence = gazu.shot.get_sequence_by_name(self.project, name)

    @property
    def shot(self):
        return self.__shot

    @shot.setter
    def shot(self, name):
        self.__shot = gazu.shot.get_shot_by_name(self.sequence, name)
        self.__entity = self.__shot

    @property
    def asset(self):
        return self.__asset

    @asset.setter
    def asset(self, name):
        self.__asset = gazu.asset.get_asset_by_name(self.project, name)
        self.__entity = self.__asset

    def get_all_task(self):
        return gazu.user.all_tasks_to_do()

    # 프로젝트를 파라미터로 받아 해당 프로젝트의 모든 에셋들을 반환한다
    def get_all_asset_by_project(self, project_dict):
        __project = project_dict
        return gazu.asset.all_assets_for_project(project_dict)

    # asset을 파라미터로 받아 해당 어셋 타입 이름을 반환한다
    def get_asset_type_name(self, asset_dict):
        # asset_type의 name은 따로 가져와야한다, asset을 가져오면 'entity_type_id'를 얻을 수 있는데 이를 활용한다
        # gazu API의 asset 관련 메서드 중 get_asset_type()에 'entity_type_id'를 파라미터로 넘겨준다
        # 얻은 asset_type의 'name' key를 이용하여 asset_type name을 가져온다
        asset_type = gazu.asset.get_asset_type(asset_dict['entity_type_id'])
        asset_type_name = asset_type['name']
        return asset_type_name

    def create_asset(self, project_name, asset_type_name, asset_name):
        project = gazu.project.get_project_by_name(project_name)
        asset_type = gazu.asset.get_asset_type_by_name(asset_type_name)
        # print(project)
        # print(type(asset_type))

        asset = gazu.asset.new_asset(
            project,
            asset_type,
            asset_name,
            "My asset description"
        )

    def delete_asset(self, asset_name):
        asset = gazu.asset.get_asset_by_name(self.project, asset_name)
        gazu.asset.remove_asset(asset)

    def update_asset(self):
        pass



COLUMN_HEADERS = ['Asset Name', 'Asset Type', 'Created Time', 'Updated Time']

class TableModel(QAbstractTableModel):
    def __init__(self):
        super().__init__()
        self.asset_table = []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.asset_table[index.row()][index.column()]

    def rowCount(self, index):
        return len(self.asset_table)

    def columnCount(self, index):
        if self.asset_table:
            return len(self.asset_table[0])
        else:
            return 0

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return COLUMN_HEADERS[section]  # section => 0, 1, 2,,,, header에서 column 의미
        return super().headerData(section, orientation, role)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = TableModel()
        self.assetView.setModel(self.model)

        # AssetAPI 클래스의 객체로 사용할 gz 생성
        self.gz = AssetAPI()

        # signal & slot
        self.uploadButton.clicked.connect(self.upload)
        self.projectEdit.returnPressed.connect(self.upload)
        self.createButton.clicked.connect(self.create)
        self.deleteButton.clicked.connect(self.delete)
        self.updateButton.clicked.connect(self.update)

        # UI
        self.projectEdit.setPlaceholderText('Project name을 입력하세요')
        self.projectNameEdit.setPlaceholderText('Project name')
        self.newAssetTypeEdit.setPlaceholderText('Asset type')
        self.newAssetNameEdit.setPlaceholderText('new Asset name')

    def upload(self):
        print('get_all_asset')
        # upload 시 마다 asset_table은 초기화한다
        self.model.asset_table.clear()
        self.gz.project = None

        # 사용자에게 입력받는 프로젝트명을 gz.project로 set
        self.gz.project = self.projectEdit.text()

        # 입력된 게 없을 때 load 버튼 클릭 시 모든 프로젝트 출력 방지
        # if not self.projectEdit.text():
        #     return

        # 해당 프로젝트의 모든 에셋을 rows에 할당한다
        items = self.gz.get_all_asset_by_project(self.gz.project)

        # 각 item 당 key에 따른 value들을 asset_table에 추가한다
        for item in items:
            # asset_type의 name은 따로 가져와야한다
            asset_type_name = self.gz.get_asset_type_name(item)
            # print(asset_type)
            # print(type(asset_type_name))
            # print(item)

            self.model.asset_table.append(
                (item['name'], asset_type_name, item['created_at'], item['updated_at']))
        print('asset_table', self.model.asset_table)
        self.model.layoutChanged.emit()

        # # 현재 window 크기에 맞게 scroll 적용
        # self.assetView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        # 현재 cell column 크기 조정 ( cell 내용에 맞게 )
        self.assetView.resizeColumnsToContents()

        self.projectNameEdit.setText(self.projectEdit.text())
        self.projectNameEdit.setEnabled(False)

    def create(self):
        print('create')
        # if self.projectEdit.text():
        #     project_name = self.projectEdit.text()
        #     self.projectNameEdit.setEnabled(False)
        # else:
        project_name = self.projectNameEdit.text()
        new_asset_type = self.newAssetTypeEdit.text()
        new_asset_name = self.newAssetNameEdit.text()

        self.gz.create_asset(project_name, new_asset_type, new_asset_name)
        self.projectNameEdit.setText('')
        self.newAssetTypeEdit.setText('')
        self.newAssetNameEdit.setText('')
        self.upload()
        self.model.layoutChanged.emit()

    def update(self):
        print('update')
        # asset = gazu.asset.update_asset(new_values_dict)

    def delete(self):
        print('delete')
        indexes = self.assetView.selectedIndexes()
        if indexes:
            index = indexes[0]
            # print(self.model.asset_table[index.row()])
            clicked_asset = self.model.asset_table[index.row()]
            clicked_asset_name = clicked_asset[0]
            # print(clicked_asset_name)
            self.gz.delete_asset(clicked_asset_name)

        self.upload()
        self.model.layoutChanged.emit()


app = QApplication()
window = MainWindow()
window.show()
app.exec_()
