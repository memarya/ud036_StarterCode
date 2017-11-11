# ud036_StarterCode
Source code for a Movie Trailer website.
In addition to the master, this repository contains 'externa-data' branch which uses external text file to store each movie's information.
A new favorite movie can be added without modifying the code by simply adding the movie information to the movies.txt file. The title of the movie, the URL link of the poster image, and the URL link of the trailer youtube video should be added to a new line and separated by a comma. This presents a potential problem in cases where there is a comma as part of a string. This problem will be addressed in future updates. Potential solutions include:
-	Change the format of the content of movies.txt such as separating title, image, and trailer video using pipe or new line
-	Use better splitting method, such as implementation of regex
