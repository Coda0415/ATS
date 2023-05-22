from flask_login import UserMixin
from . import db

class accountmanagermasterlist(db.Model):
    __tablename__ = 'accountmanagermasterlist'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    manageremail = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<accountmanagermasterlist {self.id}>'


class evansville(db.Model):
    __tablename__ = 'evansville'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INT, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<evansville {self.id}>'

class bowlinggreen(db.Model):
    __tablename__ = 'bowlinggreen'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INT, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bowlinggreen {self.id}>'

class elizabethtown(db.Model):
    __tablename__ = 'elizabethtown'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INT, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<elizabethtown {self.id}>'

class bloomington(db.Model):
    __tablename__ = 'bloomington'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INT, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bloomington {self.id}>'

class clarksville(db.Model):
    __tablename__ = 'clarksville'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INT, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<clarksville {self.id}>'

class regionalmanagermasterlist(db.Model):
    __tablename__ = 'regionalmanagermasterlist'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    manageremail = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<regionalmanagermasterlist {self.id}>'

class user(UserMixin, db.Model):
    id = db.Column(db.INTEGER, nullable=False, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    region = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<user {self.id}>'

    @staticmethod
    def load_user(user_id):
        return user.query.get(int(user_id))

    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')


class jobmasterlist(db.Model):
    __tablename__ = 'jobmasterlist'
    id = db.Column(db.Integer, primary_key=True)
    jobnumber = db.Column(db.String, nullable=False)
    jobname = db.Column(db.String, nullable=False)
    jobaddress = db.Column(db.String, nullable=False)
    jobcity = db.Column(db.String, nullable=False)
    jobstate = db.Column(db.String, nullable=False)
    jobzip = db.Column(db.String, nullable=False)
    businesssegment = db.Column(db.String, nullable=False)
    regionalmanager = db.Column(db.String, nullable=False)
    accountmanager = db.Column(db.String, nullable=False)
    region = db.Column(db.String, nullable=False)


    def __repr__(self):
        return f"<jobmasterlist(jobnumber={self.jobnumber}, jobname={self.jobname}, jobaddress={self.jobaddress}, jobcity={self.jobcity}, jobstate={self.jobstate}, jobzip={self.jobzip}, businesssegment={self.businesssegment}, regionalmanager={self.regionalmanager}, accountmanager={self.accountmanager}, region={self.region})>"

class openpositionsroster(db.Model):
    __tablename__ = 'openpositionsroster'
    positionid = db.Column(db.String, nullable=False,primary_key=True)
    jobnumber = db.Column(db.String, nullable=False)
    jobtitle = db.Column(db.String, nullable=False)
    employmenttype = db.Column(db.String, nullable=False)
    wage = db.Column(db.String, nullable=False)
    businesssegment = db.Column(db.String, nullable=False)
    jobcity = db.Column(db.String, nullable=False)
    jobdescription = db.Column(db.String, nullable=False)
    jobzip = db.Column(db.String, nullable=False)
    region = db.Column(db.String, nullable=False)
    accountmanager = db.Column(db.String, nullable=False)
    regionalmanager = db.Column(db.String, nullable=False)
    shift = db.Column(db.String, nullable=False)
    specialinstructions = db.Column(db.String, nullable=True)
    workdays = db.Column(db.String, nullable=False)
    starttime = db.Column(db.String, nullable=False)
    endtime = db.Column(db.String, nullable=False)
    flextime = db.Column(db.String, nullable=True)
    sobamount = db.Column(db.String, nullable=True)
    sobdays = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<openpositionsroster(positionid={self.positionid}, jobnumber={self.jobnumber}, jobtitle={self.jobtitle}, employmenttype={self.employmenttype}, wage={self.wage}, businesssegment={self.businesssegment}, jobcity={self.jobcity}, jobdescription={self.jobdescription}, jobzip={self.jobzip}, region={self.region}, accountmanager={self.accountmanager}, regionalmanager={self.regionalmanager}, shift={self.shift}, specialinstructions={self.specialinstructions}, workdays={self.workdays}, starttime={self.starttime}, endtime={self.endtime}, flextime={self.flextime}, sobamount={self.sobamount}, sobdays={self.sobdays})>"


class employeemasterlist(db.Model):
    __tablename__ = 'employeemasterlist'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<employeemasterlist {self.id}>'

class _3M(db.Model):
    __tablename__ = '_3M'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<_3M {self.id}>'

class aaMMetalforming(db.Model):
    __tablename__ = 'aaMMetalforming'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<aaMMetalforming {self.id}>'

class accurideCorporate(db.Model):
    __tablename__ = 'accurideCorporate'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<accurideCorporate {self.id}>'

class accurideLab(db.Model):
    __tablename__ = 'accurideLab'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<accurideLab {self.id}>'

class accuridePlant(db.Model):
    __tablename__ = 'accuridePlant'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<accuridePlant {self.id}>'

class aFNI(db.Model):
    __tablename__ = 'aFNI'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<aFNI {self.id}>'

class aGcbellefontaine(db.Model):
    __tablename__ = 'aGcbellefontaine'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<aGcbellefontaine {self.id}>'

class aGcelizabethtown(db.Model):
    __tablename__ = 'aGcelizabethtown'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<aGcelizabethtown {self.id}>'

class aliveHospiceNashville(db.Model):
    __tablename__ = 'aliveHospiceNashville'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<aliveHospiceNashville {self.id}>'

class altec(db.Model):
    __tablename__ = 'altec'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<altec {self.id}>'

class altecweekend(db.Model):
    __tablename__ = 'altecweekend'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<altecweekend {self.id}>'

class aTTcmanufacturing(db.Model):
    __tablename__ = 'aTTcmanufacturing'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<aTTcmanufacturing {self.id}>'

class bilsteincoldrolledSteel(db.Model):
    __tablename__ = 'bilsteincoldrolledSteel'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bilsteincoldrolledSteel {self.id}>'

class bloomingtonaccountmanager(db.Model):
    __tablename__ = 'bloomingtonaccountmanager'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bloomingtonaccountmanager {self.id}>'

class bloomingtonGovernmentOffices(db.Model):
    __tablename__ = 'bloomingtonGovernmentOffices'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bloomingtonGovernmentOffices {self.id}>'

class bloomingtonOperations(db.Model):
    __tablename__ = 'bloomingtonOperations'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bloomingtonOperations {self.id}>'

class bloomingtonregionalmanager(db.Model):
    __tablename__ = 'bloomingtonregionalmanager'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bloomingtonregionalmanager {self.id}>'

class bostonScientific(db.Model):
    __tablename__ = 'bostonScientific'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bostonScientific {self.id}>'

class bowlinggreenaccountmanager(db.Model):
    __tablename__ = 'bowlinggreenaccountmanager'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bowlinggreenaccountmanager {self.id}>'

class bowlinggreenMetalforming(db.Model):
    __tablename__ = 'bowlinggreenMetalforming'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bowlinggreenMetalforming {self.id}>'

class bowlinggreenMetalformingweekend(db.Model):
    __tablename__ = 'bowlinggreenMetalformingweekend'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bowlinggreenMetalformingweekend {self.id}>'

class bowlinggreenOperations(db.Model):
    __tablename__ = 'bowlinggreenOperations'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bowlinggreenOperations {self.id}>'

class bowlinggreenregionalmanager(db.Model):
    __tablename__ = 'bowlinggreenregionalmanager'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bowlinggreenregionalmanager {self.id}>'

class centuryaluminum(db.Model):
    __tablename__ = 'centuryaluminum'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<centuryaluminum {self.id}>'

class clarrksvilleaccountmanagerKY(db.Model):
    __tablename__ = 'clarrksvilleaccountmanagerKY'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<clarrksvilleaccountmanagerKY {self.id}>'

class cloverportIndependentSchools(db.Model):
    __tablename__ = 'cloverportIndependentSchools'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<cloverportIndependentSchools {self.id}>'

class CMHOF(db.Model):
    __tablename__ = 'CMHOF'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<CMHOF {self.id}>'

class ColumbiaSportswear(db.Model):
    __tablename__ = 'ColumbiaSportswear'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<ColumbiaSportswear {self.id}>'

class CommonwealthrolledProducts(db.Model):
    __tablename__ = 'CommonwealthrolledProducts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<CommonwealthrolledProducts {self.id}>'

class ContinentalMills(db.Model):
    __tablename__ = 'ContinentalMills'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<ContinentalMills {self.id}>'

class cookaviation(db.Model):
    __tablename__ = 'cookaviation'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<cookaviation {self.id}>'

class cookMedicalSpencer(db.Model):
    __tablename__ = 'cookMedicalSpencer'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<cookMedicalSpencer {self.id}>'

class CorporateadministrativeKY(db.Model):
    __tablename__ = 'CorporateadministrativeKY'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<CorporateadministrativeKY {self.id}>'

class CorporateJanitorialwork(db.Model):
    __tablename__ = 'CorporateJanitorialwork'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<CorporateJanitorialwork {self.id}>'

class dartPolymers(db.Model):
    __tablename__ = 'dartPolymers'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<dartPolymers {self.id}>'

class deaconessboehnecamp(db.Model):
    __tablename__ = 'deaconessboehnecamp'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<deaconessboehnecamp {self.id}>'

class deaconessFranklinSt(db.Model):
    __tablename__ = 'deaconessFranklinSt'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<deaconessFranklinSt {self.id}>'

class deaconessGatewaycleanTEaM(db.Model):
    __tablename__ = 'deaconessGatewaycleanTEaM'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<deaconessGatewaycleanTEaM {self.id}>'

class deaconessPediatricsElmStreet(db.Model):
    __tablename__ = 'deaconessPediatricsElmStreet'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<deaconessPediatricsElmStreet {self.id}>'

class deaconesswilder(db.Model):
    __tablename__ = 'deaconesswilder'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<deaconesswilder {self.id}>'

class domtar(db.Model):
    __tablename__ = 'domtar'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<domtar {self.id}>'

class dorelJuvenileGroup(db.Model):
    __tablename__ = 'dorelJuvenileGroup'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<dorelJuvenileGroup {self.id}>'

class elizabethtownregionalmanager(db.Model):
    __tablename__ = 'elizabethtownregionalmanager'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<elizabethtownregionalmanager {self.id}>'

class EscaladeSportsMainOffice(db.Model):
    __tablename__ = 'EscaladeSportsMainOffice'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<EscaladeSportsMainOffice {self.id}>'

class evansvilleaccountmanager(db.Model):
    __tablename__ = 'evansvilleaccountmanager'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<evansvilleaccountmanager {self.id}>'

class evansvilleOperations(db.Model):
    __tablename__ = 'evansvilleOperations'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<evansvilleOperations {self.id}>'

class evansvilleregionalmanager(db.Model):
    __tablename__ = 'evansvilleregionalmanager'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<evansvilleregionalmanager {self.id}>'

class FranklinPrimarycare(db.Model):
    __tablename__ = 'FranklinPrimarycare'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<FranklinPrimarycare {self.id}>'

class FrantzadminNobranchassignmentKY(db.Model):
    __tablename__ = 'FrantzadminNobranchassignmentKY'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<FrantzadminNobranchassignmentKY {self.id}>'

class Fritzwinter(db.Model):
    __tablename__ = 'Fritzwinter'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Fritzwinter {self.id}>'

class FruitoftheLoom(db.Model):
    __tablename__ = 'FruitoftheLoom'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<FruitoftheLoom {self.id}>'

class Glenmore(db.Model):
    __tablename__ = 'Glenmore'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Glenmore {self.id}>'

class GravesGilbertdrGranese(db.Model):
    __tablename__ = 'GravesGilbertdrGranese'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<GravesGilbertdrGranese {self.id}>'

class GravesGilbertFamilycare(db.Model):
    __tablename__ = 'GravesGilbertFamilycare'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<GravesGilbertFamilycare {self.id}>'

class GravesGilbertFranklin(db.Model):
    __tablename__ = 'GravesGilbertFranklin'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<GravesGilbertFranklin {self.id}>'

class GravesGilbertMainOffice(db.Model):
    __tablename__ = 'GravesGilbertMainOffice'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<GravesGilbertMainOffice {self.id}>'

class GravesGilbertsurgerycenter(db.Model):
    __tablename__ = 'GravesGilbertsurgerycenter'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<GravesGilbertsurgerycenter {self.id}>'

class GravesGilbertwalkinclinic(db.Model):
    __tablename__ = 'GravesGilbertwalkinclinic'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<GravesGilbertwalkinclinic {self.id}>'

class Greenviewsurgerycenter(db.Model):
    __tablename__ = 'Greenviewsurgerycenter'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Greenviewsurgerycenter {self.id}>'

class hinesPrecision(db.Model):
    __tablename__ = 'hinesPrecision'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<hinesPrecision {self.id}>'

class HoosierEnergybedford(db.Model):
    __tablename__ = 'HoosierEnergybedford'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<HoosierEnergybedford {self.id}>'

class HoosierEnergyHeadquarters(db.Model):
    __tablename__ = 'HoosierEnergyHeadquarters'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<HoosierEnergyHeadquarters {self.id}>'

class HoosierEnergyOwenCounty(db.Model):
    __tablename__ = 'HoosierEnergyOwenCounty'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<HoosierEnergyOwenCounty {self.id}>'

class HoosierEnergyworthington(db.Model):
    __tablename__ = 'HoosierEnergyworthington'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<HoosierEnergyworthington {self.id}>'

class Hunterdouglas(db.Model):
    __tablename__ = 'Hunterdouglas'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Hunterdouglas {self.id}>'

class IUcreditUnionSouthpointedr(db.Model):
    __tablename__ = 'IUcreditUnionSouthpointedr'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<IUcreditUnionSouthpointedr {self.id}>'

class IUcreditUnionbusinesscenter(db.Model):
    __tablename__ = 'IUcreditUnionbusinesscenter'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<IUcreditUnionbusinesscenter {self.id}>'

class IUcreditUnionE17thSt(db.Model):
    __tablename__ = 'IUcreditUnionE17thSt'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<IUcreditUnionE17thSt {self.id}>'

class IUcreditUnionwinslowRd(db.Model):
    __tablename__ = 'IUcreditUnionwinslowRd'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<IUcreditUnionwinslowRd {self.id}>'

class IUHealthLandmark(db.Model):
    __tablename__ = 'IUHealthLandmark'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<IUHealthLandmark {self.id}>'

class IUHealthOrthoSportsMedicine064(db.Model):
    __tablename__ = 'IUHealthOrthoSportsMedicine064'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<IUHealthOrthoSportsMedicine064 {self.id}>'

class Kimball15thStreet(db.Model):
    __tablename__ = 'Kimball15thStreet'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Kimball15thStreet {self.id}>'

class KimballElectronicsCorpHeadquarters(db.Model):
    __tablename__ = 'KimballElectronicsCorpHeadquarters'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<KimballElectronicsCorpHeadquarters {self.id}>'

class KimballHospitalityTM(db.Model):
    __tablename__ = 'KimballHospitalityTM'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<KimballHospitalityTM {self.id}>'

class Kimberlyclarrk(db.Model):
    __tablename__ = 'Kimberlyclarrk'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Kimberlyclarrk {self.id}>'

class LivingHopebaptistchurch(db.Model):
    __tablename__ = 'LivingHopebaptistchurch'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<LivingHopebaptistchurch {self.id}>'

class MadisonvilleStateOfficebuilding(db.Model):
    __tablename__ = 'MadisonvilleStateOfficebuilding'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<MadisonvilleStateOfficebuilding {self.id}>'

class MasterbrandCorporate(db.Model):
    __tablename__ = 'MasterbrandCorporate'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<MasterbrandCorporate {self.id}>'

class MasterbranddecoraPlant3(db.Model):
    __tablename__ = 'MasterbranddecoraPlant3'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<MasterbranddecoraPlant3 {self.id}>'

class MasterbrandFerdinand(db.Model):
    __tablename__ = 'MasterbrandFerdinand'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<MasterbrandFerdinand {self.id}>'

class MasterbrandHuntingburgPlant5(db.Model):
    __tablename__ = 'MasterbrandHuntingburgPlant5'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<MasterbrandHuntingburgPlant5 {self.id}>'

class MetalsaHopkinsville(db.Model):
    __tablename__ = 'MetalsaHopkinsville'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<MetalsaHopkinsville {self.id}>'

class Mizkan(db.Model):
    __tablename__ = 'Mizkan'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Mizkan {self.id}>'

class Monumentchemical(db.Model):
    __tablename__ = 'Monumentchemical'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Monumentchemical {self.id}>'

class MSHabuilding(db.Model):
    __tablename__ = 'MSHabuilding'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<MSHabuilding {self.id}>'

class NationalCorvetteMuseum(db.Model):
    __tablename__ = 'NationalCorvetteMuseum'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<NationalCorvetteMuseum {self.id}>'

class NationalCorvetteMuseumweekend(db.Model):
    __tablename__ = 'NationalCorvetteMuseumweekend'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<NationalCorvetteMuseumweekend {self.id}>'

class NOFFordsville(db.Model):
    __tablename__ = 'NOFFordsville'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<NOFFordsville {self.id}>'

class NOFHeadquartersJasper(db.Model):
    __tablename__ = 'NOFHeadquartersJasper'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<NOFHeadquartersJasper {self.id}>'

class NOFJasper11thave(db.Model):
    __tablename__ = 'NOFJasper11thave'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<NOFJasper11thave {self.id}>'

class NOFSantaclarus(db.Model):
    __tablename__ = 'NOFSantaclarus'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<NOFSantaclarus {self.id}>'

class Northviewanderson(db.Model):
    __tablename__ = 'Northviewanderson'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Northviewanderson {self.id}>'

class Northviewbinford(db.Model):
    __tablename__ = 'Northviewbinford'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Northviewbinford {self.id}>'

class Northviewcarmel(db.Model):
    __tablename__ = 'Northviewcarmel'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Northviewcarmel {self.id}>'

class NorthviewFishers(db.Model):
    __tablename__ = 'NorthviewFishers'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<NorthviewFishers {self.id}>'

class NorthviewKokomo(db.Model):
    __tablename__ = 'NorthviewKokomo'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<NorthviewKokomo {self.id}>'

class Northviewwestfield(db.Model):
    __tablename__ = 'Northviewwestfield'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Northviewwestfield {self.id}>'

class onbbellOaks014(db.Model):
    __tablename__ = 'onbbellOaks014'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbbellOaks014 {self.id}>'

class onbboonville017(db.Model):
    __tablename__ = 'onbboonville017'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbboonville017 {self.id}>'

class onbcentralcity076(db.Model):
    __tablename__ = 'onbcentralcity076'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbcentralcity076 {self.id}>'

class onbHebron007(db.Model):
    __tablename__ = 'onbHebron007'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbHebron007 {self.id}>'

class onbJasperGermantown106(db.Model):
    __tablename__ = 'onbJasperGermantown106'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbJasperGermantown106 {self.id}>'

class onbJasperMain098(db.Model):
    __tablename__ = 'onbJasperMain098'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbJasperMain098 {self.id}>'

class onbmadisonvilleMain077(db.Model):
    __tablename__ = 'onbmadisonvilleMain077'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbmadisonvilleMain077 {self.id}>'

class onbmorganfieldMain061(db.Model):
    __tablename__ = 'onbmorganfieldMain061'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbmorganfieldMain061 {self.id}>'

class onbOwensboroHwy54220(db.Model):
    __tablename__ = 'onbOwensboroHwy54220'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbOwensboroHwy54220 {self.id}>'

class onbOwensboroMain133(db.Model):
    __tablename__ = 'onbOwensboroMain133'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbOwensboroMain133 {self.id}>'

class onbTellcityOldHwyRd027(db.Model):
    __tablename__ = 'onbTellcityOldHwyRd027'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbTellcityOldHwyRd027 {self.id}>'

class onbvincennesMain0671(db.Model):
    __tablename__ = 'onbvincennesMain0671'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbvincennesMain0671 {self.id}>'

class onbwashingtonKY003(db.Model):
    __tablename__ = 'onbwashingtonKY003'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<onbwashingtonKY003 {self.id}>'

class OPScentralOffice(db.Model):
    __tablename__ = 'OPScentralOffice'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<OPScentralOffice {self.id}>'

class OPSFoustElementary(db.Model):
    __tablename__ = 'OPSFoustElementary'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<OPSFoustElementary {self.id}>'

class OPSsuttonElementarySchool(db.Model):
    __tablename__ = 'OPSsuttonElementarySchool'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<OPSsuttonElementarySchool {self.id}>'

class Owensboromanufacturing(db.Model):
    __tablename__ = 'Owensboromanufacturing'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Owensboromanufacturing {self.id}>'

class redSpotpaint(db.Model):
    __tablename__ = 'redSpotpaint'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<redSpotpaint {self.id}>'

class Sabic(db.Model):
    __tablename__ = 'Sabic'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Sabic {self.id}>'

class SalesCorporate(db.Model):
    __tablename__ = 'SalesCorporate'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<SalesCorporate {self.id}>'

class SalesInHouse(db.Model):
    __tablename__ = 'SalesInHouse'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<SalesInHouse {self.id}>'

class SingotaSolutions(db.Model):
    __tablename__ = 'SingotaSolutions'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<SingotaSolutions {self.id}>'

class SIraImagingcenter(db.Model):
    __tablename__ = 'SIraImagingcenter'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<SIraImagingcenter {self.id}>'

class Smuckers(db.Model):
    __tablename__ = 'Smuckers'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Smuckers {self.id}>'

class Smuckersweekend(db.Model):
    __tablename__ = 'Smuckersweekend'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Smuckersweekend {self.id}>'

class Sonoco(db.Model):
    __tablename__ = 'Sonoco'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Sonoco {self.id}>'

class Spectrumbrands(db.Model):
    __tablename__ = 'Spectrumbrands'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Spectrumbrands {self.id}>'

class surgicare(db.Model):
    __tablename__ = 'surgicare'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<surgicare {self.id}>'

class SwedishMatchbackSquare(db.Model):
    __tablename__ = 'SwedishMatchbackSquare'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<SwedishMatchbackSquare {self.id}>'

class TheFields(db.Model):
    __tablename__ = 'TheFields'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<TheFields {self.id}>'

class TowerInternationalbardstown(db.Model):
    __tablename__ = 'TowerInternationalbardstown'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<TowerInternationalbardstown {self.id}>'

class TowerInternationalShepherdsville(db.Model):
    __tablename__ = 'TowerInternationalShepherdsville'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<TowerInternationalShepherdsville {self.id}>'

class Toyoautomotive(db.Model):
    __tablename__ = 'Toyoautomotive'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Toyoautomotive {self.id}>'

class ToyotaIndustrialEquipment(db.Model):
    __tablename__ = 'ToyotaIndustrialEquipment'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<ToyotaIndustrialEquipment {self.id}>'

class Tungco(db.Model):
    __tablename__ = 'Tungco'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Tungco {self.id}>'

class Unifirst(db.Model):
    __tablename__ = 'Unifirst'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Unifirst {self.id}>'

class Unitedcomanies3420(db.Model):
    __tablename__ = 'Unitedcomanies3420'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Unitedcomanies3420 {self.id}>'

class UnitedLeasing3700(db.Model):
    __tablename__ = 'UnitedLeasing3700'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<UnitedLeasing3700 {self.id}>'

class Uplandbrewingcomany(db.Model):
    __tablename__ = 'Uplandbrewingcomany'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Uplandbrewingcomany {self.id}>'

class usbankairparkdayPorter4624(db.Model):
    __tablename__ = 'usbankairparkdayPorter4624'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usbankairparkdayPorter4624 {self.id}>'

class usbankairparkdrive4624(db.Model):
    __tablename__ = 'usbankairparkdrive4624'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usbankairparkdrive4624 {self.id}>'

class usbankcarterroad4553(db.Model):
    __tablename__ = 'usbankcarterroad4553'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usbankcarterroad4553 {self.id}>'

class usbankEastMain4432(db.Model):
    __tablename__ = 'usbankEastMain4432'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usbankEastMain4432 {self.id}>'

class usbankhighlandPoint4615(db.Model):
    __tablename__ = 'usbankhighlandPoint4615'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usbankhighlandPoint4615 {self.id}>'

class usbankhighlandPointdayporter4615(db.Model):
    __tablename__ = 'usbankhighlandPointdayporter4615'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usbankhighlandPointdayporter4615 {self.id}>'

class usbankMoreland4416(db.Model):
    __tablename__ = 'usbankMoreland4416'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usbankMoreland4416 {self.id}>'

class usbankMortgage4551(db.Model):
    __tablename__ = 'usbankMortgage4551'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usbankMortgage4551 {self.id}>'

class usbankMortgagedayporter4551(db.Model):
    __tablename__ = 'usbankMortgagedayporter4551'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usbankMortgagedayporter4551 {self.id}>'

class usbankNewHartford4558(db.Model):
    __tablename__ = 'usbankNewHartford4558'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usbankNewHartford4558 {self.id}>'

class usSmokelessTobaccoEagleOne(db.Model):
    __tablename__ = 'usSmokelessTobaccoEagleOne'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usSmokelessTobaccoEagleOne {self.id}>'

class usSmokelessTobaccoMainPlant(db.Model):
    __tablename__ = 'usSmokelessTobaccoMainPlant'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<usSmokelessTobaccoMainPlant {self.id}>'

class webbwheelProducts(db.Model):
    __tablename__ = 'webbwheelProducts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<webbwheelProducts {self.id}>'

class westrock(db.Model):
    __tablename__ = 'westrock'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    employeenumber = db.Column(db.INTEGER, nullable=False)
    firstname = db.Column(db.TEXT, nullable=False)
    lastname = db.Column(db.TEXT, nullable=False)
    hiredate = db.Column(db.TEXT, nullable=False)
    classificationdescription = db.Column(db.TEXT, nullable=False)
    employeetypedescription = db.Column(db.TEXT, nullable=False)
    supervisordescription = db.Column(db.TEXT, nullable=False)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    categorydescription = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)
    title = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    companyaddress2 = db.Column(db.TEXT, nullable=False)
    uctaxpayeridnumber = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobaddress2 = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    employmenttype = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<westrock {self.id}>'

