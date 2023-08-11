import sys
import os
import re
from jiwoon.gazu_api.view.UI.upload_ui import Ui_MainWindow
from PySide2.QtGui import QColor, QPalette, QFont
from PySide2.QtWidgets import QApplication, QMainWindow, QFileSystemModel, QAbstractItemView, QHeaderView
from PySide2.QtCore import Qt, QStringListModel


class UUpload(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.file_system_model = None
        self.string_list_model = None
        self.setupUi(self)
        self.setup_file_tree()
        self.setWindowTitle('Upload to KITSU')
        self.exr_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.comment_plaintextedit.setPlaceholderText('Leave your comment...')
        self.comment_plaintextedit.setFocus()
        self.upload_msg_label.setText('')

        self.select_all_btn.setStyleSheet("")
        self.upload_btn.setStyleSheet("")


    def setup_file_tree(self):
        # Create the QFileSystemModel and set it up with the QTreeView
        root_path = "/home/rapa/kitsu/nuki"
        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath(root_path)
        self.treeView.setModel(self.file_system_model)
        self.treeView.setRootIndex(self.file_system_model.index(self.file_system_model.rootPath()))
        self.treeView.setSortingEnabled(False)

        # customize the text in the treeview
        palette = self.treeView.palette()
        text_color = QColor(255, 255, 255)  # white
        palette.setColor(QPalette.Text, text_color)
        font = QFont("Arial", 10)
        self.treeView.setPalette(palette)
        self.treeView.setFont(font)

        # customize the text in the listView
        palette = self.exr_list.palette()
        text_color = QColor(255, 255, 255)  # white
        palette.setColor(QPalette.Text, text_color)
        font = QFont("Arial", 10)
        self.exr_list.setPalette(palette)
        self.exr_list.setFont(font)

        # set the column widths to be automatically adjusted
        self.treeView.header().setSectionResizeMode(QHeaderView.ResizeToContents)

        # signal
        self.file_system_model.directoryLoaded.connect(self.expand_tree)
        self.treeView.clicked.connect(self.on_tree_item_clicked)
        self.dir_lineedit.textChanged.connect(self.text_changed)
        self.select_all_btn.clicked.connect(self.select_all_btn_clicked)
        self.upload_btn.clicked.connect(self.upload_btn_clicked)

    def expand_tree(self):
        root_index = self.file_system_model.index(self.file_system_model.rootPath())
        path = r'v\d{3}'
        # root_path = re.findall(r'v\b\d{1,3}\d')
        self.expand_tree_recursive(root_index, path)

    def expand_tree_recursive(self, index, path):
        # Recursively expand all items in the tree
        if not index.isValid():
            return
        self.treeView.expand(index)
        folder_name = index.data(Qt.ItemDataRole.DisplayRole)
        if re.match(path, folder_name):
            return
        for i in range(self.file_system_model.rowCount(index)):
            child_index = index.child(i, 0)
            if child_index.isValid():
                self.expand_tree_recursive(child_index, path)

    def disable_buttons(self):
        self.upload_btn.setEnabled(False)
        self.select_all_btn.setEnabled(False)

        # self.upload_btn.setStyleSheet("color: gray")
        # self.select_all_btn.setStyleSheet('color: gray')

        # self.upload_btn.setFocusPolicy(Qt.NoFocus)
        # self.select_all_btn.setFocusPolicy(Qt.NoFocus)

    def set_enabled_buttons(self):
        self.upload_btn.setEnabled(True)
        self.select_all_btn.setEnabled(True)
        # self.upload_btn.setStyleSheet('')
        # self.select_all_btn.setStyleSheet('')

    def on_tree_item_clicked(self, index):
        if not index.isValid():
            return
        self.path = self.file_system_model.filePath(index) # 클릭 된 아이템 파일 경로
        self.dir_lineedit.setText(self.path)

        pattern = r'v\d{3}'
        # folder_name = index.data(Qt.ItemDataRole.DisplayRole)
        # print(folder_name)

        if not os.path.basename(self.path).endswith('exr'):
            self.upload_msg_label.setText('')
            self.exr_list.setEnabled(True)
            self.exr_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.disable_buttons()
        else:
            self.set_enabled_buttons()

        # print(self.path)
        files = os.listdir(self.path)
        files.sort()
        self.list_len = len(files)

        # Get the parent folder of the clicked folder
        parent_folder = index.parent().data(Qt.ItemDataRole.DisplayRole)

        # Check if the clicked folder is match with the pattern.
        if re.match(pattern, parent_folder):
            if files:
                try:
                    split_files = files[0].split('.')
                    self.name_split = split_files[0]
                    self.count_split = split_files[1]
                    self.format_split = split_files[2]
                    self.upload_msg_label.setText('')
                    self.list_enabled_setting()

                except IndexError:
                    # If the format is incorrect, set default values and show an error message.
                    self.name_split = "No Name"
                    self.count_split = '0001'
                    self.format_split = 'exr'
                    self.upload_msg_label.setText('<Error> \n Incorrect file format')
                    self.upload_msg_label.setStyleSheet('color : red;')
                    self.exr_list.setEnabled(False)
                    # set the color grey when disabled.
                    palette = self.exr_list.palette()
                    color = QColor(100, 100, 100)
                    palette.setColor(QPalette.Text, color)
                    self.exr_list.setPalette(palette)
        else:
            self.list_enabled_setting()

        self.string_list_model = QStringListModel(files)
        self.exr_list.setModel(self.string_list_model)
        # signal
        self.exr_list.selectionModel().selectionChanged.connect(self.on_listview_selection_changed)

    def list_enabled_setting(self):
        self.exr_list.setEnabled(True)
        palette = self.exr_list.palette()
        color = QColor(255, 255, 255) # White color when enabled.
        palette.setColor(QPalette.Text, color)
        self.exr_list.setPalette(palette)

    def text_changed(self, text):
        path = text
        index = self.file_system_model.index(path)
        self.treeView.setCurrentIndex(index)

    def on_listview_selection_changed(self):
        selected_indexes = self.exr_list.selectedIndexes()
        if selected_indexes:
            self.get_selected_files()

    def select_all_btn_clicked(self):
        self.exr_list.selectAll()

    def get_selected_files(self):
        selected_indexes = self.exr_list.selectedIndexes()
        selected_files = [self.string_list_model.data(index, Qt.DisplayRole) for index in selected_indexes]
        print('selected files: ', selected_files)
        return selected_files

    def run_ffmpeg(self, commands):
        if os.system(commands) == 0:
            print("ffmpeg Script Ran Successfully")
            self.upload_msg_label.setText('Upload Success!!')
            self.upload_msg_label.setStyleSheet('color: #ed8d20;')
        else:
            print("There was an error running your ffmpeg script")
            self.upload_msg_label.setText('Error')
            self.upload_msg_label.setStyleSheet('color: red;')

    def convert_to_mp4(self):
        input_dir = self.path
        print(self.path)
        input_file_name = self.name_split
        input_file_extension = self.format_split
        output_codec = '-c:v libx264'
        output_pixel = '-pix_fmt yuv420p'
        output_dir = self.path.replace('exr', 'mp4')
        output_name = self.name_split
        output_vide_format = 'mp4'

        if self.count_split.isdigit():
            num_digits = len(self.count_split)
            num_format = f'%0{num_digits}d'
            print(num_format)
        else:
            num_format = '%04d'

        command_input = f'ffmpeg -i {input_dir}/{input_file_name}.{num_format}.{input_file_extension} ' \
                        f'{output_codec} {output_pixel} {output_dir}/{output_name}.{output_vide_format}'
        print(command_input)
        self.run_ffmpeg(command_input)

    def extract_thumbnail_from_exr(self):
        input_dir = self.path
        input_file_name = self.name_split
        input_file_extension = self.format_split
        # middle of the frame.
        num_digits = len(self.count_split)
        input_file_num = str(int(self.list_len / 2)).zfill(num_digits)

        input_file_path = f'{input_dir}/{input_file_name}.{input_file_num}.{input_file_extension}'

        output_dir = self.path.replace('exr', 'jpg')
        output_name = f'{self.name_split}_thumbnail'
        output_vide_format = 'jpg'
        output_file_path = f'{output_dir}/{output_name}.{output_vide_format}'
        jpeg_pixel = '640'

        command_input = f'ffmpeg -i {input_file_path} -vf "scale={jpeg_pixel}:-1" -vframes 1 {output_file_path}'
        print(command_input)
        self.run_ffmpeg(command_input)

    def upload_btn_clicked(self):
        self.convert_to_mp4()
        self.extract_thumbnail_from_exr()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
# window = UUpload()
# window.show()
    # sys.exit(app.exec_())

def show_upload_ui():
    # app = QApplication(sys.argv)
    window = UUpload()
    window.show()
    # sys.exit(app.exec_())

if __name__ == '__main__':
    show_upload_ui()