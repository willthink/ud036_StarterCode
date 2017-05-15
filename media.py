import webbrowser


class Movie():
    """ This is the class to store movie data """

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def open_trailer(self):
        webbrowser.open(self.trailer_youtube)
