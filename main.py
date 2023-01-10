import sys
from PyQt5.QtCore import QUrl, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QWidget, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('Google Map with PyQt')
        self.resize(1024, 768)

        self.__view = QWebEngineView(self)

        self.__view.setUrl(QUrl("https://maps.google.com"))

        self.__lbl = QLabel('Loading...')
        self.__lbl.setAlignment(Qt.AlignCenter)
        self.__lbl.setFont(QFont('Arial', 32))

        lay = QVBoxLayout(self)
        lay.addWidget(self.__lbl)
        lay.addWidget(self.__view)

        self.__view.hide()

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        self.__view.loadFinished.connect(self.__finished)
        self.setCentralWidget(mainWidget)

    def __finished(self):
        self.__lbl.hide()
        self.__view.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