class aaronPitzeraccounts(db.Model):
    __tablename__ = 'aaronPitzeraccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<aaronPitzeraccounts {self.id}>'

class adoriaPruittaccounts(db.Model):
    __tablename__ = 'adoriaPruittaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<adoriaPruittaccounts {self.id}>'

class amberbeachaccounts(db.Model):
    __tablename__ = 'amberbeachaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<amberbeachaccounts {self.id}>'

class angiecomtonaccounts(db.Model):
    __tablename__ = 'angiecomtonaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<angiecomtonaccounts {self.id}>'

class bethLeeaccounts(db.Model):
    __tablename__ = 'bethLeeaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<bethLeeaccounts {self.id}>'

class brandonburrellaccounts(db.Model):
    __tablename__ = 'brandonburrellaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<brandonburrellaccounts {self.id}>'

class brandywilliamsaccounts(db.Model):
    __tablename__ = 'brandywilliamsaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<brandywilliamsaccounts {self.id}>'

class brianLewisaccounts(db.Model):
    __tablename__ = 'brianLewisaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<brianLewisaccounts {self.id}>'

class britneychiltonaccounts(db.Model):
    __tablename__ = 'britneychiltonaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<britneychiltonaccounts {self.id}>'

class charlesbaileyaccounts(db.Model):
    __tablename__ = 'charlesbaileyaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<charlesbaileyaccounts {self.id}>'

