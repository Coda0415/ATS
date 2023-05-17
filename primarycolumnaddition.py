import sqlite3
import json
import base64

# Connect to the database and create a cursor object
conn = sqlite3.connect('instance/frantz.db')
cursor = conn.cursor()

# Get the schema of the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
table_names = [row[0] for row in cursor.fetchall()]
schema = {}
for table_name in table_names:
    cursor.execute(f"PRAGMA table_info(\"{table_name}\")")
    columns = [column[1] for column in cursor.fetchall()]
    columns.insert(0, "id INTEGER PRIMARY KEY AUTOINCREMENT")
    schema[table_name] = columns

# Dump the schema to a JSON file
with open('frantz.json', 'w') as f:
    json.dump(schema, f)

# Dump the data to a JSON file
data = {}
for table_name in table_names:
    cursor.execute(f"SELECT * FROM \"{table_name}\"")
    rows = cursor.fetchall()
    encoded_rows = []
    for row in rows:
        encoded_row = []
        for col in row:
            if isinstance(col, bytes):
                encoded_row.append(base64.b64encode(col).decode())
            else:
                encoded_row.append(col)
        encoded_rows.append(encoded_row)
    data[table_name] = encoded_rows

    # Add a NULL value for the new primary key column
    for i in range(len(data[table_name])):
        data[table_name][i].insert(0, None)

with open('frantz_data.json', 'w') as f:
    json.dump(data, f)

# Close the database connection
conn.close()

# Read the JSON files and create a new database
with open('frantz.json', 'r') as f:
    schema = json.load(f)

with open('frantz_data.json', 'r') as f:
    data = json.load(f)

conn = sqlite3.connect('instance/frantz.db')
cursor = conn.cursor()

# Create the tables in the new database
for table_name, columns in schema.items():
    column_names = ['\"{}\"'.format(col) for col in columns]
    create_statement = "CREATE TABLE \"{table}\" ({columns})".format(table=table_name, columns=','.join(column_names))
    cursor.execute(create_statement)

# Insert the data into the new database
for table_name, rows in data.items():
    for row in rows:
        decoded_row = []
        for col in row:
            if isinstance(col, str):
                try:
                    decoded_col = base64.b64decode(col)
                except:
                    decoded_col = col
            else:
                decoded_col = col
            decoded_row.append(decoded_col)
        placeholders = ','.join(['?' for _ in decoded_row])
        insert_statement = "INSERT INTO \"{table}\" VALUES ({placeholders})".format(table=table_name, placeholders=placeholders)
        cursor.execute(insert_statement, decoded_row)

# Commit the changes and close the database connection
conn.commit()
conn.close()
