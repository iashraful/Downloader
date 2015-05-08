"""
    Here I have used a framework name Qt. Which is PyQt4. This is an UI base 
    framework for creating desktop software. There are some different syntax,
    I have used in framework otherwise python code is same as before. 

    I think it's very much easy and efficient to use. It's really crazy framework.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import urllib.request

class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        self.url_mgs = QLabel("Enter url only")
        self.url = QLineEdit()
        self.path_mgs = QLabel("Enter path for save")
        self.path = QLineEdit()
        self.progress = QProgressBar()
        download = QPushButton("Download")
        browse = QPushButton("Browse")

        self.url.setPlaceholderText("url only")
        self.path.setPlaceholderText("set path for save")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.url_mgs)
        layout.addWidget(self.url)
        layout.addWidget(self.path_mgs)
        layout.addWidget(self.path)
        layout.addWidget(browse)
        layout.addWidget(self.progress)
        layout.addWidget(download)

        self.setLayout(layout)
        self.setWindowTitle("PyDownloader")
        self.setFocus()
        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)

    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self,caption="Save file as", directory=".", filter="All Files (*.*)")
        self.path.setText(QDir.toNativeSeparators(save_file))


    def download(self):
        url = self.url.text()
        path = self.path.text()
        try:
            urllib.request.urlretrieve(url, path, self.report)
        except Exception:
            QMessageBox.warning(self,"Warning", "URL is not valid !!")
            return

        QMessageBox.information(self,"Message","The Download is ready to use !!")
        self.progress.setValue(0)
        self.url.setText("")
        self.path.setText("")


    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.progress.setValue(int(percent))




app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()