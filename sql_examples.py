import sqlite3


# Establish connection
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query data based on a condition
cursor.execute("Select * from events where date = '2088.10.24'")
rows = cursor.fetchall()
print(rows)

# Query certain columns based on a condition
cursor.execute("Select band, city from events where date = '2088.10.24'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Cats', 'Cat city', '2088.10.15'),
            ('Hens', 'Hen city', '2088.10.15')]
cursor.executemany("Insert into events values(?, ?, ?)", new_rows)
connection.commit()

# Query every rows
cursor.execute("select * from events")
rows = cursor.fetchall()
print(rows)
