import webbrowser
class Movie() :
    "Movie"

    def __init__(self,movie_title,movie_storyline,movie_poster,movie_trailer) :
         self.title=movie_title
         self.story=movie_storyline
         self.poster_image_url=movie_poster
         self.trailer_youtube_url=movie_trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
