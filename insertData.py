from sqliteConnect import *
from readData import *
from time import sleep


def addFilm():
    film = []

    filmName = input("Please input the film name: ")
    yearReleased = int(input("Please input the film year released: "))
    filmRating = input("Please input the film age rating: ")
    filmDuration = int(input("Please input the film duration(in minutes): "))
    filmGenre = input("Please input the film genre: ")

    film.append(filmName)
    film.append(yearReleased)
    film.append(filmRating)
    film.append(filmDuration)
    film.append(filmGenre)

    cursor.execute(
        f"INSERT INTO tblFilms VALUES(null, ?, ?, ?, ?, ?)", film)

    conn.commit()
    print(f"{filmName} added to the songs table")
    sleep(3)
