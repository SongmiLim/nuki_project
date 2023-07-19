from PySide2.QtWidgets import QWidget
from nuki_main_ui import Ui_Nuki
from nuki_filetree import TreeModel

class Widget(QWidget, Ui_Nuki):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.model = TreeModel()
        self.filetree.setModel(self.model)

        self.model.production_tree()

        self.filetree.header()

        if not self.filetree.isSortingEnabled():
            self.filetree.setSortingEnabled(True)

        self.update_filetree_btn.clicked.connect(self.model.production_tree)






