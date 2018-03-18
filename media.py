import webbrowser


class Movie():
    """Class for storing movie information"""

    VALID_PARENTAL_GUIDANCE = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, parental_guidance=None):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        if parental_guidance is None:
            parental_guidance = "NOT FIT FOR HUMAN CONSUMPTION"
        self.parental_guidance= parental_guidance

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
