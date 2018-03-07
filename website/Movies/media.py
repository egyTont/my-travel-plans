import webbrowser
class Movie():
    VALID_RATINGS=["G","PG","PG-13","R"]
    def __init__(omk,movie_title,movie_storyline,poster_image,trailer_youtube):
        omk.title=movie_title
        omk.storyline=movie_storyline
        omk.poster_image_url=poster_image
        omk.trailer_youtube_url=trailer_youtube
    def show_trailer(omk):
        webbrowser.open(omk.trailer_youtube_url)
        
