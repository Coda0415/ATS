import sqlite3
import pandas as pd

# read in the csv file and store it as a dataframe
dfJobMasterList = pd.read_csv('Jobs Report 4.3.23 - Jobs Report 4.3.23 (1).csv')

# add an "id" column and use it as the primary key
dfJobMasterList.insert(0, 'id', range(1, 1 + len(dfJobMasterList)))
dfJobMasterList.set_index('id', inplace=True)

# rename the 'Tier5_Description' column to 'BusinessSegment'
dfJobMasterList = dfJobMasterList.rename(columns={
    'Tier5_Description': 'BusinessSegment',
    'LocationDescription': 'Region',
    'JobAddress1': 'JobAddress',
    'JobDescription': 'JobName'
})

# filter out inactive managers
dfRegionalManager = dfJobMasterList[dfJobMasterList['RegionalManager'] != 'inactive']

# select relevant columns
dfRegionalManager = dfRegionalManager[['RegionalManager', 'Region']]

# Connect to the database
conn = sqlite3.connect('frantz.db')
c = conn.cursor()

# Create the RegionalManagerMasterList table
c.execute('''CREATE TABLE RegionalManagerMasterList
             (id INTEGER PRIMARY KEY,
             RegionalManager TEXT,
             Region TEXT,
             ManagerEmail TEXT)''')

# Find all unique RegionalManagers in dfJobMasterList
regional_managers = dfJobMasterList[dfJobMasterList['RegionalManager'] != 'Inactive']['RegionalManager'].unique()

# Define a function to create the manager's email
def create_email(name):
    first_initial = name[0]
    last_name = name.split()[-1]
    email = first_initial + last_name + '@frantzbuilding.com'
    return email

# Iterate through the regional_managers list and add them to the table
for manager in regional_managers:
    region = dfJobMasterList[dfJobMasterList['RegionalManager'] == manager]['Region'].iloc[0]
    email = create_email(manager)
    c.execute("INSERT INTO RegionalManagerMasterList (RegionalManager, Region, ManagerEmail) VALUES (?, ?, ?)", (manager, region, email))

# Commit changes and close connection
conn.commit()
conn.close()
