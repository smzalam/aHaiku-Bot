import sqlite3
from funcs import getting_pos, getting_rules

#Create a database
conn = sqlite3.connect('821555368999780352.db')

#Create a cursor
cursor = conn.cursor()

cursor.execute("SELECT * FROM rules")
result = cursor.fetchall()

print(result)

pos = getting_pos(result)
rules = getting_rules(result)

print(pos)
print(rules)



print("committed successfully")

conn.commit()

conn.close()