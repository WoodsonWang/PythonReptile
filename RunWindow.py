import sys
import pachong
import PyQt5
from PyQt5.QtWidgets import QApplication,QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwin = QMainWindow()
    ui = pachong.Ui_MainWindow()
    ui.setupUi(mainwin)
    mainwin.show()
    sys.exit(app.exec_())
