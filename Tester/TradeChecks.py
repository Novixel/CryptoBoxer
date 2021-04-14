# Trade Checks - BTC Boxer
# By Novixel
#
# TradeChecks.py
# Lets Check If Trading Is A Viable Option

def checkFunds(base,quot): # lets check our balance
    """ BaseAvailable , QuoteAvailable, will return bool int
    bool = true if we have enough, 
    int = what we can trade if any,
    3 is none
    """
    minTrdsize = 0.0001
    minFunamont = 10
    if base > minTrdsize and quot > minFunamont: 
        return True, 0 # we have enough funds in both
    elif quot > minFunamont:
        return True, 1 # we have enough to only buy
    elif base > minTrdsize:
        return True, 2 # only enough to sell
    else:
        return False, 3 # we have no funds

def CanWeTrade(marketPrice, wMovingAvg):
    cur = marketPrice
    wma = wMovingAvg
    canTrade, whatTrade = checkFunds()
    shouldTrade = bool
    def buy():
        if canTrade and whatTrade <= 1:
            # We can Trade and it has to be a buy
            if wma > cur:
                # Moving avg is still up so we can buy But
                # is it still dropping?
                # how much is is dropping
                return True
            else: 
                return False
        else:
            return False

    def sell():
        if canTrade and whatTrade == (2 or 0):
            # We can Trade and it can be a sell 
            if wma < cur:
                # moving avg is Below the current so market is moving up
                # we can trade but should wait for market to stop moving up
                return True
            else: 
                return False
        else:
            return False

    if buy() and sell():
        return print("We Can Trade")
    elif buy() and not sell():
        return print("We Can Only Buy")
    elif sell() and not buy():
        return print("We Can Only Sell")
    else:
        return print("We CANT trade!")
