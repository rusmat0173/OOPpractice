class Song:

    def __init__(self, title, artist, album, track_number):
        self.title = title
        self.artist = artist
        self.album = album
        self.track_number = track_number

        artist.add_song(self)


class Album:

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

        self.tracks = []

        artist.add_album(self)

    def add_track(self, title, artist=None):
        if artist is None:
            artist = self.artist

        track_number = len(self.tracks)

        song = Song(title, artist, self, track_number)

        self.tracks.append(song)

    def __str__(self):
        return '{}: {}'.format(self.title, self.year)


class Artist:
    def __init__(self, name):
        self.name = name

        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return '{}; {}; {}'.format(self.name, self.albums, self.songs)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)


band = Artist("Bob's Awesome Band")
print(band)

album1 = Album("Bob's First Singles", band, 2013)
# print(album1)
album2 = Album("Bob's Greatest Hits", band, 2014)
# print(album2)

for item in band.albums:
    print(item)

# album1.add_track("A Ballad about Cheese")
# album1.add_track("A Ballad about Cheese (dance remix)")
# album1.add_track("A Third Song to Use Up the Rest of the Space")
#
# playlist = Playlist("My Favourite Songs")
#
# for song in album1.tracks:
#    playlist.add_song(song)