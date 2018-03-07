import movie
import fresh_tomatoes
naruto_the_last=movie.Movie("Naruto The Last",
                            "A story of a boy that was nothing and made it to the top and then fell in love with hinata",
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/TheLastNarutomovie.jpg",
                            "https://www.youtube.com/watch?v=CZjKC66dR0Y")

maze_runner=movie.Movie("The Maze Runner",
                        "a group of people that got lost :)",
                        "https://upload.wikimedia.org/wikipedia/en/b/be/The_Maze_Runner_poster.jpg",
                        "https://www.youtube.com/watch?v=K1In45K0DGc")
the_disaster_artist=movie.Movie("The Disaster Artist",
                                "a weirdo",
                                "https://upload.wikimedia.org/wikipedia/en/c/c9/TheDisastorArtistTeaserPoster.jpg",
                                "https://www.youtube.com/watch?v=cMKX2tE5Luk&list=PLrn4UdEflPogvjjjH6CpZcyWtboB-Kwy_&t=0s&index=5")
iron_man=movie.Movie("IronMan",
                     "a man that made an iron suit",
                     "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                     "https://www.youtube.com/watch?v=8hYlB38asDY")
movies=[naruto_the_last,maze_runner,the_disaster_artist,iron_man]
fresh_tomatoes.open_movies_page(movies)
                                
                        
                    
                                
