# Novixel's Smart Trader - The Bitcoin Boxer
# Version 0.02 - Pre-Release - Beta Testing
# April 14, 2021
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
    minFunamont = 10
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
    # Check Funding Calculations
    tradeFunds, whatTrade = checkFunds(base_Avail,quote_Avail)

    # Calculation of if,and,or,but
    if lastTradePrice != current_price: 
        if (tradeFunds) and (whatTrade == 0):
            canTrade = True
            canBuy = True
            canSell = True
            return 'both'
        elif (tradeFunds) and (whatTrade == 1):
            canTrade = True
            canBuy = True
            canSell = False
            return 'buy'
        elif (tradeFunds) and (whatTrade == 2):
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

    # base_Ext = "BTC"/"EUR" = quote_ext
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
    whatTrade = CanWeTrade( current_price, 
                            lastTradePrice, 
                            lastTradeSide,
                            base_Avail,
                            quote_Avail)

    # DEBUG INFO #
    print("\n\t# DEBUG INFO : ShouldWeTrade() #\n")
    print("\nOur last trade was a",lastTradeSide,"at the price of",lastTradePrice)
    print("\nWe Have:\n\t",base_ext,base_Avail)
    print("\t",quot_ext,quote_Avail)
    print("\nTotal:",current_quot_total, quot_ext)
    print("\nThe Current Market Price is:",current_price)
    print("\nOur Trading Side Option:",whatTrade)
    print("\n\t# DEBUG INFO : ShouldWeTrade() #\n\n")
    ##############

    #return with the trade we can do 
    return whatTrade, current_quot_total, quot_ext, base_ext

def CheckTheMarket():
    print('\nTrader is Checking the market.')
    SmartTrade.updateTick()
    SmartTrade.update24Hour()
    SmartTrade.updateFunds()
    markCheck,lower,upper = SmartTrade.MarketCheck()
    return markCheck , lower, upper

def DecideOnTrade(lower,upper): #Big Function
    print('\nTrader is Deciding on a Trade.')
    cp = float(cfg.ReadTICKER("price"))
    product_id = cfg.product_id
    price = cp
    if lower > cp: #### BUY Trade
        diffDec = lower - cp # the decrease from the lower bound
        percDec = diffDec / cp * 100
        side = 'buy'
        if percDec >= 5:
            print("5% Below our lower bounds\n",percDec)
            size = 0.0003
            SmartTrade.makeTrade(product_id, side, price, size)
        elif percDec >= 4:
            print("4% Below our lower bounds\n",percDec)
            size = 0.00025
            SmartTrade.makeTrade(product_id, side, price, size)
        elif percDec >= 3:
            print("3% Below our lower bounds\n",percDec)
            size = 0.0002
            SmartTrade.makeTrade(product_id, side, price, size)
        elif percDec >= 2:
            print("2% Below our lower bounds\n",percDec)
            size = 0.00015
            SmartTrade.makeTrade(product_id, side, price, size)
        elif percDec >= 1 and cfg.ReadLASTTRADE("side") != "buy":
            print("1% Below our lower bounds\n",percDec)
            size = 0.0001
            SmartTrade.makeTrade(product_id, side, price, size)
        else:
            print(percDec)
    else: ### Sell Trade
        diffInc = cp - upper # the increase from the upper limit
        percInc = diffInc / cp * 100 #Percent of increse
        side = 'sell'
        if percInc >= 5:
            print("5% Above our upper bounds\n", percInc)
            size = 0.0003
            SmartTrade.makeTrade(product_id, side, price, size)
        elif percInc >= 4:
            print("4% Above our upper bounds\n", percInc)
            size = 0.00025
            SmartTrade.makeTrade(product_id, side, price, size)
        elif percInc >= 3:
            print("3% Above our upper bounds\n", percInc)
            size = 0.0002
            SmartTrade.makeTrade(product_id, side, price, size)
        elif percInc >= 2:
            print("2% Above our upper bounds\n", percInc)
            size = 0.00015
            SmartTrade.makeTrade(product_id, side, price, size)
        elif percInc >= 1 and cfg.ReadLASTTRADE("side") != "sell":
            print("1% Above our upper bounds\n", percInc)
            size = 0.0001
            SmartTrade.makeTrade(product_id, side, price, size)
        else:
            print(percInc)
        # product_id, side, price, size
        #SmartTrade.makeTrade()
