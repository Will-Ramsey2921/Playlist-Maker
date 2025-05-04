import csv
from song import Song

def save_playlist(filename: str, songs: list[Song]) -> None:
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for song in songs:
            writer.writerow([song.title, song.artist])

def load_playlist(filename: str) -> list[Song]:
    songs = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    songs.append(Song(row[0], row[1]))
    except FileNotFoundError:
        pass
    return songs
