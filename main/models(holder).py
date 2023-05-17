from flask_login import UserMixin
from . import db

class AccountManagerMasterList(db.Model):
    __tablename__ = 'AccountManagerMasterList'
    id = db.Column(db.INTEGER, nullable=False, primary_key=True)
    AccountManager = db.Column(db.TEXT, nullable=False)
    Region = db.Column(db.TEXT, nullable=False)
    RegionalManager = db.Column(db.TEXT, nullable=False)
    ManagerEmail = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<AccountManagerMasterList {self.id}>'


class Evansville(db.Model):
    id = db.Column(db.INTEGER, nullable=False, primary_key=True)
    JobNumber = db.Column(db.INT, nullable=False)
    JobName = db.Column(db.TEXT, nullable=False)
    JobAddress = db.Column(db.TEXT, nullable=False)
    JobCity = db.Column(db.TEXT, nullable=False)
    JobState = db.Column(db.TEXT, nullable=False)
    JobZip = db.Column(db.TEXT, nullable=False)
    BusinessSegment = db.Column(db.TEXT, nullable=False)
    RegionalManager = db.Column(db.TEXT, nullable=False)
    AccountManager = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Evansville {self.id}>'

class BowlingGreen(db.Model):
    id = db.Column(db.INTEGER, nullable=False, primary_key=True)
    JobNumber = db.Column(db.INT, nullable=False)
    JobName = db.Column(db.TEXT, nullable=False)
    JobAddress = db.Column(db.TEXT, nullable=False)
    JobCity = db.Column(db.TEXT, nullable=False)
    JobState = db.Column(db.TEXT, nullable=False)
    JobZip = db.Column(db.TEXT, nullable=False)
    BusinessSegment = db.Column(db.TEXT, nullable=False)
    RegionalManager = db.Column(db.TEXT, nullable=False)
    AccountManager = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<BowlingGreen {self.id}>'

class Elizabethtown(db.Model):
    id = db.Column(db.INTEGER, nullable=False, primary_key=True)
    JobNumber = db.Column(db.INT, nullable=False)
    JobName = db.Column(db.TEXT, nullable=False)
    JobAddress = db.Column(db.TEXT, nullable=False)
    JobCity = db.Column(db.TEXT, nullable=False)
    JobState = db.Column(db.TEXT, nullable=False)
    JobZip = db.Column(db.TEXT, nullable=False)
    BusinessSegment = db.Column(db.TEXT, nullable=False)
    RegionalManager = db.Column(db.TEXT, nullable=False)
    AccountManager = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Elizabethtown {self.id}>'

class Bloomington(db.Model):
    id = db.Column(db.INTEGER, nullable=False, primary_key=True)
    JobNumber = db.Column(db.INT, nullable=False)
    JobName = db.Column(db.TEXT, nullable=False)
    JobAddress = db.Column(db.TEXT, nullable=False)
    JobCity = db.Column(db.TEXT, nullable=False)
    JobState = db.Column(db.TEXT, nullable=False)
    JobZip = db.Column(db.TEXT, nullable=False)
    BusinessSegment = db.Column(db.TEXT, nullable=False)
    RegionalManager = db.Column(db.TEXT, nullable=False)
    AccountManager = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Bloomington {self.id}>'

class Clarksville(db.Model):
    id = db.Column(db.INTEGER, nullable=False, primary_key=True)
    JobNumber = db.Column(db.INT, nullable=False)
    JobName = db.Column(db.TEXT, nullable=False)
    JobAddress = db.Column(db.TEXT, nullable=False)
    JobCity = db.Column(db.TEXT, nullable=False)
    JobState = db.Column(db.TEXT, nullable=False)
    JobZip = db.Column(db.TEXT, nullable=False)
    BusinessSegment = db.Column(db.TEXT, nullable=False)
    RegionalManager = db.Column(db.TEXT, nullable=False)
    AccountManager = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Clarksville {self.id}>'

