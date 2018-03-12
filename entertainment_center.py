import media
import fresh_tomatoes
import csv

film_list = []


def get_films_from_csv():
    with open("FilmList.csv") as film_file:
        csv_entries = csv.DictReader(film_file)
        for film in csv_entries:
            film_list.append(media.Movie(film.get("title"), film.get("tagline"),
                                         film.get("poster"),
                                         film.get("trailer")))

get_films_from_csv()
fresh_tomatoes.open_movies_page(film_list)
