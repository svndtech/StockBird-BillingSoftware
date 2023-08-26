from sqlalchemy.orm import sessionmaker ,declarative_base
from sqlalchemy import create_engine
import datetime 
from DataModels.DataBasemodels import User

class UserDataAccessImplementation:

    def __init__(self):
        engine = create_engine("sqlite:///stockbird_db.db",echo=True)
        # Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def add_user(self,user_object):
        try:
            if isinstance(user_object,User):
                self.session.add(user_object)
                self.session.commit(user_object)
                return True
            return False
        except Exception as e:
            print(str(e))
            return False


