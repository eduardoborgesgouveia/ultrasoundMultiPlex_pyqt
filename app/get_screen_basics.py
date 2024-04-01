import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
import pygetwindow as gw


class OBSStudioApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OBS Studio Clone")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel("Fontes de Vídeo e Áudio")
        self.layout.addWidget(self.label)

        self.btn_add_video = QPushButton("Adicionar Fonte de Vídeo")
        self.btn_add_video.clicked.connect(self.add_video_source)
        self.layout.addWidget(self.btn_add_video)

        self.btn_add_audio = QPushButton("Adicionar Fonte de Áudio")
        self.btn_add_audio.clicked.connect(self.add_audio_source)
        self.layout.addWidget(self.btn_add_audio)

    def add_video_source(self):
        self.list_widget.clear()
        windows = gw.getAllTitles()
        for window in windows:
            self.list_widget.addItem(window)

    def add_audio_source(self):
        # Aqui você pode adicionar lógica para adicionar fonte de áudio
        print("Fonte de áudio adicionada")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OBSStudioApp()
    window.show()
    sys.exit(app.exec_())
