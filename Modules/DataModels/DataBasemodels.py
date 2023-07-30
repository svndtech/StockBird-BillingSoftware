

from sqlalchemy import create_engine,Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker ,declarative_base
import datetime


Base = declarative_base()

class UserGroup(Base):
    __tablename__ = "user_group"

    user_group_id = Column("user_group_id",Integer,primary_key=True)
    user_group_name = Column("user_group_name",String)

    def __init__(self,user_group_id,user_group_name):
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def __repr__(self):
        return f"({self.user_group_id})  {self.user_group_name}"    


class Department(Base):
    __tablename__ = "department"

    dept_id = Column("id", Integer, primary_key=True)
    department = Column("department", String)

    def __init__(self, dept_id, department):
        self.dept_id = dept_id
        self.department = department

    def __repr__(self):
        return f"({self.id})  {self.department}"


class Employee(Base):

    __tablename__ = "employee"

    ssn = Column("id", Integer, primary_key=True)
    employee_id = Column("employee_id", Integer)
    department = Column(Integer, ForeignKey("department.id"))
    name = Column("name", String)
    dob = Column("dob", Date)
    mobile = Column("mobile", Integer)
    address = Column("address", String)

    def __init__(self, ssn, employee_id, department, name, dob, mobile, address):
        self.ssn = ssn
        self.employee_id = employee_id
        self.department = department
        self.name = name
        self.dob = dob
        self.mobile = mobile
        self.address = address

    def __repr__(self):
        return f"({self.ssn})  {self.employee_id} {self.name} {self.department} {self.name} {self.dob} {self.mobile} {self.address}"


class User(Base):

    __tablename__ = "user_account"

    user_id = Column("user_id", Integer, primary_key=True)
    employee_id = Column("employee_id", ForeignKey("employee.employee_id"))
    username = Column("user_name", String)
    password = Column("password", String)
    created_on = Column("created_on", DateTime)
    updated_on = Column("updated_on", DateTime)

    def __init__(self, user_id, employee_id, username, password, created_on, updated_on):
        self.user_id = user_id 
        self.employee_id = employee_id
        self.username = username
        self._password = password
        self.created_on = created_on
        self.updated_on = updated_on

engine = create_engine("sqlite:///stockbird_db.db",echo=True)
# Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

ug01 = UserGroup(104,'Biller')

dp01 = Department(101,'Management')

today_date = datetime.date.today()
emp01 = Employee(123456789,2907202301,dp01.dept_id,"Admin User",today_date,9876543210,"Chennai")
session.add(emp01)
session.commit()