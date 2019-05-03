import comments
import song

number_of_underrated_songs = 2
phrases = 'underrated;recognition;talented'
underrated_songs = comments.find_comments('https://www.youtube.com/watch?v=ZkzY29DKHEQ', phrases, number_of_underrated_songs)

with open('results.txt', 'w') as file: 
    for single_song in underrated_songs:
        file.write("Title: " + single_song.title + "\n") 
        file.write("Url: " + single_song.url + "\n")
        file.write("\n")