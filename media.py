class Movie():
	"""Movie class provides a data structure for storing movie information.
    
    Attributes:
        movie_title: Movie title.
        poster_image_url: A link to the movie poster image.
        trailer_youtube_url: A youtube link to the movie trailer
    """
	def __init__(self, movie_title, poster_image_url, trailer_youtube_url):
		self.title = movie_title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
