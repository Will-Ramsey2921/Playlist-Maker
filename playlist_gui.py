from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton,
    QLabel, QLineEdit, QMessageBox, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from song import Song
from file_service import save_playlist, load_playlist

class PlaylistApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPod Style Playlist Manager")
        self.setGeometry(400, 150, 350, 500)
        self.setStyleSheet("background-color: #f8f8f8; font-family: Arial; color: #000000;")

        self.songs: list[Song] = load_playlist("playlist.csv")

        layout = QVBoxLayout()
        layout.setSpacing(12)
        self.setLayout(layout)

        self.screen = QListWidget()
        self.screen.setStyleSheet("""
            QListWidget {
                background-color: #ffffff;
                border: 2px solid #000;
                padding: 5px;
                font-size: 12pt;
                color: #000000;
            }
        """)
        self.screen.setFixedHeight(230)
        layout.addWidget(self.screen)

        title_label = QLabel("Song Name:")
        title_label.setStyleSheet("font-weight: bold; font-size: 10pt; color: #000000;")
        layout.addWidget(title_label)

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter song title")
        self.title_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                color: #000000;
                background-color: #ffffff;
                border: 1px solid #aaa;
                border-radius: 6px;
                font-size: 11pt;
            }
        """)
        layout.addWidget(self.title_input)

        artist_label = QLabel("Artist:")
        artist_label.setStyleSheet("font-weight: bold; font-size: 10pt; color: #000000;")
        layout.addWidget(artist_label)

        self.artist_input = QLineEdit()
        self.artist_input.setPlaceholderText("Enter artist name")
        self.artist_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                color: #000000;
                background-color: #ffffff;
                border: 1px solid #aaa;
                border-radius: 6px;
                font-size: 11pt;
            }
        """)
        layout.addWidget(self.artist_input)

        button_frame = QFrame()
        wheel_layout = QVBoxLayout()
        wheel_layout.setSpacing(10)
        button_frame.setLayout(wheel_layout)

        add_btn = QPushButton("➕ Add Song")
        add_btn.clicked.connect(self.add_song)
        add_btn.setStyleSheet(self.button_style())
        wheel_layout.addWidget(add_btn)

        mid_buttons = QHBoxLayout()

        move_up_btn = QPushButton("⬆ Move Up")
        move_up_btn.clicked.connect(self.move_up)
        move_up_btn.setStyleSheet(self.button_style())
        mid_buttons.addWidget(move_up_btn)

        remove_btn = QPushButton("🗑 Remove")
        remove_btn.clicked.connect(self.remove_song)
        remove_btn.setStyleSheet(self.button_style())
        mid_buttons.addWidget(remove_btn)

        move_down_btn = QPushButton("⬇ Move Down")
        move_down_btn.clicked.connect(self.move_down)
        move_down_btn.setStyleSheet(self.button_style())
        mid_buttons.addWidget(move_down_btn)

        wheel_layout.addLayout(mid_buttons)
        layout.addWidget(button_frame)

        self.refresh_screen()

    def button_style(self) -> str:
        return """
            QPushButton {
                background-color: #e0e0e0;
                border: 1px solid #999;
                border-radius: 8px;
                padding: 6px;
                font-size: 10pt;
                color: #000000;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }
        """

    def add_song(self):
        title = self.title_input.text().strip()
        artist = self.artist_input.text().strip()
        if title and artist:
            self.songs.append(Song(title, artist))
            self.refresh_screen()
            save_playlist("playlist.csv", self.songs)
            self.title_input.clear()
            self.artist_input.clear()
        else:
            QMessageBox.warning(self, "Missing Info", "Please enter both song name and artist.")

    def remove_song(self):
        index = self.screen.currentRow()
        if index >= 0:
            del self.songs[index]
            self.refresh_screen()
            save_playlist("playlist.csv", self.songs)

    def move_up(self):
        i = self.screen.currentRow()
        if i > 0:
            self.songs[i - 1], self.songs[i] = self.songs[i], self.songs[i - 1]
            self.refresh_screen()
            self.screen.setCurrentRow(i - 1)
            save_playlist("playlist.csv", self.songs)

    def move_down(self):
        i = self.screen.currentRow()
        if i < len(self.songs) - 1:
            self.songs[i + 1], self.songs[i] = self.songs[i], self.songs[i + 1]
            self.refresh_screen()
            self.screen.setCurrentRow(i + 1)
            save_playlist("playlist.csv", self.songs)

    def refresh_screen(self):
        self.screen.clear()
        for song in self.songs:
            self.screen.addItem(str(song))
