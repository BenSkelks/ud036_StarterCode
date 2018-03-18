import webbrowser


class Movie():
    """Class for storing movie information"""

    VALID_PARENTAL_GUIDANCE = ["PG", "PG-13", "R", "U", "15", "18"]

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, movie_parental_guidance):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        if movie_parental_guidance is None:
            self.parental_guidance = "Not Fit For Human Consumption"
        else:
            self.parental_guidance = movie_parental_guidance


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
