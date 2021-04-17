# Novixel's Smart Trade Fucntions - The Bitcoin Boxer
# Version 1 - First Official Release - 
# April 17, 2021
#
# SmartTrade.py
#

import ConfigSetup as cfg
from Connect import CoinConnect as CC

Coin = CC()
auth = Coin.auth

def getLastTrade():
    filled = auth.get_fills(cfg.product_id)
    lastside = "buy"
    lastprice = 0
    for i in filled:
        i = i
        lastside = i["side"]
        lastprice = i['price']
        break
    return lastside, float(lastprice)

def updateFunds():
        LEFTA, RIGHTA = cfg.product_id.split("-")
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
        tick = auth.get_product_ticker(cfg.product_id)
        for k,v in tick.items():
            cfg.SaveTicker(str(k), str(v))
        return float(tick["price"])

def update24Hour():
        day = auth.get_product_24hr_stats(cfg.product_id)
        for k,v in day.items():
            cfg.SaveDay(str(k), str(v))
        

def makeTrade(product_id, side, price, size):
    """Final Stop Where the trade is made with SIDE,SIZE,AMOUNT"""
    global trade
    print("Sending",side,"Request Of",size,"at",price,(cfg.ReadRIGHTaccount("currency")))
    trade = auth.place_order(
        product_id= product_id,
        side= side, 
        order_type= 'limit',
        price= price , 
        size= size )
    print("\nLast Trade Attempt Results:\n")
    for k,v in trade.items():
        print(k, "=", v)
        cfg.SaveTrade(str(k), str(v))

# first check 
def MarketCheck(): #### THIS DECIDES IF WE EVEN ATTEMPT a trade
    # basicly if this is false !
    # the market has been stable for the past 24 hours
    # and that means no trade attempts where made
    # Is it a good time to trade in this market?
    print("\nMarketCheck()\n")
    print("\n24HOUR last:", cfg.ReadDAYSTATS("last"))
    c = float(cfg.ReadTICKER("price"))   #current price
    h = float(cfg.ReadDAYSTATS("high"))   #current 24hr high
    lo = float(cfg.ReadDAYSTATS("low") )  #current 24hr low
    s,l = getLastTrade()
    bl = ((h + lo) / 2) # 24hourBaseLine
    b = ((bl + l) / 2)
    ba = (b * 0.009) # 0.90% of that baseline
    bu = ba + b # add 1% of the base to counter sell fee
    bd = b - ba # Minus 1% of the base to counter buy fee

    f = ((b + c) / 2) # BaseLine of price and 24h base
    ld = c - l # current price minus our last trade price
    ldp = 100 * (ld / c)

    # DEBUG INFO .... But very useful
    print(  "\n\n\tChecking Market At\t", cfg.ReadTICKER("time"),"\n",
            "\n\n\t\tUpperBounds\t=\t",      "%.8f" % bu,
            "\n\n\t\tCenterBounds\t=\t",      "%.8f" % b,
            "\n\n\t\tLowerBounds\t=\t",      "%.8f" % bd,
            "\n\n\tOur Last Trade Price\t=\t",  "%.8f" % l,
            "\n\n\tOur Last Trade Side\t=\t", s,
            "\n\n\tCurrent Market Price\t=\t",  "%.8f" % c,
            "\n\n\tDifference From Last \t=\t",  "%.4f" % ldp,"%")
    # CHOOO! CHOOO! ALL ABORD! ... i mean ... DING! DING! Round 1!
    # Last Stop For Our First Market Check
    # if current price is within our bounds the market is stable
    # This is where we decide whether to Sting Like A Bee
    # or To Hold back and float like a butterfly !
    if bd <= c <= bu:
        print("\n- MarketCheck - False \n")
        return False , bd , bu
    else:
        print("\n- MarketCheck - True \n")
        return True, bd , bu
    

    