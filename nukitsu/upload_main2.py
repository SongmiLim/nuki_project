import sys
from PySide2.QtWidgets import QApplication
from nukitsu.gazu_api.service.upload import UUpload

def show_ui():
    # app = QApplication(sys.argv)
    window = UUpload()
    window.show()
    # sys.exit(app.exec_())

if __name__ == '__main__':
    show_upload_ui()