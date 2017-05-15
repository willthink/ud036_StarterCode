import webbrowser


class Movie():
    """ This is the class to store movie data """

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
    	"""
    	initialize a Movie instance 

    	Args: 
    	     movie_title: title string of the movie
    	     poster_image_url: a url string to the poster image of the movie
    	     trailer_youtube_url: a url string to the youtube trailer of the movie 

    	Returns: 
    	        An instance of the Movie class
    	"""
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
