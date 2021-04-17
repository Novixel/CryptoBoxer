# Novixel's Crypto Trader - The Bitcoin Boxer
# Version 1 - First Official Release - 
# April 17, 2021
#
# TheTrader.py
#

import ConfigSetup as cfg
import SmartTrade

def checkFunds(base,quot): # lets check our balance
    """ BaseAvailable , QuoteAvailable, will return bool int
    bool = true if we have enough, 
    int = what we can trade if any,
    3 is none
    """
    minTrdsize = 0.000100
    minFunamont = 8
    if base >= minTrdsize and quot >= minFunamont: 
        return True, 0 # we have enough funds in both
    elif quot >= minFunamont:
        return True, 1 # we have enough to only buy
    elif base >= minTrdsize:
        return True, 2 # only enough to sell
    else:
        return False, 3 # we have no funds

#Step #2 - Trader Asks data if we are able to trade
def CanWeTrade(current_price, lastTradePrice, lastTradeSide, base_Avail, quote_Avail):
    # Check Funding first!
    tradeFunds, whatTrade = checkFunds(base_Avail,quote_Avail)

    # Second Check For Trade ## Here we can do anything
    # Calculation of if,and,or,but

    # We never want to trade at the same price! 
    # (if market hasnt moved since last trade)
    if lastTradePrice != current_price:
        # Now we can add more!
        if (tradeFunds) and (whatTrade == 0):
            # if we add more too!!
            canTrade = True
            canBuy = True
            canSell = True
            return 'both'
        elif (tradeFunds) and (whatTrade == 1) and lastTradePrice > current_price:
            canTrade = True
            canBuy = True
            canSell = False
            return 'buy'
        elif (tradeFunds) and (whatTrade == 2) and lastTradePrice < current_price:
            canTrade = True
            canBuy = False
            canSell = True
            return 'sell'
        else:
            canTrade = False
            canBuy = False
            canSell = False
            return 'none'
    else:
        print(lastTradePrice," lastTradePrice is the same as current_price", current_price)
        return 'none'
        

# Step #1 - Ask The Trader If We Can Trade!
def ShouldWeTrade():
    # Get Last Trade We Made!
    lastTradeSide, lastTradePrice = SmartTrade.getLastTrade()

    # Update Our Currency Accounts
    SmartTrade.updateFunds()

    # base_Ext = "BTC" / "EUR" = quote_ext
    base_ext = cfg.ReadLEFTaccount("currency")
    quot_ext = cfg.ReadRIGHTaccount("currency")

    # Get Available Balances
    base_Avail = float(cfg.ReadLEFTaccount("available"))
    quote_Avail = float(cfg.ReadRIGHTaccount("available"))

    # Get Current Market Price As of last Tick (*Most Accurate Recent Price)
    current_price = SmartTrade.updateTick()
    
    # How Much of quote does it cost to buy 1 of the base
    exchange_rate = 1 / current_price
    # 
    current_base_total = (exchange_rate * quote_Avail) + base_Avail
    current_quot_total = current_price * current_base_total
    
    # Finally The Trader Uses This Data To Ask if We CAN trade
    # Second Check Before We Trade!!
    # This is the big one
    sides = CanWeTrade( current_price, 
                            lastTradePrice, 
                            lastTradeSide,
                            base_Avail,
                            quote_Avail)

    # DEBUG INFO #
    print("\n# DEBUG INFO : ShouldWeTrade() #\n")
    print("\nOur last trade was a",lastTradeSide,"at the price of",lastTradePrice)
    print("\nOur Balances:\n",base_ext,base_Avail)
    print("\n",quot_ext,quote_Avail)
    print("\nOur Overal Total:",current_quot_total, quot_ext)
    print("\nOur Trading Side:",sides)
    print("\n# DEBUG INFO : ShouldWeTrade() #\n")
    ##############
    cfg.SaveProfit("current_total", str(current_quot_total))
    # return with the trade we can do and some data
    # dont change these unless you know what your doing
    return sides, current_quot_total, quot_ext, base_ext

def CheckTheMarket():
    print('\nTrader is Checking the market.')
    SmartTrade.updateTick()
    SmartTrade.update24Hour()
    SmartTrade.updateFunds()
    # First check # 
    # note: we can add another check in here if needed
    markCheck,lower,upper = SmartTrade.MarketCheck()
    return markCheck , lower, upper