class davidvoorheesaccounts(db.Model):
    __tablename__ = 'davidvoorheesaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<davidvoorheesaccounts {self.id}>'

class debraMurphyaccounts(db.Model):
    __tablename__ = 'debraMurphyaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<debraMurphyaccounts {self.id}>'

class desmondcarpenteraccounts(db.Model):
    __tablename__ = 'desmondcarpenteraccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<desmondcarpenteraccounts {self.id}>'

class donnaMccartyaccounts(db.Model):
    __tablename__ = 'donnaMccartyaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<donnaMccartyaccounts {self.id}>'

class ericjohnsonaccounts(db.Model):
    __tablename__ = 'ericjohnsonaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<ericjohnsonaccounts {self.id}>'

class Inactiveaccounts(db.Model):
    __tablename__ = 'Inactiveaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Inactiveaccounts {self.id}>'

class Inactivejobaccounts(db.Model):
    __tablename__ = 'Inactivejobaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Inactivejobaccounts {self.id}>'

class jordanTongaccounts(db.Model):
    __tablename__ = 'jordanTongaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<jordanTongaccounts {self.id}>'

class JulianGulleyaccounts(db.Model):
    __tablename__ = 'JulianGulleyaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<JulianGulleyaccounts {self.id}>'

class KathyHogueaccounts(db.Model):
    __tablename__ = 'KathyHogueaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<KathyHogueaccounts {self.id}>'

