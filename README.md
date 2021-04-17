# BitcoinBoxer
    The Bitcoin Boxer! 
    
    A custom built crypto currency trading algorithm designed to trade automaticly on the Coinbase Pro Exchange.
    
    Designed by Simon
    Built by Novixel
    
    Installation: 
        
    Step 1 (Install Python & PyPi)
        Heres a quck easy to understand guide!
        https://realpython.com/installing-python/
        
        Make Sure Your Version Of Python Contains 'pip'
        https://pip.pypa.io/en/stable/installing/
        
        
    Step 2 (Build virtual enviroment for the program to run in):
        type in console --->   python3 -m pip install -- user pipenv
        More detailed guide in the link below
        https://docs.python-guide.org/dev/virtualenvs/
        
        We will need this to easily download our dependacy of other librarys.
        or your can always download them manually. So this Step is Optional!
        
        
    Step 3 (Get everything together!)
        Extract the contents of this repo zip file in to a seperate folder
        Alternitivly you can clone the repo!
       
        Once you have the files un-zipped your free to open up StartHere.py with your favorite text editor
        if you want to mess around with the variables in that script!
       
        
    Step 4:
        Open up a terminal/CommantPrompt and navigate to that files directory. 
        it should look somthing like this 'c:/thisPC/user/desktop/ThePlaceYouPutTheBot/'
        
        cd ThePlaceYouPutTheBot
        
        Once your inside of that folder! in the terminal type this
            --->  pipenv install
        this will install all the requeried dependancy's for the project
        more detailed info in the link below
        https://pipenv.kennethreitz.org/en/latest/install/#pragmatic-installation-of-pipenv
        
    Finnaly!! 
    
        The bot will ask you for the following information upon first initilization.
        --- Best to have this ready before hand ---
        
        Enter the Currency Pair you would like to trade on,
            - We defualt to 'BTC-EUR' if user input was empty
        
        Enter Your Api Key, 
        Enter Your Api Secret,
        Enter Your Api Passphrase,
    
        1 Addition file will be created
        within a new directory. ---- >   BoxingRules/config.ini
    
        These is a very important file for the program to run.
        minumum trade is set at 100
        
        Now Watch The Magic Happen! and let the bot make you some profits!!
        
        
