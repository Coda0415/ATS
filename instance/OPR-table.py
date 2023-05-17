import sqlite3

def create_open_positions_roster_table():
    conn = sqlite3.connect('frantz.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS openPositionsRoster (
            PositionID TEXT PRIMARY KEY,
            JobNumber TEXT,
            JobTitle TEXT,
            EmploymentType TEXT,
            Wage REAL,
            BusinessSegment TEXT,
            JobCity TEXT,
            JobDescription TEXT,
            JobZip INTEGER,
            Region TEXT,
            AccountManager TEXT,
            RegionalManager TEXT,
            Shift INTEGER,
            SpecialInstructions TEXT,
            WorkDays TEXT,
            StartTime TEXT,
            EndTime TEXT,
            FlexTime REAL,
            SobAmount REAL,
            SobDays TEXT
        )
    ''')

    conn.commit()
    conn.close()

create_open_positions_roster_table()
