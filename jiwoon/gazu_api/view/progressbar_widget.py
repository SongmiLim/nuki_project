from PySide2.QtWidgets import QMainWindow


class ProgressBar(QMainWindow):
    def __init__(self):
        super().__init__()

    @staticmethod
    def set_progressbar(self, value):
        styleSheet = '''
        QFrame{
            border-radius: 75px;
            background-color: qconicalgradient(cx: 0.5, cy: 0.5, angle: 90,
             stop:{STOP_1} rgba(206, 92, 0, 0), stop:{STOP_2} rgba(237, 141, 32, 255));
        }
        '''
        value = round(value, 2)
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # Fix MAX VALUE
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"
        self.percentage_label.setText('<p><span style=\" font-size:28pt;\">' + (
                str(value) + '</span><span style=\" vertical-align:super;\">%</span></p>'))
        newStyleSheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
        self.circularProgress.setStyleSheet(newStyleSheet)
