import pandas as pd
import sqlite3

# read in the csv files and store them as dataframes
dfJobMasterList = pd.read_csv('Jobs Report 4.3.23 - Jobs Report 4.3.23 (1).csv')
dfEmployeeMasterList = pd.read_csv('HR Report Employee Master 3.31.23 - HR Report Employee Master 3.31.23.csv (2).csv')

dfEmployeeMasterList = dfEmployeeMasterList.rename(columns={'PrimaryJob': 'JobNumber',
                        'LocationDescription': 'Region',
                        'FTPT_IDDesc': 'EmploymentType',
                        'JobAddress1': 'JobAddress',
                        'JobDescription': 'JobName'})

dfJobMasterList = dfJobMasterList.rename(columns={'Tier5_Description': 'BusinessSegment',
                        'LocationDescription': 'Region',
                        'JobAddress1': 'JobAddress',
                        'JobDescription': 'JobName'})


# get all the unique JobNumber values
unique_job_numbers = dfEmployeeMasterList["JobNumber"].unique()

# create a connection to the SQLite database
conn = sqlite3.connect("frantz.db")

# create the JobMasterList table
cursor = conn.cursor()
cursor.execute("""CREATE TABLE JobMasterList (
                    id INTEGER PRIMARY KEY,
                    JobNumber TEXT,
                    JobName TEXT,
                    JobAddress TEXT,
                    JobCity TEXT,
                    JobState TEXT,
                    JobZip TEXT,
                    BusinessSegment TEXT,
                    RegionalManager TEXT,
                    AccountManager TEXT,
                    Region TEXT
                )""")

# iterate through the unique JobNumber values and insert the relevant records into the JobMasterList table
for job_number in unique_job_numbers:
    df_job = dfJobMasterList[dfJobMasterList["JobNumber"] == job_number]
    if not df_job.empty:
        job_description = df_job["JobName"].iloc[0]
        job_address = df_job["JobAddress"].iloc[0]
        job_city = df_job["JobCity"].iloc[0]
        job_state = df_job["JobState"].iloc[0]
        job_zip = df_job["JobZip"].iloc[0]
        business_segment = df_job["BusinessSegment"].iloc[0]
        regional_manager = df_job["RegionalManager"].iloc[0]
        account_manager = df_job["AccountManager"].iloc[0]
        region = df_job["Region"].iloc[0]

        cursor.execute(f"""INSERT INTO JobMasterList (JobNumber, JobName, JobAddress, JobCity, JobState, JobZip, BusinessSegment, RegionalManager, AccountManager, Region)
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (job_number, job_description, job_address, job_city, job_state, job_zip, business_segment,
                        regional_manager, account_manager, region))

# commit the changes to the database
conn.commit()
