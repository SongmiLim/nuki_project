import sys
import os
from jiwoon.gazu_api.view.UI.upload_ui import Ui_MainWindow
from PySide2.QtGui import QColor, QPalette, QFont
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QFileSystemModel, QWidget, QAbstractItemView
)
from PySide2.QtCore import Qt, QStringListModel


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setup_file_tree()
        self.setWindowTitle('Upload to KITSU')
        self.exr_list.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def setup_file_tree(self):
        # Create the QFileSystemModel and set it up with the QTreeView
        root_path = "/home/rapa/Nuki_Project"
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath(root_path)  # Set the root path to your desired starting directory
        self.treeView.setModel(self.file_system_model)
        self.treeView.setRootIndex(self.file_system_model.index(self.file_system_model.rootPath()))
        self.treeView.setSortingEnabled(False)

        # customize the text in the treeview
        palette = self.treeView.palette()
        text_color = QColor(255, 255, 255) # white
        palette.setColor(QPalette.Text, text_color)
        font = QFont("Arial", 10)
        self.treeView.setPalette(palette)
        self.treeView.setFont(font)

        # customize the text in the listView
        palette = self.exr_list.palette()
        text_color = QColor(255, 255, 255) # white
        palette.setColor(QPalette.Text, text_color)
        font = QFont("Arial", 10)
        self.exr_list.setPalette(palette)
        self.exr_list.setFont(font)

        # Adjust the width of the first column to show the file names properly
        self.treeView.setColumnWidth(0, 160)
        self.treeView.setColumnWidth(1, 50)
        self.treeView.setColumnWidth(2, 70)

        # signal
        self.file_system_model.directoryLoaded.connect(self.expand_tree)
        self.treeView.clicked.connect(self.on_tree_item_clicked)
        self.dir_lineedit.textChanged.connect(self.text_changed)

    def expand_tree(self):
        root_index = self.file_system_model.index(self.file_system_model.rootPath())
        self.expand_tree_recursive(root_index, 'pre-comp')

    def expand_tree_recursive(self, index, path):
        # Recursively expand all items in the tree
        if not index.isValid():
            return
        self.treeView.expand(index)
        if path == index.data(Qt.ItemDataRole.DisplayRole):
            return
        for i in range(self.file_system_model.rowCount(index)):
            child_index = index.child(i, 0)
            if child_index.isValid():
                self.expand_tree_recursive(child_index, path)

    def on_tree_item_clicked(self, index):
        if not index.isValid():
            return
        path = self.file_system_model.filePath(index) # 클릭 된 아이템 파일 경로
        self.dir_lineedit.setText(path)

        files = os.listdir(path)
        files.sort()

        string_list_model = QStringListModel(files)
        self.exr_list.setModel(string_list_model)

        # multiselection
        selected_indexes = self.exr_list.selectedIndexes()
        selected_files = [string_list_model.data(index, Qt.DisplayRole) for index in selected_indexes]

        print("selected_files:")
        for file in selected_files:
            print(file)

    def text_changed(self, text):
        path = text
        index = self.file_system_model.index(path)
        self.treeView.setCurrentIndex(index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())