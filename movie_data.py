# Importing required modules
import website
import media

# Creating instances for each movie with title, release date, genre, director
# poster, trailer, and brief description.
hypernorm = media.Movie("HyperNormalisation",
                        "2016",
                        "Documentary",
                        "Adam Curtis",
                        "https://upload.wikimedia.org/wikipedia/en/5/5e/HyperNormalisation.jpg",  # N0QA
                        "https://www.youtube.com/watch?v=-fny99f8amM",
                        "Thought-provoking BBC documentary on power "
                        "and narratives in contemporary society.")

samsara = media.Movie("Samsara",
                      "2011",
                      "Documentary",
                      "Rob Fricke",
                      "https://upload.wikimedia.org/wikipedia/en/7/78/Samsara_Film_Poster.jpg",  # N0QA
                      "https://www.youtube.com/watch?v=P0xVp3N-M84",
                      "Visually stunning meditation on humankind's "
                      "simultaneous majesty and vulnerability.") 

m_mambo = media.Movie("Millennium Mambo",
                      "2001",
                      "Drama",
                      "Hou Hsiao-Hsien",
                      "https://upload.wikimedia.org/wikipedia/en/8/89/Millennium_mambo.jpg",  # N0QA
                      "https://www.youtube.com/watch?v=8ubt8JvykiQ",
                      "Taiwanese art house film about the fleeting "
                      "beauty of youth.")

short_term_12 = media.Movie("Short Term 12",
                            "2013",
                            "Drama",
                            "Destin Daniel Cretton",
                            "https://upload.wikimedia.org/wikipedia/en/b/b8/Short_Term_12.jpg",  # N0QA
                            "https://www.youtube.com/watch?v=qhS6tvSb0UQ",
                            "Heart-breaking story of a foster home's employees "
                            "and residents.")

eternal_sunshine = media.Movie("Eternal Sunshine of the Spotless Mind",
                               "2004",
                               "Drama",
                               "Michel Gondry",
                               "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_sunshine_of_the_spotless_mind_ver3.jpg",  # N0QA
                               "https://www.youtube.com/watch?v=1GiLxkDK8sI",
                               "Is love worth it? Who knows???")

totoro = media.Movie("My Neighbor Totoro",
                     "1988",
                     "Animation",
                     "Hayao Miyazaki",
                     "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg",  # N0QA
                     "https://www.youtube.com/watch?v=92a7Hj0ijLs",
                     "Adorable, feel-good cartoon about siblings in the "
                     "Japanese countryside and their mysterious friend.")

# Listing each object in an array
movies = [hypernorm, samsara, m_mambo, short_term_12, eternal_sunshine, totoro]

# Call method to generate movie page in .html
website.open_movies_page(movies)
