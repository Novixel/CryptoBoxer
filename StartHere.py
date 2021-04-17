# Welcome To Novixel's Bitcoin Boxer!!
# Version 1 - First Official Release
# April 17, 2021
#
# StartHere.py
#
# Just in time!
from time import sleep
from datetime import datetime
import TheBot

# Starting time for the program!
start = datetime.now()

# Welcome to the danger zone!
print("\n\n\n\t#**    Thank you for choosing Novixel Development Solutions    **#\n\n")
print("\t\tStart Time\t:\t", start)

# Always read the README!

# Enter The Currency Pair You Would Like To Trade With!

CurrencyPair = "BTC-USDC" # <-----  ENTER YOUR CURRENCY PAIR ("BTC-ETH" or "ETH-BTC")!

# This will let you set the currency pair on start up!
if not CurrencyPair:
    product_id = input("Enter The Currency Pair You Would Like To Trade With!") or "BTC-EUR"
    CurrencyPair = product_id
    if product_id == "BTC-EUR":
        print("Default Currency Pair Was Set:",product_id)
    else:
        print("You've selected to trade on:",product_id)

product_id = CurrencyPair

# Bot loops every minute!
# So we want to restart every 2 hours and show our profits
BotLoops = 120

# How long should the bot run for?
Hours = (24 * 365)      # 1 year should be long enough

# Now we start up the bot!
Boxer = TheBot.BOT(product_id) 

# set our starting balance
StartingQuote = Boxer.start_total

# Now we start the main loop and

# Watch the magic happen
while Hours > 0:
    bStart = datetime.now()
    print("\n\tBots Start Time:\t",bStart)
    Boxer.StartTradingLoop(BotLoops)
    bEnd = datetime.now()
    print("\n\tBot loop End Time:\t",bEnd)
    EndingQuote = Boxer.current_total
    print("Total Profit:",EndingQuote - StartingQuote)
    sleep(2)   
else:
    print("\n\t\tStarted at\t:\t",start)
    print("\n\t\tEnded at\t:\t",datetime.now())

print("\n\n\n\t#**    Thank you for choosing Novixel Development Solutions    **#\n\n")