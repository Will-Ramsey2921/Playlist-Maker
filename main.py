import sys
from PyQt6.QtWidgets import QApplication
from playlist_gui import PlaylistApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlaylistApp()
    window.show()
    sys.exit(app.exec())
