# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 6 Assignment 3

def make_album(artist, album_title, numsongs="None"):
    make_dict = {'artist': artist, 'title': album_title, 'number of songs': numsongs}
    return make_dict

while True:
    album_title= input("What is the title of the album (or q for quit)? ")
    if album_title == "q":
        break
    artist= input("What is the name of the artist? ")
    album_dict = make_album(artist, album_title)
    print(album_dict)