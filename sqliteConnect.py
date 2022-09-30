import sqlite3  # import the sqlite module/library

conn = sqlite3.connect("filmflix.db")

cursor = conn.cursor()
