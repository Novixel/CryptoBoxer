# lets get some market data

from configparser import ConfigParser
from Connect import CoinConnect as CC
import ConfigSetup as cfg
from time import sleep
import datetime
import os

product_id = cfg.product_id
LEFTA, RIGHTA = cfg.product_id.split("-")

Coin = CC()
auth = Coin.auth

datPath = (cfg.path + "\data.ini")

def UpdateDataFile(today):
    """Pass in todays date"""
    print("Updating Data for:",today)
    c = ConfigParser()
    c.read(datPath)
    if (product_id + "-" + str(today)) in c:
        print(today,"was found")
    else: # the reuse of knowledge here is beacause i didnt want to change the entire get function
        #print("Today's Data not found, Updating data for:", today) 
        dayData = auth.get_product_historic_rates(product_id,today,today)
        datCon = {}
        count = 0
        c.add_section(section=(product_id + "-" + str(today)))
        for evry in dayData:
            for val in evry:
                count +=1
                if count == 1: 
                    key = "time"
                if count == 2:
                    key = "low"
                if count == 3:
                    key = "high"
                if count == 4:
                    key = "open"
                if count == 5:
                    key = "close"
                if count == 6:
                    key = "volume"
                c.set((product_id + "-" + str(today)),str(key),str(val))
        with open(datPath, 'w') as conf:
            c.write(conf)


def checkData(date,item):
    """ 
        date = must be in this format: YYYY-MM-DD,
        item = must be a string!,
    Items to Choose From:
        'time', 'low', 'high', 'open', 'close', 'volume'
    """
    c = ConfigParser()
    c.read(datPath)
    thisdate = product_id + "-" + str(date)
    if c.has_section(thisdate):
        day = c[thisdate]
        item = day[item]
        return item
    else:
        UpdateDataFile(date)
        sleep(.33)
        c.read(datPath)
        day = c[thisdate]
        item = day[item]
        return item

def BuildDataSettings(day,data):
    config_object = ConfigParser()
    config_object[product_id + "-" + str(day)] = data # THIS TOOK FOREVER
    with open(datPath, 'a') as conf:
        config_object.write(conf)
    
def GetHistoryData(now):
    print("\nGetting last 30 Days from today:", now)
    sleep(.33)
    then = now - datetime.timedelta(days=30) # get last 30 days
    print("\nTime Traveled to:",then)
    while now > then:
        dayData = auth.get_product_historic_rates(product_id,then,then)
        datCon = {}
        count = 0
        for evry in dayData:
            for val in evry:
                count +=1
                if count == 1: # lol couldnt find a better solution
                    key = "time"
                if count == 2:
                    key = "low"
                if count == 3:
                    key = "high"
                if count == 4:
                    key = "open"
                if count == 5:
                    key = "close"
                if count == 6:
                    key = "volume"
                datCon[key] = str(val)
        then = then + datetime.timedelta(days=1)
        yield then, datCon

def SaveHistoryData():
    now = datetime.datetime.now()
    now.strptime(str(now),"%Y-%m-%d %H:%M:%S.%f")
    for day,data in GetHistoryData(now.date()):
        BuildDataSettings(day,data)
        print(day,"- Saving -",product_id,"\n")
        sleep(3)

def main():
    if os.path.isfile(datPath):
        print("Data File Found!\n")
        sleep(.33)
        print("Checking Data!\n")
    else:
        print("File Not Found!\n\nCreating File\n")
        SaveHistoryData()
        print("Finished Saving Data To File!\n")
        sleep(.33)
        print("Now We Can Check Data!\n")
    print("\nMarket Data Finalized\n")

if __name__ == "__main__":
    main()
    #UpdateDataFile(datetime.datetime.now())
