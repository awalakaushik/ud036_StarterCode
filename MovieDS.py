import webbrowser


class Movie():
    ''' Movie class that creates a movie object '''
    def __init__(self, movieTitle, movieTagline, posterImage, trailerYoutube):
        self.title = movieTitle
        self.storyline = movieTagline
        self.poster_image_url = posterImage
        self.trailer_youtube_url = trailerYoutube

    def show_trailer(self):
        ''' show_trailer() shows the movie trailer'''
        webbrowser.open(self.trailer_youtube_url)
