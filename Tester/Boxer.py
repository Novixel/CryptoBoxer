# Novixel's The Crypto Boxer 
# Version 0.01
# April 7, 2021
#
# Custom Trading Bot For (Mosis)
#
# Boxer.py
import ConfigSetup as cfg 
from Connect import CoinConnect
import ViableTrade
import SmartTrade as Smt
import datetime
import cbpro
import time
import os 

product_id = cfg.product_id # Temp
isoNow = datetime.datetime.now().isoformat() 
Coin = CoinConnect()  # Create The Connection,
auth = Coin.auth  #Get The Auth From That Connection And Store it

def StartLoop(x):
    count = 0
    Smt.updateTick() # Fresh data!!
    while x > 0 or x < 0: # Forever Loop if 0
        x -= 1
        count += 1
        
        print("\n\tStep 1 - Gather Data\n")
        time.sleep(.33)

        Smt.updateTick()
        Smt.updateFunds()

        
        mTime = auth.get_time() # 2021-04-07T21:19:25.295Z
        print("\tCurrent Time:\t", isoNow)
        print("\tMarket Time:\t", mTime["iso"])
        print("\tTicker Time:\t",cfg.ReadTICKER("time"))

        print("\n\tStep 2 - Process Data & Calculate trade\n")
        time.sleep(.33)



        time.sleep(.33)
        print("Check available funds\n")
        print(cfg.ReadLEFTaccount("available"),cfg.ReadLEFTaccount("currency"))
        print(cfg.ReadRIGHTaccount("available"),cfg.ReadRIGHTaccount("currency"))
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



        print("\n\tStep 3 - Trade Time!\n") # Magic time
        time.sleep(.33)

        side, last = Smt.getLastTrade() # GET LAST TRADE
        
        Smt.updateTick()

        if side == 'buy': # simple but very effective way to ensure we alternate our trades
            print("our last trade was a",side)
            mytrade = Smt.sellTrade()
        else:
            print("our last trade was a",side)
            mytrade = Smt.buyTrade()

        print(mytrade) # print last trade made for us
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
    StartLoop(1)
    


if __name__ == "__main__":
    main(auth)
