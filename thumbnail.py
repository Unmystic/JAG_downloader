import sys
import os

from PySide6.QtGui import QPixmap
import yt_dlp

from paths import Path
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

URL = "https://www.youtube.com/watch?v=1hr-5b_WEYg"
ydl_opts = {
    "extract_flat": "discard_in_playlist",
    "fragment_retries": 10,
    "ignoreerrors": "only_download",
    "nocheckcertificate": True,
    "outtmpl": {"default": "thumb"},
    "postprocessors": [
        {"format": "png", "key": "FFmpegThumbnailsConvertor", "when": "before_dl"},
        {"key": "FFmpegConcat", "only_multi_video": True, "when": "playlist"},
    ],
    "proxy": "socks5://127.0.0.1:12334",
    "retries": 10,
    "skip_download": True,
    "warn_when_outdated": True,
    "writethumbnail": True,
}


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        layout = QVBoxLayout()

        self.url = QLineEdit()
        self.url.setPlaceholderText("Insert full url here")
        self.btn = QPushButton("Set thumbnail")
        self.btn.pressed.connect(self.setThumb)

        self.label = QLabel()

        layout.addWidget(self.url)
        layout.addWidget(self.btn)
        layout.addWidget(self.label)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

    def setThumb(self):
        url = self.url.text()
        if self.is_valid_youtube_url(url):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                try:
                    ydl.download(url)
                    self.label.setPixmap(QPixmap("thumb.png"))
                except Exception:
                    print("Error!!!")

    def is_valid_youtube_url(self, url):
        opts = {
            "quiet": True,
            "proxy": "socks5://127.0.0.1:12334",
        }
        with yt_dlp.YoutubeDL(opts) as ydl:
            try:
                ydl.extract_info(url, download=False)
                return True
            except Exception:
                return False


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
