from sqliteConnect import *
import readData
from time import sleep


def delFilm():
    idField = input("Enter ID of song you wish to remove: ")
    readData.getFilm(idField)

    confirm = input("Are you sure you wish to remove the above song? (Y/N) ")
    if confirm.upper() == "Y":
        cursor.execute(f"DELETE FROM tblFilms where filmID = {idField}")

        conn.commit()
        print(f"Record {idField} deleted from the table")

    else:
        print("Action has been cancelled.")
    sleep(3)
    readData.readFilms()
