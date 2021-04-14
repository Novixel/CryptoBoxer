# Novixel Viable Trade Calculations
# 
#
import MarketData as MD
from datetime import timedelta, datetime
from time import sleep

# lets get some data 

namlist = ['time', 'low', 'high', 'open', 'close', 'volume']
templist = []


def WMA(days):
    weights = []
    avglist = []
    count = 1
    select = 0
    templist.reverse()
    for i in range(5):
        weights.append(count)
        weight = weights[select] / (days)
        #print("Date Item#:",weights[select])
        #print("Closing price",templist[select])
        #print("Weighting:",weight)
        result = templist[select] * weight
        avglist.append(result)
        count += 1
        select += 1
        #print("Weighted average",result)
    print("\nWMA:",sum(avglist))
    return sum(avglist)

def UseData(x):
    global templist
    ma = []
    ma.append(x)
    templist.append(float(x))
    

def ReadData(lastdate):
    AllData = {}
    for i in namlist: # this will get all the info we need
        AllData[i] = MD.checkData(lastdate,i)
        TEMP = AllData
    t = TEMP['time']
    l = TEMP['low']
    h = TEMP['high']
    o = TEMP['open']
    c = TEMP['close']
    v = TEMP['volume']
    return l,h,o,c,v

def GetData(days):
    """How many far back should we look (Max:30)"""
    now = datetime.now() # get today!
    nowdate = now.date() - timedelta(days=1)
    if days == 1:
        lastdate = nowdate
    else:
        lastdate = nowdate - timedelta(days=int(days))
        
    #Loops for data
    while lastdate <= nowdate:
        lastdate = lastdate + timedelta(days=1)
        low,high,dayopen,dayclose,volume, = ReadData(lastdate)
        UseData(dayclose)
        sleep(.33)
    else:
        return WMA(days)


if __name__ == "__main__":
    mva = GetData(15)
