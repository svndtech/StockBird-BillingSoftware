# from Modules import root
import initializer

def main():

    init = initializer.Initializer()
    init.initialize_tables()
    # print("Final ",init.initialize_environment())
    # init.install_python() if init.initialize_environment()==False else print("Python Already Exists")
    pass

if __name__ == "__main__":
    main()

    
    
    