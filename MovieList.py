''' Python script to add movie data...
It used the Movie Data Structure and the file 'freshtomatoes.py' file to
generate the movie website'''
import MovieDS
import fresh_tomatoes

posterPrefix = "https://upload.wikimedia.org/wikipedia/en/"
urlPrefix = "https://www.youtube.com/watch?"

# Movie: Bahubali
bahubali2_The_Conclusion = MovieDS.Movie("Baahubali 2",
                                         "Baahubali 2: The Conclusion",
                                         posterPrefix +
                                         "f/f9/Baahubali_the_Conclusion.jpg",
                                         urlPrefix+"v=G62HrubdD6o")
# Movie: Raees
raees = MovieDS.Movie("Raees",
                      "A story on a criminal Abdul Latif's life",
                      posterPrefix+"2/2b/Raees_Poster.jpg",
                      urlPrefix+"?v=J7_1MU3gDk0")

# Movie: tubelight
tubelight = MovieDS.Movie("TubeLight",
                          "Indian Hindi Period War Drama",
                          posterPrefix+"0/04/Tubelight_Poster.jpg",
                          urlPrefix+"v=PGQRNKHJwH4")

# Movie: Kaabil
kaabil = MovieDS.Movie("Kaabil",
                       "Crime Thriller Film & Love between two blind people",
                       posterPrefix+"c/ce/Kaabil_Movie_Poster.jpg",
                       urlPrefix+"v=nubDFeiUAsI")

# Movie: jollyllb2
jollyllb2 = MovieDS.Movie("Jolly LLB 2",
                          "A sequel to the 2013 film Jolly LLB",
                          posterPrefix+"4/4b/Jolly_LLB_2_first_look.jpg",
                          urlPrefix+"v=q07SQFmL4rM")

# Movie: badrinath ki dulhania
badrinath = MovieDS.Movie("Badrinath Ki Dulhania",
                          "Love story between Badri and his wife",
                          posterPrefix+"7/76/Badrinath_Ki_Dulhania_Cover.jpg",
                          urlPrefix+"v=ztX-iGlZ_Ug")

# Add all the movies to a list
movies = [bahubali2_The_Conclusion,
          raees,
          tubelight,
          kaabil,
          jollyllb2,
          badrinath]

# This function call opens a webpage of movies generated from the input, a list of movie instances.
fresh_tomatoes.open_movies_page(movies)
