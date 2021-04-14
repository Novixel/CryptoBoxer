import TheBot

mypair = "BTC-USDC"
myMax = 10
myAccounts = {}

mybot = TheBot.BOT(mypair)

print("START of sample test! with 10 loops\n\n")
mybot.StartTradingLoop(myMax)