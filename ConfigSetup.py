# Novixel's Config File Setup - The Bitcoin Boxer
# Version 1 - First Official Release - 
# April 17, 2021
#
# ConfigSetup.py
#
import os
from pathlib import Path
from configparser import ConfigParser

# This is our VIP constant global variable!
product_id = str

# Lets build a few configurable setting for the program!

# (Build Directory)
        # Build A place for the bots config files to be stored 
def BuildBotNest():
    fullPath = os.path.realpath(__file__) # Get Exact Path to this file
    thisDir = os.path.dirname(fullPath) # Get Exact Directory of this File
    botFold = thisDir + '\BoxingRules' # Create a new folder path for setup 
    Path(botFold).mkdir(parents=True, exist_ok=True) # Check for folder or make if not there
    os.chdir(botFold) # change Directory to save setup files
    return botFold

path = str(BuildBotNest()) # we need this for all the settings :)

pathStr = (path + '\config.ini') # create the file string for repeat

# (Build Config File)
        # Build a config file in that folder we just made for later use.
def BuildBotSettings():
    config_object = ConfigParser()
    config_object["API"] = {            
        "key"           :   "CoinbaseProAPI key",
        "b64secret"     :   "CoinbaseProAPI b64secret",
        "passphrase"    :   "CoinbaseProAPI passphrase"
    }
    config_object["TICKER"] = {
            "trade_id"  :   "Trade ID Number",
            "price"     :   "Current Price",
            "size"      :   "0.000000000000000",
            "time"      :   "2021-05-01T12:00:00.578544Z",
            "bid"       :   "0.000000000000000",
            "ask"       :   "0.000000000000000",
            "volume"    :   "0.000000000000000"
    }
    config_object["DAYSTATS"] = {
        "open"          :   "0.000000000000000", 
        "high"          :   "0.000000000000000", 
        "low"           :   "0.000000000000000", 
        "volume"        :   "0.000000000000000", 
        "last"          :   "0.000000000000000", 
        "volume_30day"  :   "0.000000000000000"
    }
    config_object["LEFTACCOUNT"] = {
        'id'                :   'Base account id', 
        'currency'          :   'base', 
        'balance'           :   '0.0000000000000000', 
        'hold'              :   '0.000000000000000', 
        'available'         :   '0.0000000000000', 
        'profile_id'        :   'profile id', 
        'trading_enabled'   :   "bool"
    }
    config_object["RIGHTACCOUNT"] = {
        'id'                :   'Quote account id', 
        'currency'          :   'quote', 
        'balance'           :   '0.000000000000000', 
        'hold'              :   '0.000000000000000', 
        'available'         :   '0.000000000000000', 
        'profile_id'        :   'profile id', 
        'trading_enabled'   :   "bool"
    }
    config_object["LASTTRADE"] = {
        "time"          :   "2021-05-01T12:00:00.578544Z",
        "trade_id"      :   "000",
        "price"         :   "0.000000000000000",
        "size"          :   "0.000000000000000",
        "side"          :   "side"
    }
    config_object["PROFITS"] = {
        "start_time"        :   "2021-05-01T12:00:00.578544Z",
        "start_total"       :   "0.000000000000000",
        "current_total"     :   "0.000000000000000",
        "profit"            :   "0.000000000000000",
    }

    #Write to a file!!
    with open(pathStr,'w') as conf:
        config_object.write(conf)

# (Edit That Config File)
        # Save to new data to The Config File we just made
        # these need to be compacted in to one function
def SaveNewApi(key,b64secret,passphrase):
    c = ConfigParser()
    c.read(pathStr)
    #Get the api from config
    API = c["API"]
    API["key"] = str(key)
    API["b64secret"] = str(b64secret)
    API["passphrase"] = str(passphrase)
    #Write changes back to file
    with open(pathStr, 'w') as conf:
        c.write(conf)

def SaveLeftAccount(x,d):
    c = ConfigParser()
    c.read(pathStr)
    #Get the api from config
    account = c["LEFTACCOUNT"]
    account[str(x)] = d
    with open(pathStr, 'w') as conf:
        c.write(conf)

def SaveRightAccount(x,d):
    c = ConfigParser()
    c.read(pathStr)
    #Get the api from config
    account = c["RIGHTACCOUNT"]
    account[str(x)] = d
    with open(pathStr, 'w') as conf:
        c.write(conf)

def SaveTicker(x , d ):
    c = ConfigParser()
    c.read(pathStr)
    #Get the api from config
    TICKER = c["TICKER"]
    TICKER[str(x)] = d
    with open(pathStr, 'w') as conf:
        c.write(conf)

def SaveDay(x , d ):
    c = ConfigParser()
    c.read(pathStr)
    #Get the api from config
    DAY = c["DAYSTATS"]
    DAY[str(x)] = d
    with open(pathStr, 'w') as conf:
        c.write(conf)

def SaveTrade(x , d ):
    c = ConfigParser()
    c.read(pathStr)
    #Get the api from config
    Trade = c["LASTTRADE"]
    Trade[str(x)] = d
    with open(pathStr, 'w') as conf:
        c.write(conf)

def SaveProfit(x , d ):
    c = ConfigParser()
    c.read(pathStr)
    #Get the api from config
    profit = c["PROFITS"]
    profit[str(x)] = d
    with open(pathStr, 'w') as conf:
        c.write(conf)

# (Read That Config File)
# Read the file and assign variables to the values
# these need to be compacted in to one function
def ReadConfig(x):
    """x should be what you want from the config file as a string"""
    c = ConfigParser()
    c.read(pathStr)
    #Get Info from config
    API = c["API"]
    return API[x]

def ReadProfit(x):
    """x should be what you want from the config file as a string"""
    c = ConfigParser()
    c.read(pathStr)
    #Get Info from config
    PROFITS = c["PROFITS"]
    return PROFITS[x]

def ReadLASTTRADE(x):
    """x = 'price',etc """
    c = ConfigParser()
    c.read(pathStr)
    #Get Info from config
    LASTTRADE = c["LASTTRADE"]
    return LASTTRADE[x]

def ReadTICKER(x):
    """x = 'price',etc """
    c = ConfigParser()
    c.read(pathStr)
    #Get Info from config
    TICKER = c["TICKER"]
    return TICKER[x]

def ReadDAYSTATS(x):
    """x = 'open',etc """
    c = ConfigParser()
    c.read(pathStr)
    #Get Info from config
    DAY = c["DAYSTATS"]
    return DAY[x]

def ReadLEFTaccount(x):
    """x = 'available',etc """
    c = ConfigParser()
    c.read(pathStr)
    #Get Info from config
    ACCOUNT = c["LEFTACCOUNT"]
    return ACCOUNT[x]

def ReadRIGHTaccount(x):
    """x = 'available',etc """
    c = ConfigParser()
    c.read(pathStr)
    #Get Info from config
    ACCOUNT = c["RIGHTACCOUNT"]
    return ACCOUNT[x]