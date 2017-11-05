import media
import fresh_tomatoes
	"""Creates instances of the movie class and creates a list from these instances.
    
    """

sent_of_a_women = media.Movie("Sent Of a Woman", "https://upload.wikimedia.org/wikipedia/en/9/91/Scent_of_a_Woman.jpg", "https://www.youtube.com/watch?v=ebDO0C-RTpU")
the_departed = media.Movie("The Departed", "http://www.richardcrouse.ca//wp-content/uploads/2013/09/departed.jpg","https://www.youtube.com/watch?v=SGWvwjZ0eDc")
eight_mile = media.Movie("8 Mile", "https://upload.wikimedia.org/wikipedia/en/8/8b/Eight_mile_ver2.jpg","https://www.youtube.com/watch?v=axGVrfwm9L4")
good_will_hunting = media.Movie("Good Will Hunting","https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg","https://www.youtube.com/watch?v=QSMvyuEeIyw")
silicon_valley = media.Movie("Silicon Valley","http://www.gstatic.com/tv/thumb/tvbanners/13806643/p13806643_b_v8_aa.jpg","https://www.youtube.com/watch?v=69V__a49xtw")
movies = [sent_of_a_women, the_departed, eight_mile, good_will_hunting, silicon_valley]

fresh_tomatoes.open_movies_page(movies)
