from PySide2.QtWidgets import QApplication, QMainWindow
from practice.AssetCRUD.view.ui_asset_manage_view import Ui_MainWindow
from practice.AssetCRUD.model.asset_api import AssetAPI
from practice.AssetCRUD.model.tabel_model import TableModel


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = TableModel()
        self.assetView.setModel(self.model)

        # AssetAPI 클래스의 객체로 사용할 gz 생성
        self.gz = AssetAPI()

        # signal & slot
        self.uploadButton.clicked.connect(self.upload_button_clicked)
        self.projectEdit.returnPressed.connect(self.upload_button_clicked)
        self.createButton.clicked.connect(self.create_button_clicked)
        self.deleteButton.clicked.connect(self.delete_button_clicked)
        self.updateButton.clicked.connect(self.update_button_clicked)

        # UI
        self.projectEdit.setPlaceholderText('Project name을 입력하세요')
        self.projectNameEdit.setPlaceholderText('Project name')
        self.newAssetTypeEdit.setPlaceholderText('Asset type')
        self.newAssetNameEdit.setPlaceholderText('new Asset name')

    def upload_button_clicked(self):
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

    def create_button_clicked(self):
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

    def update_button_clicked(self):
        print('update')
        # asset = gazu.asset.update_asset(new_values_dict)

    def delete_button_clicked(self):
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
