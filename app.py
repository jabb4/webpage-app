from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys, time

class Window(QWidget):
    def __init__(self):

        ### Change these tre settings ###
        self.url = "https://duckduckgo.com"
        self.window_title = "Example"
        self.window_geometry = {"hight": 400, "width": 600, "x-pos": 500, "y-pos": 100}
        ### Change these tre settings ###

        super().__init__()
        self.initUI()

    ### Change this function to do stuff when closing the window ###
    def closeWindow(self):
        time.sleep(1)
    ### Change this function to do stuff when closing the window ###
        
    def initUI(self):
        self.setGeometry(self.window_geometry["x-pos"], self.window_geometry["y-pos"], self.window_geometry["width"], self.window_geometry["hight"])
        self.setWindowTitle(self.window_title)

        vbox = QVBoxLayout(self)

        self.webEngineView = QWebEngineView()
        vbox.addWidget(self.webEngineView)
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)

        self.webEngineView.setUrl(QUrl(self.url))
        self.show()

    def closeEvent(self, event):
        self.closeWindow()
        event.accept()



def run_app():
    main = QApplication(sys.argv)
    window = Window()
    sys.exit(main.exec_())

if __name__ == "__main__":
    run_app()