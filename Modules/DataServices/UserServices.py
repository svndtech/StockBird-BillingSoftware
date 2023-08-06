from DataAccessors.UserDAI import UserDataAccessImplementation



class UserService:
    
    def __init__(self) -> None:
        
        self.user_dao = UserDataAccessImplementation()

    def add_user(self,user_object):
        return self.user_dao.add_user(user_object)