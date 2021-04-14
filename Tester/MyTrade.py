import TheTrader

trade = TheTrader.ShouldWeTrade()

if trade == 'none':
    print("We cant make any trades")
elif trade == 'both':
    print("We can make ANY Trade we want")
else:
    print("We can make a",trade,"trade")