class Katrinarabuckaccounts(db.Model):
    __tablename__ = 'Katrinarabuckaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Katrinarabuckaccounts {self.id}>'

class KeshaHallaccounts(db.Model):
    __tablename__ = 'KeshaHallaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<KeshaHallaccounts {self.id}>'

class Kimjonesaccounts(db.Model):
    __tablename__ = 'Kimjonesaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Kimjonesaccounts {self.id}>'

class KimberlyMcConnellaccounts(db.Model):
    __tablename__ = 'KimberlyMcConnellaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<KimberlyMcConnellaccounts {self.id}>'

class Kylebartlettaccounts(db.Model):
    __tablename__ = 'Kylebartlettaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Kylebartlettaccounts {self.id}>'

class Lisabentonaccounts(db.Model):
    __tablename__ = 'Lisabentonaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Lisabentonaccounts {self.id}>'

class rodneyPhillipsaccounts(db.Model):
    __tablename__ = 'rodneyPhillipsaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<rodneyPhillipsaccounts {self.id}>'

class SammieKiddaccounts(db.Model):
    __tablename__ = 'SammieKiddaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<SammieKiddaccounts {self.id}>'

class Sarahbradleyaccounts(db.Model):
    __tablename__ = 'Sarahbradleyaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Sarahbradleyaccounts {self.id}>'

