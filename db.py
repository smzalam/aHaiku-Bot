import sqlite3

#Create a database
conn = sqlite3.connect('ahaiku.db')

#Create a cursor
cursor = conn.cursor()

#Create a table
#only five datatyoes: NULL, INTEGER, REAL, TEXT, BLOB
cursor.execute("""CREATE TABLE rules (
    position integer,
    rule text
)""")


conn.commit()

conn.close()