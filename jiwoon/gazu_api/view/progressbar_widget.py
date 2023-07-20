import sys
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont)
from PySide2.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect
from jiwoon.gazu_api.view.UI.nuki_main_widget import Ui_Nuki

'''
GUI FILE
'''

class ProgressBar(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Nuki()
        self.ui.setupUi(self)

        self.value = 40
        self.ui.percentage_label.setText('<p><span style=\" font-size:28pt;\">' + (str(self.value) + '</span><span style=\" vertical-align:super;\">%</span></p>'))

        # Apply shadow drop
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)
        self.show()

    def progressBarValue(self, value):
        styleSheet = '''
        QFrame{
            border-radius: 75px;
            background-color: qconicalgradient(cx: 0.5, cy: 0.5, angle: 90,
             stop:{STOP_1} rgba(206, 92, 0, 0), stop:{STOP_2} rgba(237, 141, 32, 255));
        }
        '''
        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # Fix MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        newStyleSheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.ui.circularProgress.setStyleSheet(newStyleSheet)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProgressBar()
    sys.exit(app.exec_())