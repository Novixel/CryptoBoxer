# Novixel's Smart Trade Fucntions - The Bitcoin Boxer
# Version 0.02 - Pre-Release - Beta Testing
# April 14, 2021
#
# SmartTrade.py
#

import ConfigSetup as cfg
from Connect import CoinConnect as CC

LEFTA, RIGHTA = cfg.product_id.split("-")
lasttrademade = 0.0

Coin = CC()
auth = Coin.auth

def getLastTrade():
    filled = auth.get_fills(cfg.product_id)
    for i in filled:
        lastside = i["side"]
        lastprice = i['price']
        break
    return lastside, float(lastprice)

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
    trade = auth.place_order(
        product_id= product_id,
        side= side, 
        order_type= 'limit',
        price= price , 
        size= size )
    print(trade)
    for k,v in trade.items():
        cfg.SaveTrade(str(k), str(v))


def MarketCheck(): #### THIS DECIDES IF WE EVEN ATTEMPT a trade
    # Is it a good time to trade in this market?
    print("##Checking Market##\nCurrentPrice:", cfg.ReadTICKER("price"))
    print("\n24HOUR last:", cfg.ReadDAYSTATS("last"))
    c = float(cfg.ReadTICKER("price"))   #current price
    h = float(cfg.ReadDAYSTATS("high"))   #current 24hr high
    l = float(cfg.ReadDAYSTATS("low") )  #current 24hr low
    b = ((h + l) / 2) # 24hourBaseLine
    ba = (b / 100) # 1% of that baseline
    bu = ba + b # add 1% of the base to counter sell fee
    bd = b - ba # Minus 1% of the base to counter buy fee
    f = ((b + c) / 2) # BaseLine of price and 24h base
    _,l = getLastTrade()
    ld = c - l # current price minus our last trade price
    ldp = 100 * (ld / c)
    print("\n\nChecking Market At\t", cfg.ReadTICKER("time"), "\n",
        "\n\n\t\t24hourBaseline\t=\t",      "%.8f" % b,
        "\n\n\t\tUpperBounds\t=\t",      "%.8f" % bu,
        "\n\n\t\tLowerBounds\t=\t",      "%.8f" % bd,
        "\n\n\tCurrent Market Price\t=\t",  "%.8f" % c,
        "\n\n\tLast Trade Price\t=\t",  "%.8f" % l,
        "\n\n\tDifference last/cur \t=\t",  "%.2f" % ldp, "%")
    if bd <= c <= bu:
        return False , bd , bu
    else:
        return True, bd , bu
    

    