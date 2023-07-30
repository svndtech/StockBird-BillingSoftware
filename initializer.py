# All Initialization is created here , like package imports , file creation, etc ,.
from sqlalchemy import create_engine
from sys import stdout
import os

# Creation of a sql file that holds the whole database


class Initializer:

    def __init__(self):
        print("\n STOCK BIRD - SVND Technologies \n STARTING Application.....! \n STOCKBIRD v1.1 Aug 2023 - Made to stock wisely. \n Initializing everything for you... Kindly wait \n Welcome to Stock Bird")

    def initialize_environment(self):
        try:
        
            print("\n Installing Python 3.8.2")
            if(os.path.isfile(os.path.join(os.path.join(os.getcwd(),"python"),"python.exe"))==False):
                current_dir = os.path.join(os.getcwd(), "python")
                os.mkdir(current_dir)
                print(current_dir)
                os.system(f".\\python-3.8.2-amd64.exe /quiet TargetDir={current_dir} InstallAllUsers=1 PrependPath=1 Include_test=0 ")
            else:
                print("Python Exists !")
        
        except Exception as e:

            print("ERROR " + str(e))    

        finally :

            pass        



