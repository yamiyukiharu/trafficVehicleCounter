import sys
from PySide2.QtCore import Qt, QThread
from PySide2.QtWidgets import QApplication
from qt.view_controller import ViewController
from model import Model
import pyqtgraph as pg
import qtmodern.styles

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True) #enable highdpi scaling
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True) #use highdpi icons
pg.setConfigOptions(imageAxisOrder='row-major') #pyqtgraph default uses column major, resulting in rotated images

class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__()
        self.modelThread = QThread()
        self.model = Model()
        self.model.moveToThread(self.modelThread)
        self.modelThread.start()
        self.modelThread.setPriority(QThread.HighestPriority)

        self.viewController = ViewController(self.model)
        self.viewController.show()

if __name__ == '__main__':
    app = App(sys.argv)
    qtmodern.styles.light(app)
    sys.exit(app.exec_())