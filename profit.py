import alpaca_trade_api as tradeapi
import requests, sys
from config import *

if __name__ == '__main__':

    sys.stdout.write(GREEN)
    sys.stdout.write(BOLD)

    #api = tradeapi.REST(API_KEY_francisco, SECRET_KEY_francisco, 'https://api.alpaca.markets')
    #account = api.get_account()
    #balance_change = round(float(account.equity) - float(account.last_equity),2)
    #porcentaje = round(100 * (float(float(account.equity) / float(account.last_equity)) -1),2)
    #print(f'Today\'s portfolio profit on francisco  account ({strategy_francisco})                : {balance_change} USD ({porcentaje}%)    Balance: ${float(account.equity)}')


    api = tradeapi.REST(API_KEY_firaagorri, SECRET_KEY_firaagorri, 'https://paper-api.alpaca.markets')
    account = api.get_account()
    balance_change = round(float(account.equity) - float(account.last_equity),2)
    porcentaje = round(100 * (float(float(account.equity) / float(account.last_equity)) -1),2)
    print(f'Today\'s portfolio profit on firaagorri account ({strategy_firaagorri})             : {balance_change} USD ({porcentaje}%)    Balance: ${float(account.equity)}')


    #api = tradeapi.REST(API_KEY_darth, SECRET_KEY_darth, 'https://paper-api.alpaca.markets')
    #account = api.get_account()
    #balance_change = round(float(account.equity) - float(account.last_equity),2)
    #porcentaje = round(100 * (float(float(account.equity) / float(account.last_equity)) -1),2)
    #print(f'Today\'s portfolio profit on darth      account ({strategy_darth})    : {balance_change} USD ({porcentaje}%)    Balance: ${float(account.equity)}')


   # api = tradeapi.REST(API_KEY_slqcctm, SECRET_KEY_slqcctm, 'https://paper-api.alpaca.markets')
   # account = api.get_account()
   # balance_change = round(float(account.equity) - float(account.last_equity),2)
   # porcentaje = round(100 * (float(float(account.equity) / float(account.last_equity)) -1),2)
   # print(f'Today\'s portfolio profit on slqcctm    account ({strategy_slqcctm})               : {balance_change} USD ({porcentaje}%)    Balance: ${float(account.equity)}')


    #api = tradeapi.REST(API_KEY_ellucian, SECRET_KEY_ellucian, 'https://paper-api.alpaca.markets')
    #account = api.get_account()
    #balance_change = round(float(account.equity) - float(account.last_equity),2)
    #porcentaje = round(100 * (float(float(account.equity) / float(account.last_equity)) -1),2)
    #print(f'Today\'s portfolio profit on ellucian   account ({strategy_ellucian})     : {balance_change} USD ({porcentaje}%)    Balance: ${float(account.equity)}')


    #api = tradeapi.REST(API_KEY_outlook, SECRET_KEY_outlook, 'https://paper-api.alpaca.markets')
    #account = api.get_account()
    #balance_change = round(float(account.equity) - float(account.last_equity),2)
    #porcentaje = round(100 * (float(float(account.equity) / float(account.last_equity)) -1),2)
    #print(f'Today\'s portfolio profit on outlook    account ({strategy_outlook})     : {balance_change} USD ({porcentaje}%)    Balance: ${float(account.equity)}')

    print("")
    sys.stdout.write(RESET)
