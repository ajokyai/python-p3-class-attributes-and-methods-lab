import unittest
from song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        # Reset class attributes before each test
        Song.count = 0
        Song.artists = []
        Song.genres = []
        Song.artist_count = {}
        Song.genre_count = {}

    def test_song_creation(self):
        s = Song("Halo", "Beyonce", "Pop")
        self.assertEqual(Song.count, 1)
        self.assertIn("Beyonce", Song.artists)
        self.assertIn("Pop", Song.genres)
        self.assertEqual(Song.artist_count["Beyonce"], 1)
        self.assertEqual(Song.genre_count["Pop"], 1)

if __name__ == "__main__":
    unittest.main()
