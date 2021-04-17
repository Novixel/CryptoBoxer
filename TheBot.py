# Novixel's Trade Bot - The Bitcoin Boxer
# Version 1 - First Official Release - 
# April 17, 2021
#
# TheBot.py
#

import ConfigSetup as cfg
import TheTrader
import time

class BOT:
    """def __init__(self,product_id), product_id= str , maxLoops = int"""
    product_id = str
    maxLoops = int
    start_total = float
    start_side = str
    current_total = float
    base_ext = str
    quot_ext = str

    def __init__(self,product_id):
        self.product_id = product_id
        cfg.product_id = self.product_id
        self.start_side, total, self.quot_ext, self.base_ext = TheTrader.ShouldWeTrade()
        self.start_total = total
        cfg.SaveProfit("start_total", str(total))

    def StartTradingLoop(self, maxLoops):
        """Start The Trade Loop Forever Loop if 0"""
        totalLoops = 0
        self.maxLoops = maxLoops
        while self.maxLoops > totalLoops or self.maxLoops == 0:
            # Start of Trade Loop
            if self.maxLoops == 0 and totalLoops == 0:
                print("\nBot looping forever.")
            elif self.maxLoops > 0 and totalLoops == 0:
                print("\nBot Starting loop 0/", self.maxLoops, )

            # Check The Market and grab our bounds!
            check, lower, upper = self.CheckMarket()
            # First check for our trade ^
            if check: # We can add some extra variables here!!
                print("\n\tThe market is looking good")
                # Second check for our trade!
                if self.TradeCheck():
                    # The Trader checked the market and said we can trade!
                    cfg.SaveProfit("current_total", str(self.current_total))
                    print("\n\tBot asks Trader to make a trade!\nPlease Wait..\n")
                    # bring our bounds with us for the trade!
                    self.AttemptTrade(lower,upper)
                else:
                    # the trader said we cant make a trade right now
                    print("\n\tBut The Trader said it's not a good time to trade!")
            else:
                print("\n\tMarket is Stable\n")

            # Loop end 
            totalLoops += 1
            print("\n\tloop#:", totalLoops, "/", self.maxLoops)
            print("\nLoop Has Finished.\n\tNow we wait 1 min if no trades where made")
            start = float(cfg.ReadProfit("start_total"))
            end = float(cfg.ReadProfit("current_total"))
            profit = start - end
            proPerc = profit / end * 100 
            print("\nCurrent Total Profit:\t",profit,self.quot_ext,"\n\tAbout:","%.2f"%proPerc,"%")
            time.sleep(59)
            print("\n\t*Jumps out of bed*")
        else:
            start = float(cfg.ReadProfit("start_total"))
            end = float(cfg.ReadProfit("current_total"))
            profit = start - end
            proPerc = profit / end * 100 
            print("\nTotal Profit:\t",profit,self.quot_ext,"\n\tAbout:","%.2f"%proPerc,"%")
            print("\n\tFinished",totalLoops,"Loops\n")

    def TradeCheck(self):
        # We ask the trader if we can trade!
        TradeSide, self.current_total, self.quot_ext, self.base_ext = TheTrader.ShouldWeTrade()
        print("\nOur Current Total:", self.current_total, self.quot_ext)
        if TradeSide == "both":
            print("\nWe Can buy or sell")
            print("\nWe Have",self.current_total,self.quot_ext,"to trade with")
            return True
        elif TradeSide == "none":
            print("\nCANT make any trades right now")
            print("\nWe only Have",self.current_total,self.quot_ext,"in TOTAL")
            return False
        else:
            print("\nWe can only",TradeSide)
            print("\nWe Have",self.current_total,self.quot_ext,"to trade with")
            return True

    def CheckMarket(self):
        # We ask the trader to check the market
        print('\nAsking Trader To Check The Market.')
        check, lower, upper = TheTrader.CheckTheMarket()
        if check:
            return True, lower, upper
        else:
            return False, lower, upper

    def AttemptTrade(self, lower, upper):
        print('\nAsking Trader To Decide.')
        # Here is where the bot can do another check!!
        # placeholder if upper is greater then lower bounds
        if upper > lower:
            TheTrader.DecideOnTrade(lower,upper)
        else:
            # theoretically impossible but yeah never know
            print("I have no idea how we got here")



