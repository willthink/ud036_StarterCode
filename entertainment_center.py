from media import Movie
import fresh_tomatoes

avengers3 = Movie("Avengers 3",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BOGQ5NTY3NjktYjIzNS00Y2ZjLWIyODQtMjQzYzg1ZTMzOGI5XkEyXkFqcGdeQXVyNDMwMzEyNzA@._V1_.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=pfQeLSDX4DQ")

forrest_gump = Movie("Forrest Gump", 
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=bLvqoHBptjg")

shaw_red = Movie("Shawshank Redemption",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=6hB3S9bIaco")

dark_knight = Movie("The Dark Knight",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

start_wars = Movie("Star Wars: Episode V - The Empire Strikes Back",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BYmViY2M2MTYtY2MzOS00YjQ1LWIzYmEtOTBiNjhlMGM0NjZjXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,644,1000_AL_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

back_future = Movie("Back to the Future",
                          "https://images-na.ssl-images-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,643,1000_AL_.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=qvsgGtivCgs")
help(Movie.__init__)

# add movie instances into array of movies
movies = [forrest_gump, shaw_red, avengers3,
          dark_knight, start_wars, back_future]

# create html page
fresh_tomatoes.open_movies_page(movies)