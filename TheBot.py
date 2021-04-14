# Main Control Hub THE BOT
import ConfigSetup as cfg
import TheTrader
import time

class BOT:
    """product_id , maxTradeChecks"""
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
        self.start_side, self.start_total, self.quot_ext, self.base_ext = TheTrader.ShouldWeTrade()

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

            # Check The Market 
            check, lower, upper = self.CheckMarket()
            if check: 
                # Check If a trade should be made
                if self.TradeCheck(): # We call this to check a trade
                    print("\nBot is Attempting To Trade!")
                    self.AttemptTrade(lower,upper)
                    time.sleep(30)
                    print("\nTrade Attempt Over")
                    print("Trader is Napping..")
                    time.sleep(30)
                    print("*(theBOSS)SLAMS HAND ON DESK*")
                else:
                    print("\nBot tradecheck failed!")
                    time.sleep(1)
            else:
                print("\nCheck Market Came back false.\nNo tradeChecks were Made")

            # Loop end 
            totalLoops += 1
            print("\n\tloop#:", totalLoops, "/", self.maxLoops)
            print("Bot is having a Nap..")
            time.sleep(30)
            print("*Jumps out of bed*")
        else:
            print("Bot Finished",totalLoops,"Loops")

    def TradeCheck(self):
        print('\nAsking Trader Check If We Can Trade.')
        TradeSide, self.current_total, self.quot_ext, self.base_ext = TheTrader.ShouldWeTrade()
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
        print('\nAsking Trader To Check The Market.')
        check, lower, upper = TheTrader.CheckTheMarket()
        if check:
            return True, lower, upper
        else:
            return False, lower, upper

    def AttemptTrade(self, lower, upper):
        print('\nAsking Trader To Decide.')
        TheTrader.DecideOnTrade(lower,upper)



