import media
import fresh_tomatoes
import csv

def get_films_from_csv():
    film_file = csv.reader("FilmList.csv")
    for row in film_file:
        print(film_file)

black_cat_white_cat = media.Movie("Black Cat White Cat",
                                  "Grandad's resurrection helps love prevail",
                                  "https://upload.wikimedia.org/wikipedia/en/6/6f/Black_Cat%2C_White_Cat_poster.jpg",
                                  "https://www.youtube.com/watch?v=tt4EVvCmhvs")

the_godfather = media.Movie("The Godfather",
                            "Where the mafia makes offers no one can refuse",
                            "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                            "https://www.youtube.com/watch?v=5DO-nDW43Ik")

pi = media.Movie("Pi",
                 "To make sense, drill a hole in your head",
                 "https://upload.wikimedia.org/wikipedia/en/5/5a/Piposter.jpg",
                 "https://www.youtube.com/watch?v=r0SC582sJvE")

the_believer = media.Movie("The Believer",
                           "The story of a Jewish klu klux klan leader",
                           "https://upload.wikimedia.org/wikipedia/en/7/78/Believerposter.jpg",
                           "https://www.youtube.com/watch?v=mzDCptEBvq4")

beverly_hills_cop = media.Movie("Beverly Hills Cop",
                                "Only the first one was good, but it was great",
                                "https://upload.wikimedia.org/wikipedia/en/a/a2/Beverly_Hills_Cop.jpg",
                                "https://www.youtube.com/watch?v=3NoSLJOViDE")

favourite_films = [black_cat_white_cat, the_godfather, pi, the_believer, beverly_hills_cop]

get_films_from_csv()
# fresh_tomatoes.open_movies_page(favourite_films)
