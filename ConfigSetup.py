# Novixel's Config File Setup - The Bitcoin Boxer
# Version 0.02 - Pre-Release - Beta Testing
# April 14, 2021
#
# ConfigSetup.py
#
import os
from pathlib import Path
from configparser import ConfigParser

product_id = str # temp

# Lets build a few configurable setting for the program!

# Step 1 (Build Directory)
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

# Step 2 (Build Config File)
        # Build a config file in that folder we just made for later use.
def BuildBotSettings():
    config_object = ConfigParser()
    config_object["API"] = {            
        "key": "CoinbaseProAPI key",
        "b64secret": "CoinbaseProAPI b64secret",
        "passphrase": "CoinbaseProAPI passphrase"
    }
    config_object["TICKER"] = {
        "trade_id" : "Trade ID Number",
        "price" : "Current Price",
        "size" : "0.01019058",
        "time" : "2021-04-08T08:35:54.751006Z",
        "bid" : "48101.39",
        "ask" : "48115.5",
        "volume" : "1691.61862457"
    }
    config_object["DAYSTATS"] = {
        "open": "6745.00000000", 
        "high": "7292.11000000", 
        "low": "6650.00000000", 
        "volume": "26185.51325269", 
        "last": "6813.19000000", 
        "volume_30day": "1019451.11188405"
    }
    config_object["LEFTACCOUNT"] = {
        'id': 'Coin account id', 
        'currency': 'BTC', 
        'balance': '0.0003000058416290', 
        'hold': '0.0000699178500000', 
        'available': '0.000230087991629', 
        'profile_id': 'profile id', 
        'trading_enabled': "True"
    }
    config_object["RIGHTACCOUNT"] = {
        'id': 'Coin account id', 
        'currency': 'USDC', 
        'balance': '100.00', 
        'hold': '0.0000699178500000', 
        'available': '100.00', 
        'profile_id': 'profile id', 
        'trading_enabled': "True"
    }
    config_object["LASTTRADE"] = {
        "time": "2014-11-07T22:19:28.578544Z",
        "trade_id": "74",
        "price": "10.00000000",
        "size": "0.01000000",
        "side": "buy"
    }
    #Write to a file!!
    with open(pathStr,'w') as conf:
        config_object.write(conf)

# Step 3 (Edit That Config File)
        # Save to new data to The Config File we just made
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

# Step 4 (Read That Config File)
# Read the file and assign variables to the values
def ReadConfig(x):
    """x should be what you want from the config file as a string"""
    c = ConfigParser()
    c.read(pathStr)
    #Get Info from config
    API = c["API"]
    return API[x]
    
# 100th line for out config file markinfo = c["MARKETINFO"]
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