class RegionalManagerMasterList(db.Model):
    __tablename__ = 'RegionalManagerMasterList'
    id = db.Column(db.INTEGER, nullable=False, primary_key=True)
    RegionalManager = db.Column(db.TEXT, nullable=False)
    Region = db.Column(db.TEXT, nullable=False)
    ManagerEmail = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<RegionalManagerMasterList {self.id}>'


class User(UserMixin, db.Model):
    id = db.Column(db.INTEGER, nullable=False, primary_key=True)
    Username = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False, unique=True)
    Password = db.Column(db.String(100), nullable=False)
    Role = db.Column(db.String(100), nullable=False)
    Region = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<User {self.id}>'

    @staticmethod
    def load_user(user_id):
        return User.query.get(int(user_id))

    def set_password(self, password):
        self.Password = generate_password_hash(password, method='sha256')

class JobMasterList(db.Model):
    __tablename__ = 'JobMasterList'
    id = db.Column(db.Integer, primary_key=True)
    JobNumber = db.Column(db.String, nullable=False)
    JobName = db.Column(db.String, nullable=False)
    JobAddress = db.Column(db.String, nullable=False)
    JobCity = db.Column(db.String, nullable=False)
    JobState = db.Column(db.String, nullable=False)
    JobZip = db.Column(db.String, nullable=False)
    BusinessSegment = db.Column(db.String, nullable=False)
    RegionalManager = db.Column(db.String, nullable=False)
    AccountManager = db.Column(db.String, nullable=False)
    Region = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f"<JobMasterList(JobNumber={self.JobNumber}, JobName={self.JobName}, JobAddress={self.JobAddress}, JobCity={self.JobCity}, JobState={self.JobState}, JobZip={self.JobZip}, BusinessSegment={self.BusinessSegment}, RegionalManager={self.RegionalManager}, AccountManager={self.AccountManager}, Region={self.Region})>"

class OpenPositionsRoster(db.Model):
    __tablename__ = 'OpenPositionsRoster'
    PositionID = db.Column(db.String, nullable=False,primary_key=True)
    JobNumber = db.Column(db.String, nullable=False)
    JobTitle = db.Column(db.String, nullable=False)
    EmploymentType = db.Column(db.String, nullable=False)
    Wage = db.Column(db.String, nullable=False)
    BusinessSegment = db.Column(db.String, nullable=False)
    JobCity = db.Column(db.String, nullable=False)
    JobDescription = db.Column(db.String, nullable=False)
    JobZip = db.Column(db.String, nullable=False)
    Region = db.Column(db.String, nullable=False)
    AccountManager = db.Column(db.String, nullable=False)
    RegionalManager = db.Column(db.String, nullable=False)
    Shift = db.Column(db.String, nullable=False)
    SpecialInstructions = db.Column(db.String, nullable=True)
    WorkDays = db.Column(db.String, nullable=False)
    StartTime = db.Column(db.String, nullable=False)
    EndTime = db.Column(db.String, nullable=False)
    FlexTime = db.Column(db.String, nullable=True)
    SobAmount = db.Column(db.String, nullable=True)
    SobDays = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<OpenPositionsRoster(PositionID={self.PositionID}, JobNumber={self.JobNumber}, JobTitle={self.JobTitle}, EmploymentType={self.EmploymentType}, Wage={self.Wage}, BusinessSegment={self.BusinessSegment}, JobCity={self.JobCity}, JobDescription={self.JobDescription}, JobZip={self.JobZip}, Region={self.Region}, AccountManager={self.AccountManager}, RegionalManager={self.RegionalManager}, Shift={self.Shift}, SpecialInstructions={self.SpecialInstructions}, WorkDays={self.WorkDays}, StartTime={self.StartTime}, EndTime={self.EndTime}, FlexTime={self.FlexTime}, SobAmount={self.SobAmount}, SobDays={self.SobDays})>"
