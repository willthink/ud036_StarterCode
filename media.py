import webbrowser


class Movie():
    """ This is the class to store movie data """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def open_trailer(self):
        webbrowser.open(self.trailer_youtube)
