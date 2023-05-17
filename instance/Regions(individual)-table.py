import sqlite3
import pandas as pd

# Read in the csv file and store it as a dataframe
dfJobMasterList = pd.read_csv('Jobs Report 4.3.23 - Jobs Report 4.3.23 (1).csv')

# Rename the 'Tier5_Description' column to 'BusinessSegment'
dfJobMasterList = dfJobMasterList.rename(columns={'Tier5_Description': 'BusinessSegment',
                                                  'LocationDescription': 'Region',
                                                  'JobAddress1': 'JobAddress',
                                                  'JobDescription': 'JobName'})

# Create a dictionary to map full region names to shorter table names
region_table_names = {
    'Evansville Region': 'Evansville',
    'Bowling Green Region': 'BowlingGreen',
    'Elizabethtown Region': 'Elizabethtown',
    'Bloomington Region': 'Bloomington',
    'Clarksville Region': 'Clarksville'
}

# Connect to the database
conn = sqlite3.connect('frantz.db')
c = conn.cursor()

# Create a table for each region
for full_region_name, table_name in region_table_names.items():
    # Select only the rows for the current region
    df_region = dfJobMasterList[dfJobMasterList['Region'] == full_region_name]

    # Create the table with the appropriate columns
    c.execute(f"CREATE TABLE {table_name} \
               (id INTEGER PRIMARY KEY, \
               JobNumber INT, \
               JobName TEXT, \
               JobAddress TEXT, \
               JobCity TEXT, \
               JobState TEXT, \
               JobZip TEXT, \
               BusinessSegment TEXT, \
               RegionalManager TEXT, \
               AccountManager TEXT)")

    # Insert the data from the data frame into the table
    for index, row in df_region.iterrows():
        c.execute(f"INSERT INTO {table_name} \
                   (JobNumber, JobName, JobAddress, JobCity, JobState, JobZip, \
                   BusinessSegment, RegionalManager, AccountManager) \
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                  (row['JobNumber'],
                   row['JobName'],
                   row['JobAddress'],
                   row['JobCity'],
                   row['JobState'],
                   row['JobZip'],
                   row['BusinessSegment'],
                   row['RegionalManager'],
                   row['AccountManager']))

# Commit changes and close connection
conn.commit()
conn.close()