def DecideOnTrade(lower,upper): #Big Function
    # Here we determine our trade details!
    print('\nTrader is Deciding on a Trade.')

    # get Current market price that we saved before this function was called
    cp = float(cfg.ReadTICKER("price")) 

    # we always need the product id constant
    product_id = cfg.product_id 
    diff = (lower + upper) / 2 # middle of our bounds
    difff = diff - cp   # diffrence from the new middle bounds to the current price
    difper = difff / cp * 100 # difference in percent % from the current price

    # Some Debug info fo us
    print("\nFollow Price","%.8f"%(diff),"quote")
    print("\nCurrent Price","%.8f"%(cp),"quote")
    print("\nPrice Difference","%.8f"%(difper),"%")
    print("\nthats about","%.8f"%(difff),"quote")

    # Conversion Calculations!
    m = 1 / cp # 1 quote of the base currency
    n = ( cp * 0.0001) # min trade size of quote(for btc/somthing)
    a = 100 * m # our minimun trade we will accept
    print("\n1 quote of base","%.8f"%(m))
    print("\nMinimum Trade Size","%.8f"%(n))
    print("\nOur Minimum Trade Size is","%.8f"%(a))

    base = float(cfg.ReadLEFTaccount("available"))
    quote = float(cfg.ReadRIGHTaccount("available"))
    # this is the price for the trade normaly current!
    print("\nGeting last filled trade info before we make this trade")
    lastSide, lastPrice = SmartTrade.getLastTrade()

    tinc = cp - lastPrice
    tincP = float("%.8f"%(tinc / lastPrice * 100))
    print("\nDif from Currentprice to lasttradeprice is", tincP, "%")

    price = cp

    myMin = float("%.8f"% (a))

    # Here We Decide On What Kind Of Trade Can Happen

    # this is where we add another moving avg calculation!!
    # if NewMvg < cp:
    #     # this means we can check another number or variable/ kpi or somthing
    #               **  we would add this to the below if or within it

    if lower > cp and quote > a:                                      #### BUY Trade is optimal
        # we ensure we only buy again if we see a better price
        diffDec = lower - cp # the difference from the buy bound to the current price
        percDec = float("%.5f"%(diffDec / cp * 100)) # covert to percentage of current
        side = 'buy' # Set the SIDE of the trade!

        # at this point The Current Price has past our BUY check
        # and the Current Price is Lower then our last Trade price
        # So now we decide if and or what and how much our next 
        # trade should be if we do decide to make a trade!

        # if market is down over 7.0% from our buyline and lower then 
        # the lowest trade made in the past 24hours 
        # we trigger the failsafe and force a SELL TRADE 
        # of *all current base currency* to prevent any furthur loses
        # We then make a BUY Trade for the same price and size that we sold for 
        # this insures that we can buy back in to the market at the same price
        # that we sold for so if the price rises back up again we can 
        # get back to trading 
        if (percDec > 7.0) and cp < float(cfg.ReadDAYSTATS("low")):# Failsafe!
            print("\n",percDec,"!!!Fail Safe Triggerd!!!")
            print("MARKET HAS DROPPED -7 % TODAY!")
            print("INIITIATE FAILSAFE PROTCAL ")
            # we send a request to cancel all trades!
            SmartTrade.auth.cancel_all(product_id)
            # now we send a request to update our funds just incase!! 
            SmartTrade.updateFunds()
            # now we change the size to EVERYTHING we have AVAILABLE
            # In our BASE CURRENCY to prevent any more loss
            size = float(cfg.ReadLEFTaccount("available"))
            side = "sell" # CHANGEING SIDE!!!!!
            print("SENDING FAILSAFE SELL TRADE!!!")
            SmartTrade.makeTrade(product_id, side, price, size)
            print("Creating new buy at that same price!")
            side = "buy"
            SmartTrade.makeTrade(product_id, side, price, size)

        elif (4 <= percDec <= 6.9):
            print("\n",percDec,"Below our lower bounds")
            size = (myMin * 2) * 4 # 800
            SmartTrade.makeTrade(product_id, side, price, size)

        elif (1.5 <= percDec < 3.9) and lastPrice > price:
            print("\n",percDec,"Below our lower bounds")

            size = (myMin * 2)
            print(product_id, side, price, size)
            SmartTrade.makeTrade(product_id, side, price, size)

        elif (0.1 <= percDec < 1.49) and lastPrice > price:
            print("\n",percDec,"Below our lower bounds")
            size = myMin
            print(product_id, side, price, size)
            SmartTrade.makeTrade(product_id, side, price, size)

        else:
            print('\nTrader did not make a Trade.')
            print("\nThe PERCENT CHANGE IS:",percDec)

    # if upper bounds is greater then current price
    if upper < cp and base > myMin:                       ### Sell Trade
        diffInc = cp - upper # the increase from the upper limit
        percInc = diffInc / cp * 100 #Percent of increse
        side = 'sell'
        SmartTrade.updateFunds()
        MaxToSell = base / m 
        # if the price is greater than 10% from our buy bounds
        # we go hard on the paint and make some big buys
        if percInc > 10:
            print(percInc,"ITS BIG BOY TIME!\n")

            Tsize = (myMin * 2) * 5 # 200 x 5 = 1000

            if  (base / 4) <= Tsize <= (base) and lastPrice < price: # Check if we are big boys
                print("Will make 1 REALLY Big Boy Trades!")
                size = (myMin * 2) * 5 * 4 # 4k trade

            elif Tsize > (base / 3) and lastPrice > price: # Check if we are big boys
                print("Will make a 3x Big Boy Trade!")
                size =(myMin * 2) * 5 * 3

            elif Tsize > base and lastPrice > price: # Check if we are big boys
                print("Will make 2x Big Boy Trades!")
                size =(myMin * 2) * 5 * 2

            else: # We make one big boy trade
                print("Will make 1 Big Boy Trade!")
                size = Tsize # 1000 quote of base

            SmartTrade.makeTrade(product_id, side, price, size)

        elif (5 <= percInc <= 9.9):
            print(percInc,"So we make bigger trade\n")
            size = (myMin * 2) * 4 # 200 x 4 = 800
            SmartTrade.makeTrade(product_id, side, price, size)

        elif (1.5 <= percInc <= 4.9) and lastPrice < price:
            print(percInc,"Above our upper bounds\n")
            size = myMin * 2
            SmartTrade.makeTrade(product_id, side, price, size)

        elif (0.1 <= percInc <= 1.49) and lastPrice < price:
            print(percInc,"Above our upper bounds\n")
            size = myMin
            SmartTrade.makeTrade(product_id, side, price, size)
        else:
            print('\nTrader did not make a Trade.')
            print("Beacuse of this:",percInc)