class StevenKiddaccounts(db.Model):
    __tablename__ = 'StevenKiddaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<StevenKiddaccounts {self.id}>'

class StevenSimmonsaccounts(db.Model):
    __tablename__ = 'StevenSimmonsaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<StevenSimmonsaccounts {self.id}>'

class Tammywolfeaccounts(db.Model):
    __tablename__ = 'Tammywolfeaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<Tammywolfeaccounts {self.id}>'

class valerierankinaccounts(db.Model):
    __tablename__ = 'valerierankinaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<valerierankinaccounts {self.id}>'

class vickiSouthernaccounts(db.Model):
    __tablename__ = 'vickiSouthernaccounts'
    id = db.Column(db.INTEGER, nullable=False,primary_key=True)
    jobnumber = db.Column(db.INTEGER, nullable=False)
    jobname = db.Column(db.TEXT, nullable=False)
    jobaddress = db.Column(db.TEXT, nullable=False)
    jobcity = db.Column(db.TEXT, nullable=False)
    jobstate = db.Column(db.TEXT, nullable=False)
    jobzip = db.Column(db.TEXT, nullable=False)
    businesssegment = db.Column(db.TEXT, nullable=False)
    regionalmanager = db.Column(db.TEXT, nullable=False)
    accountmanager = db.Column(db.TEXT, nullable=False)
    region = db.Column(db.TEXT, nullable=False)

    def __repr__(self):
        return f'<vickiSouthernaccounts {self.id}>'



