# Importing webbrowser module from Python standard library
import webbrowser


class Movie():
    """This class provides a way to store movie data

    Each movie has the following attributes (all strings):
        title: Name of the film
        year: Year in which film was released
        genre: Genre of film
        director: Director of film
        art: URL of poster art
        trailer: URL to trailer
        comments: Subjective notes on each film
    """

    # Initiate objects of the class Movie
    def __init__(self,
                 title,
                 year,
                 genre,
                 director,
                 art,
                 trailer,
                 comments):
        self.title = title
        self.year = year
        self.genre = genre
        self.director = director
        self.art = art
        self.trailer = trailer
        self.comments = comments

    # Instance method to open trailer URL in web browser
    def show_trailer(self):
        webbrowser.open(self.trailer)
