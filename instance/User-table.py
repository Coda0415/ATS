import sqlite3

# Connect to the database
conn = sqlite3.connect('frantz.db')
c = conn.cursor()

# Create the User table
c.execute('''CREATE TABLE User
             (id INTEGER PRIMARY KEY,
             Username TEXT NOT NULL,
             Email TEXT NOT NULL UNIQUE,
             Password TEXT NOT NULL,
             Role TEXT NOT NULL,
             Region TEXT)''')

# Commit changes and close connection
conn.commit()
conn.close()