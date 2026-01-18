from song import Song

# Create some songs
s1 = Song("99 Problems", "Jay-Z", "Rap")
s2 = Song("Halo", "Beyonce", "Pop")
s3 = Song("In Da Club", "50 Cent", "Rap")

print("Total songs:", Song.count)
print("Artists:", Song.artists)
print("Genres:", Song.genres)
print("Artist count:", Song.artist_count)
print("Genre count:", Song.genre_count)
