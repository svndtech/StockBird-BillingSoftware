# All Initialization is created here , like package imports , file creation, etc ,.
import os
from sqlalchemy import exc
import json
from Modules.DataModels import *
# Creation of a sql file that holds the whole database


class Initializer:

    def __init__(self):
        print("\n STOCK BIRD - SVND Technologies \n STARTING Application.....! \n STOCKBIRD v1.1 Aug 2023 - Made to stock wisely. \n Initializing everything for you... Kindly wait \n Welcome to Stock Bird")
        self.current_dir = os.path.join(os.getcwd(), "python")


    def initialize_environment(self):
        try:
            if(os.path.isdir(self.current_dir)==False):
                print("\n Creating a new directory for python installation.")
                os.mkdir(self.current_dir)
                return False
            else:
                return os.path.isfile(os.path.join(self.current_dir,"python.exe"))
        except FileExistsError as e:
            print("ERROR " + str(e))    
            return True 

    def initialize_tables(self):
        try:
          with open('initializationData.json') as json_file :
              json_data = json.load(json_file)
              print(json_data)
              for key,value in json_data.items():
                  if(key=="user_groups"):
                      User

        except exc.OperationalError as e:
            print(str(e))        