class termemployeetable(db.Model):
    __tablename__ = 'termemployeetable'

    id = db.Column(db.Integer, primary_key=True)
    employeenumber = db.Column(db.Integer)
    firstname = db.Column(db.String(500))
    lastname = db.Column(db.String(500))
    hiredate = db.Column(db.String(500))
    classificationdescription = db.Column(db.String(500))
    employeetypedescription = db.Column(db.String(500))
    supervisordescription = db.Column(db.String(500))
    jobnumber = db.Column(db.String(500))
    jobname = db.Column(db.String(500))
    categorydescription = db.Column(db.String(500))
    region = db.Column(db.String(500))
    title = db.Column(db.String(500))
    jobstate = db.Column(db.String(500))
    companyaddress2 = db.Column(db.String(500))
    uctaxpayeridnumber = db.Column(db.String(500))
    jobaddress = db.Column(db.String(500))
    jobaddress2 = db.Column(db.String(500))
    jobcity = db.Column(db.String(500))
    jobzip = db.Column(db.String(500))
    employmenttype = db.Column(db.String(500))
    lastdayworked = db.Column(db.String(500))
    reasonforleaving = db.Column(db.String(500))
    additionalinformation = db.Column(db.String(500))
    dependabilityslider = db.Column(db.String(500))
    dependabilitycomments = db.Column(db.String(500))
    abilityslider = db.Column(db.String(500))
    abilitycomments = db.Column(db.String(500))
    attitudetowardjobslider = db.Column(db.String(500))
    attitudetowardjobcomments = db.Column(db.String(500))
    attitudetowardsupervisorslider = db.Column(db.String(500))
    attitudetowardsupervisorcomments = db.Column(db.String(500))
    attitudetowardcoworkersslider = db.Column(db.String(500))
    attitudetowardcoworkerscomments = db.Column(db.String(500))
    leadershipslider = db.Column(db.String(500))
    leadershipcomments = db.Column(db.String(500))
    workwithoutsupervisionslider = db.Column(db.String(500))
    workwithoutsupervisioncomments = db.Column(db.String(500))
    totalevalscore = db.Column(db.String(500))
    eligibleforhire = db.Column(db.String(500))
    eligibleforhiredate = db.Column(db.String(500))

    def __repr__(self):
        return f'<termemployeetable {self.id}>'


