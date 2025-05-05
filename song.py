class Song:
    """Represents a song with a title and an artist."""
    def __init__(self, title: str, artist: str):
        """Initialize a Song instance."""
        self.title = title
        self.artist = artist

    def __str__(self):
        """Return a formatted string representation of the song."""
        return f"{self.title} – {self.artist}"
