# Novixel's Sample Start Script - The Bitcoin Boxer
# Version 0.02 - Pre-Release - Beta Testing
# April 14, 2021
#
# Sample.py
#

# Get the bot
import TheBot
# we always need the cfg

# Set Up Your Test
mypair = "BTC-USDC"
myLoops = 0 # 0 will loop forever

mybot = TheBot.BOT(mypair) # Create the bot with your selected currency pair
start = mybot.start_total

print("\nWe Are Starting With:", start, mybot.quot_ext) #For Debug
mybot.StartTradingLoop(myLoops) # Start Bots Trade Loop With Number of loops
print("\nFinnaly We End With a Total of", mybot.end_total, mybot.quot_ext)
print("we made",start - mybot.end_total, mybot.quot_ext)
