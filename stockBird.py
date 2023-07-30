from Modules import root
import initializer

if __name__ == "__main__":

    init = initializer.Initializer()
    init.initialize_environment()

    stockApp = root.rootGui()
    stockRoot = stockApp.getRoot()
    stockApp.getLoginFrame()
    
    