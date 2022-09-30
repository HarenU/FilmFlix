from sqliteConnect import *
import readData
from time import sleep


def updateFilm():
    idField = input("Enter the ID of the film to be updated: ")
    readData.getFilm(idField)
    fieldName = input(
        "Enter the field you would like to update (Title, Year, Rating, Duration, Genre): ").title()

    newFieldValue = input(f"Enter the new field value for {fieldName}: ")

    cursor.execute(
        F"UPDATE tblFilms SET {fieldName} = '{newFieldValue}' WHERE filmID = {idField}")
    conn.commit()
    print(f"Record {idField} updated in songs table")
    sleep(3)
    readData.readFilms()  # invoke the subroutine readSongs from read.py
