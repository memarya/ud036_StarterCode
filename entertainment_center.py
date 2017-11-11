import media
import fresh_tomatoes
"""Creates instances of the movie class and creates
   a list from these instances.

"""

movie1 = media.Movie("Sent Of a Woman", "https://upload.wikimedia"
                     ".org/wikipedia/en/9/91/Scent_of_a_Woman.jpg",
                     "https://www.youtube.com/watch?v=ebDO0C-RTpU")
movie2 = media.Movie("The Departed", "http://www.richardcrouse.ca//"
                     "wp-content/uploads/2013/09/departed.jpg",
                     "https://www.youtube.com/watch?v=SGWvwjZ0eDc")
movie3 = media.Movie("8 Mile",
                     "https://upload.wikimedia.org/wikipedia/en/8/"
                     "8b/Eight_mile_ver2.jpg",
                     "https://www.youtube.com/watch?v=axGVrfwm9L4")
movie4 = media.Movie("Good Will Hunting", "https://upload."
                     "wikimedia.org/wikipedia/en/b/b8/"
                     "Good_Will_Hunting_theatrical_poster.jpg",
                     "https://www.youtube.com/watch?v=QSMvyuEeIyw")
movie5 = media.Movie("Silicon Valley",
                     "http://www.gstatic.com/tv/thumb/tvbanners"
                     "/13806643/p13806643_b_v8_aa.jpg",
                     "https://www.youtube.com/watch?v=69V__a49xtw")
movies = [movie1, movie2, movie3, movie4, movie5]

fresh_tomatoes.open_movies_page(movies)
