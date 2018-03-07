import media
import fresh_tomatoes

toy_story=media.Movie("Toy Story",
                      "A story of a stupid kid that have stupid dolls",
                      "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)
avatar=media.Movie("Avatar",
                   "A marine on drugs",
                   "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                   "https://www.youtube.com/watch?v=d1_JBMrrYw8")
Frequencies=media.Movie("Frequencies",
                        "A guy that live with bad luck until he fall in love with a girl that change his world",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcTU5J1eE1vp9WSBDdcIrdMZyGXrDEmJ7ZuLYk1vBbK-6ogm8Yt_",
                        "https://www.youtube.com/watch?v=cQHc-WkT77s")               
schoolofrock=media.Movie("School of Rock",
                           "A guy that love music",
                           "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                           "https://www.youtube.com/watch?v=3PsUJFEBC74")
movies=[schoolofrock,Frequencies,avatar,toy_story]
fresh_tomatoes.open_movies_page(movies)
#print avatar.storyline
#Frequencies.show_trailer()