class applicants(db.Model):
    __tablename__ = 'applicants'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.Text)
    are_you_at_least_18_years_old_ = db.Column(db.Text)
    are_you_legally_eligible_to_work_in_the_us_ = db.Column(db.Text)
    full_time_or_part_time_employment_ = db.Column(db.Text)
    best_way_to_contact_you_ = db.Column(db.Text)
    city = db.Column(db.Text)
    company = db.Column(db.Text)
    content = db.Column(db.Text)
    startdate = db.Column(db.Date)
    date_available_to_start_work_ = db.Column(db.Date)
    two_forms_of_id_valid_and_hard_copies = db.Column(db.Text)
    email = db.Column(db.Text)
    enddate = db.Column(db.Date)
    firstname = db.Column(db.Text)
    applied_or_employed_by_frantz_building_services = db.Column(db.Text)
    job_location = db.Column(db.Text)
    jobtitle = db.Column(db.Text)
    lastname = db.Column(db.Text)
    may_we_contact_this_employer_ = db.Column(db.Text)
    no_contact_explanation = db.Column(db.Text)
    phone = db.Column(db.Text)
    one_person_who_would_confirm_great_employee = db.Column(db.Text)
    state = db.Column(db.Text)
    supervisor__phone_number = db.Column(db.Text)
    role_description = db.Column(db.Text)
    supervisor_name = db.Column(db.Text)
    reason_for_leaving_ = db.Column(db.Text)
    their_phone_number = db.Column(db.Text)
    applicantid = db.Column(db.Text)
    accountmanager = db.Column(db.Text)
    regionalmanager = db.Column(db.Text)
    eligibleforhire = db.Column(db.Text)
    applicantstatus = db.Column(db.Text)
    hubspotcontactid = db.Column(db.Text)
    contacthistory = db.Column(db.Text)
    lastcontact = db.Column(db.Date)
    lastcontacttype = db.Column(db.Text)
    nextcontact = db.Column(db.Date)
    nextcontacttype = db.Column(db.Text)
    dateapplied = db.Column(db.Date)
    backgroundcheck = db.Column(db.Text)
    idstatus = db.Column(db.Text)
    drugscreen = db.Column(db.Text)
    positionid = db.Column(db.Text)
    jobnumber = db.Column(db.Text)
    preferred_name = db.Column(db.Text)
    applicant_statement_signature = db.Column(db.Text)
    applicant_statement_acknowledgement = db.Column(db.Text)
    applicant_statement_date_acknowledgement = db.Column(db.Text)

    def __repr__(self):
        return f'<applicants {self.id}>'



