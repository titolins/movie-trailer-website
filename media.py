class Movie():
    """ movie class created for the movie trailer website project at full stack
    web developer nano degree from udacity.

    """

    def __init__(self, movie_title, poster_image, trailer_youtube):
        """movie class constructor

        each movie has a title, a url to a poster image and a url to a trailer
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
