import ConfigSetup as cfg
from cbpro import AuthenticatedClient
from time import sleep
import os

class User:
    product_id = str
    auth = None

    def __init__(self):
        self.product_id = input("Please Enter You're Selected Currency Pair.\n") or "BTC-USDC" #Default is btc-usdc

        cfg.BuildBotNest() # Build directory for our data and config files

        if os.path.isfile(cfg.pathStr): # if file is a file! We continue
            sleep(0.33)
        else: 
            print("\nConfig File Not Found!\nBuilding Setup File!\n") # else: we make a file
            cfg.BuildBotSettings()
            print("The Config File Was Created!\n")

        if cfg.ReadConfig("key") == "CoinbaseProAPI key": # Set your api key,
            key = input("Enter API KEY:\n")
            secret = input("Enter API SECRET:\n")
            passphrase = input("Enter API PASSPHRASE:\n")
            cfg.SaveNewApi(key,secret,passphrase)
        else:                                           # Read your already set key
            key = cfg.ReadConfig("key")
            secret = cfg.ReadConfig("b64secret")
            passphrase = cfg.ReadConfig("passphrase")

        self.auth = AuthenticatedClient(key,secret,passphrase)