from sqliteConnect import *
from time import sleep


def readFilms():
    cursor.execute("SELECT * FROM tblFilms")
    row = (cursor.fetchall())
    for record in row:
        print(record)


def getFilm(id):
    cursor.execute(f"SELECT * FROM tblFilms where filmID = {id}")
    print(cursor.fetchall())


def searchOptions():
    option = 0
    while option not in ["1", "2", "3", ""]:
        print("Search Menu options \nEnter \n1. Genre \n2. Year. \n3. Rating.")

        options = input(
            "Enter one of the options listed above (Press Enter to exit): ")

        if options not in ["1", "2", "3", ""]:
            print("please enter one of the options")

        return options


def searchFilm():
    searchMenu = searchOptions()
    searchTerm = input("Please enter the search term: ")

    if searchMenu == "1":
        selField = "genre"
        searchTerm = searchTerm.title()
    elif searchMenu == "2":
        selField = "yearReleased"
    elif searchMenu == "3":
        selField = "rating"
        searchTerm = searchTerm.upper()
    elif searchMenu == "":
        return

    cursor.execute(
        f"SELECT * FROM tblFilms where {selField} = \"{searchTerm}\"")
    row = (cursor.fetchall())

    if (len(row) == 0):
        print("Nothing has been found, please check your search term and try again")
        searchFilm()
    else:
        print(f"{len(row)} record(s) returned")
        for record in row:
            print(record)

    sleep(3)
