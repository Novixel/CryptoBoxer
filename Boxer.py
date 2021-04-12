# Novixel's Crypto Boxer 
# Version 0.01
# April 7, 2021
#
# Custom Trading Bot For (Mosis)
#
# Boxer.py
import ConfigSetup as cfg 
from Connect import CoinConnect
import ViableTrade
import datetime
import cbpro
import time
import os 

product_id = "BTC-EUR" # Change ME To the pair you would like to watch
LEFTA, RIGHTA = product_id.split("-")

isoNow = datetime.datetime.now().isoformat() 
auth = CoinConnect().auth # Create The Connection, Get The Auth From That Connection And Store it

def updateFunds():
        funds = auth.get_accounts()
        x = -1
        for i in funds:
            x += 1
            for k,v in i.items():
                if v == LEFTA:
                    lefta = funds[x]
                    for b,t in lefta.items():
                        cfg.SaveLeftAccount(str(b),str(t))
                elif v == RIGHTA:
                    righta = funds[x]
                    for u,d in righta.items():
                        cfg.SaveRightAccount(str(u),str(d))

def updateTick():
        tick = auth.get_product_ticker(product_id)
        for k,v in tick.items():
            cfg.SaveTicker(str(k), str(v))

def StartLoop(x):
    count = 0
    while x > 0 or x < 0: # Forever Loop if 0
        x -= 1
        count += 1
        
        print("\n\tStep 1 - Gather Data\n")
        time.sleep(.33)

        updateTick()
        updateFunds()
        mTime = auth.get_time() # 2021-04-07T21:19:25.295Z
        print("\tCurrent Time:\t", isoNow)
        print("\tMarket Time:\t", mTime["iso"])
        print("\tTicker Time:\t",cfg.ReadTICKER("time"))

        print("\n\tStep 2 - Process Data & Calculate trade\n")
        time.sleep(.33)

        print("If the Current Price is 1 BTC For",cfg.ReadTICKER("price"),RIGHTA)
        time.sleep(.33)
        print("Check if we have enough funds available for our trade")
        print(cfg.ReadLEFTaccount("available"),cfg.ReadLEFTaccount("currency"))
        print(cfg.ReadRIGHTaccount("available"),cfg.ReadRIGHTaccount("currency"))
        print("if we do! is the trade Viable, Else: We wait for market to change",)
        time.sleep(.33)

        print("Checking if the market is viable for trade")

        mva = ViableTrade.GetData(15)
        print("Current Price:",cfg.ReadTICKER("price"))
        time.sleep(.33)
        if float(mva) > float(cfg.ReadTICKER("price")):
            print("Moving avg Is Above the current price")
        else:
            print("Moving Avg is Below The Current Price")
        time.sleep(.33)
        print("\n\tStep 3 - Trade Time!\n")
        time.sleep(.33)

        print("\n INSERT TRADE CONSOLE OUTPUT HERE! \n")
        time.sleep(.33)
        
        print("\n\tWaiting..")
        for i in range(1,11):
            print(i)
            time.sleep(.98)
        print("\n\nloop Restarting\n\n")
        

def main(auth):
    print("Our Time:", isoNow)
    time.sleep(.33)
    mTime = auth.get_time() # 2021-04-07T21:19:25.295Z
    print("Market Time:", mTime["iso"])
    time.sleep(.33)
    StartLoop(input("How Many Times Should We loop?(int)\n"))
    


if __name__ == "__main__":
    main(auth)
