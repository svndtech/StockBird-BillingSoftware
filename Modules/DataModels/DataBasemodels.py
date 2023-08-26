from sqlalchemy import create_engine,Column, Integer, String, Date, ForeignKey, DateTime ,Time, ARRAY , JSON
from sqlalchemy.orm import sessionmaker ,declarative_base
import datetime


Base = declarative_base()

class Products(Base):
    __tablename__ = "products"

    product_id = Column("product_id",Integer, primary_key=True)
    product_name = Column("product_name",String)
    unit_price = Column("unit_price",Integer)
    product_type_id = Column("product_type_id",String)
    product_label = Column("product_label",String)
    description = Column("description", String)

    def __init__(self,product_id,product_name,unit_price,product_type_id,product_label,description):
        self.product_id = product_id
        self.product_name = product_name
        self.unit_price = unit_price
        self.product_type_id = product_type_id
        self.product_label = product_label
        self.description = description

    def __repr__(self):
        return f"({self.product_label})  - Rs. {self.unit_price}"        


class ProductType(Base):
    __tablename__ = "product_types"

    type_id = Column("type_id", Integer , primary_key=True)
    product_type = Column("product_type" , String)

    def __init__(self,type_id , product_type):
        self.type_id = type_id
        self.product_type = product_type

    def __repr__(self):
        return f"({self.type_id} - {self.product_type})"
    
    
class PurchaseHistory(Base):
    __tablename__ = "purchase_history"

    purchase_id = Column("purchase_id",Integer)
    product_id = Column("product_id",Integer)
    bill_id = Column("bill_id",Integer)
    purchase_date = Column("purchase_date",Date)
    purchase_time = Column("purchase_time",Time)

    def __init__(self):
        pass
    
    def __repr__(self):
        pass




class Bills(Base):
    __tablename__ = "bills"    

    bill_id = Column("bill_id", Integer,primary_key=True)
    pass 


class Members(Base):
    __tablename__ = "members"

    member_id = Column("member_id",Integer, primary_key=True)
    member_discount = Column("member_discount", Integer)
    member_name = Column("member_name", String,default=member_id)
    member_created_on =  Column("created_on",DateTime)
    member_updated_on = Column("updated_on",DateTime)

    def __init__(self,member_id,member_discount,member_name,member_created_on, member_updated_on):
        self.member_id = member_id
        self.member_discount = member_discount
        self.member_name =  member_name
        self.member_created_on = member_created_on
        self.member_updated_on = member_updated_on

    def __repr__(self):
        return f"{self.member_id} {self.member_name}"    

        
class UserGroups(Base):
    __tablename__ = "user_groups"

    user_group_id = Column("user_group_id",Integer,primary_key=True)
    user_group_name = Column("user_group_name",String)

    def __init__(self,user_group_id,user_group_name):
        self.user_group_id = user_group_id
        self.user_group_name = user_group_name

    def __repr__(self):
        return f"({self.user_group_id})  {self.user_group_name}"    


class Departments(Base):
    __tablename__ = "departments"

    dept_id = Column("id", Integer, primary_key=True)
    department = Column("department", String)

    def __init__(self, dept_id, department):
        self.dept_id = dept_id
        self.department = department

    def __repr__(self):
        return f"({self.id})  {self.department}"


class Employees(Base):

    __tablename__ = "employees"

    ssn = Column("id", Integer, primary_key=True)
    employee_id = Column("employee_id", Integer)
    department = Column(Integer, ForeignKey("department.id"),cascade=all)
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


class Users(Base):

    __tablename__ = "user_accounts"

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

ug01 = UserGroups(104,'Biller')

dp01 = Departments(101,'Management')

today_date = datetime.date.today()
emp01 = Employees(123456789,2907202301,dp01.dept_id,"Admin User",today_date,9876543210,"Chennai")
session.add(emp01)
session.commit()