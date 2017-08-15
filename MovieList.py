import MovieDS
import fresh_tomatoes

bahubali2_The_Conclusion = MovieDS.Movie("Baahubali 2",
                        "Continuation of Baahubali: The Beginning",
                        "https://upload.wikimedia.org/wikipedia/en/f/f9/Baahubali_the_Conclusion.jpg",
                        "https://www.youtube.com/watch?v=G62HrubdD6o")

raees = MovieDS.Movie("Raees",
                     "A story on a criminal Abdul Latif's life",
                     "https://upload.wikimedia.org/wikipedia/en/2/2b/Raees_Poster.jpg",
                     "https://www.youtube.com/watch?v=J7_1MU3gDk0")

tubelight = MovieDS.Movie("TubeLight",
                     "Indian Hindi Period War Drama",
                     "https://upload.wikimedia.org/wikipedia/en/0/04/Tubelight_Poster.jpg",
                     "https://www.youtube.com/watch?v=PGQRNKHJwH4")

kaabil = MovieDS.Movie("Kaabil",
                     "Crime Thriller Film & Love between two blind people",
                     "https://upload.wikimedia.org/wikipedia/en/c/ce/Kaabil_Movie_Poster.jpg",
                     "https://www.youtube.com/watch?v=nubDFeiUAsI")

jollyllb2 = MovieDS.Movie("Jolly LLB 2",
                        "A sequel to the 2013 film Jolly LLB",
                        "https://upload.wikimedia.org/wikipedia/en/4/4b/Jolly_LLB_2_first_look.jpg",
                        "https://www.youtube.com/watch?v=q07SQFmL4rM")

badrinath = MovieDS.Movie("Badrinath Ki Dulhania",
                       "Love story between Badri and his wife",
                       "https://upload.wikimedia.org/wikipedia/en/7/76/Badrinath_Ki_Dulhania_Cover.jpg",
                       "https://www.youtube.com/watch?v=ztX-iGlZ_Ug")


movies = [bahubali2_The_Conclusion,raees,tubelight,kaabil,jollyllb2,badrinath]

fresh_tomatoes.open_movies_page(movies)