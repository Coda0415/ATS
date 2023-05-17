import sqlite3
import pandas as pd

# Read in the csv file and store it as a dataframe
dfJobMasterList = pd.read_csv('Jobs Report 4.3.23 - Jobs Report 4.3.23 (1).csv')

# Rename the 'Tier5_Description' column to 'BusinessSegment'
dfJobMasterList = dfJobMasterList.rename(columns={'Tier5_Description': 'BusinessSegment',
                        'LocationDescription': 'Region',
                        'JobAddress1': 'JobAddress',
                        'JobDescription': 'JobName'})

# Filter out inactive account managers
dfAccountManager = dfJobMasterList[dfJobMasterList['AccountManager'] != 'inactive']

# Select relevant columns
dfAccountManager = dfAccountManager[['AccountManager', 'Region', 'RegionalManager']]

# Connect to the database
conn = sqlite3.connect('frantz.db')
c = conn.cursor()

# Create the AccountManagerMasterList table
c.execute('''CREATE TABLE AccountManagerMasterList
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             AccountManager TEXT,
             Region TEXT,
             RegionalManager TEXT,
             ManagerEmail TEXT)''')

# Find all unique account managers in dfJobMasterList
account_managers = dfJobMasterList[dfJobMasterList['AccountManager'] != 'Inactive']['AccountManager'].unique()

# Define a function to create the manager's email
def create_email(name):
    first_initial = name[0]
    last_name = name.split()[-1]
    email = first_initial + last_name + '@frantzbuilding.com'
    return email

# Iterate through the account_managers list and add them to the table
for manager in account_managers:
    region = dfJobMasterList[dfJobMasterList['AccountManager'] == manager]['Region'].iloc[0]
    regional_manager = dfJobMasterList[dfJobMasterList['AccountManager'] == manager]['RegionalManager'].iloc[0]
    email = create_email(manager)
    c.execute("INSERT INTO AccountManagerMasterList (AccountManager, Region, RegionalManager, ManagerEmail) VALUES (?, ?, ?, ?)", (manager, region, regional_manager, email))

# Commit changes and close connection
conn.commit()
conn.close()
