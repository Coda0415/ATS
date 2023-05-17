import sqlite3
import csv
import psycopg2

# Connect to the SQLite database
sqlite_conn = sqlite3.connect('/Users/colindavis/PycharmProjects/ATS/instance/frantz.db')
sqlite_cursor = sqlite_conn.cursor()

# Execute a SELECT statement on the EmployeeMasterList table and fetch all rows
sqlite_cursor.execute('SELECT * FROM EmployeeMasterList')
rows = sqlite_cursor.fetchall()

# Write the data to a CSV file
with open('EmployeeMasterList.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([desc[0] for desc in sqlite_cursor.description])  # Write the header
    writer.writerows(rows)

# Close the SQLite connection
sqlite_conn.close()

# Connect to the PostgreSQL database
postgres_conn = psycopg2.connect(database='frantz', user='coda415', password='Qwerty415!', host='localhost')
postgres_cursor = postgres_conn.cursor()

# Drop the existing EmployeeMasterList table if it exists
postgres_cursor.execute("DROP TABLE IF EXISTS employeemasterlist")


# Create the EmployeeMasterList table in PostgreSQL if it doesn't exist
postgres_cursor.execute('''
    CREATE TABLE employeemasterlist
             (id INTEGER PRIMARY KEY,
             employeenumber INTEGER,
             firstname TEXT,
             lastname TEXT,
             hiredate TEXT,
             classificationdescription TEXT,
             employeetypedescription TEXT,
             supervisordescription TEXT,
             jobnumber TEXT,
             jobname TEXT,
             categorydescription TEXT,
             region TEXT,
             title TEXT,
             jobstate TEXT,
             companyaddress2 TEXT,
             uctaxpayeridnumber TEXT,
             jobaddress TEXT,
             jobaddress2 TEXT,
             jobcity TEXT,
             jobzip TEXT,
             employmenttype TEXT)
''')
postgres_conn.commit()

# Load the data from the CSV file into the PostgreSQL database
with open('EmployeeMasterList.csv', 'r') as csvfile:
    # Skip the header row
    next(csvfile)
    postgres_cursor.copy_expert("COPY EmployeeMasterList(id,EmployeeNumber,FirstName,LastName,HireDate,ClassificationDescription,EmployeeTypeDescription,SupervisorDescription,JobNumber,JobName,CategoryDescription,Region,Title,JobState,CompanyAddress2,UCTaxPayerIDNumber,JobAddress,JobAddress2,JobCity,JobZip,EmploymentType) FROM STDIN WITH CSV", csvfile)

postgres_conn.commit()

# Close the PostgreSQL connection
postgres_cursor.close()
postgres_conn.close()
