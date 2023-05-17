import sqlite3
import pandas as pd

# read in the csv file and store it as a dataframe
dfEmployeeMasterList = pd.read_csv('HR Report Employee Master 3.31.23 - HR Report Employee Master 3.31.23.csv (2).csv')

# rename the columns as needed
dfEmployeeMasterList = dfEmployeeMasterList.rename(columns={'PrimaryJob': 'JobNumber',
                        'LocationDescription': 'Region',
                        'FTPT_IDDesc': 'EmploymentType',
                        'JobAddress1': 'JobAddress',
                        'JobDescription': 'JobName'})

# connect to the database and create the table
conn = sqlite3.connect('frantz.db')
c = conn.cursor()

# drop the existing table if it exists
c.execute('''DROP TABLE IF EXISTS EmployeeMasterList''')

# create the table
c.execute('''CREATE TABLE EmployeeMasterList
             (id INTEGER PRIMARY KEY,
             EmployeeNumber INTEGER,
             FirstName TEXT,
             LastName TEXT,
             HireDate TEXT,
             ClassificationDescription TEXT,
             EmployeeTypeDescription TEXT,
             SupervisorDescription TEXT,
             JobNumber INTEGER,
             JobName TEXT,
             CategoryDescription TEXT,
             Region TEXT,
             Title TEXT,
             JobState TEXT,
             CompanyAddress2 TEXT,
             UCTaxPayerIDNumber TEXT,
             JobAddress TEXT,
             JobAddress2 TEXT,
             JobCity TEXT,
             JobZip TEXT,
             EmploymentType TEXT)''')

# insert the data from the dataframe into the table
for index, row in dfEmployeeMasterList.iterrows():
    c.execute('''INSERT INTO EmployeeMasterList
                 (EmployeeNumber, FirstName, LastName, HireDate, ClassificationDescription, EmployeeTypeDescription,
                 SupervisorDescription, JobNumber, JobName, CategoryDescription, Region, Title, JobState,
                 CompanyAddress2, UCTaxPayerIDNumber, JobAddress, JobAddress2, JobCity, JobZip, EmploymentType)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (row['EmployeeNumber'], row['FirstName'], row['LastName'], row['HireDate'], row['ClassificationDescription'],
               row['EmployeeTypeDescription'], row['SupervisorDescription'], row['JobNumber'], row['JobName'],
               row['CategoryDescription'], row['Region'], row['Title'], row['JobState'], row['CompanyAddress2'],
               row['UCTaxPayerIDNumber'], row['JobAddress'], row['JobAddress2'], row['JobCity'], row['JobZip'],
               row['EmploymentType']))

# commit the changes and close the connection
conn.commit()
conn.close()
