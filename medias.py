import webbrowser


class Movie():

    def __init__(self, movie_title, movie_story, poster_img, trailer_youtube):
        self.title = movie_title
        self.story = movie_story
        self.poster_img_url = poster_img
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    
