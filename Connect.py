import cbpro
import ConfigSetup as cfg
import os
from time import sleep

class CoinConnect:
    def __init__(self): # Set up

        print("\nCoinConnecting...\n")

        sleep(0.33)
        cfg.BuildBotNest() # Build directory for our data and config files

        if os.path.isfile(cfg.pathStr): # if file is a file! We continue
            print("Config File Found!")
            sleep(0.33)
        else: 
            print("File Not Found!\nBuilding Setup File!\n") # else: we make a file
            sleep(0.33)
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

        self.auth = cbpro.AuthenticatedClient(key,secret,passphrase)
