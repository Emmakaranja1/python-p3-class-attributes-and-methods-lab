class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

      # Proper method calls (once per instance)
        Song.add_song_to_count()
        Song.genres.append(genre)
        Song.artists.append(artist)
        Song.add_to_genres()
        Song.add_to_artists()
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls):
        cls.genres = list(set(cls.genres))

    @classmethod
    def add_to_genres(cls):
        cls.genres = list(set(cls.genres))  # ensure uniqueness

    @classmethod
    def add_to_artists(cls):
        cls.artists = list(set(cls.artists))  # ensure uniqueness

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    pass
