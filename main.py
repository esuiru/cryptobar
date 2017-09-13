"""
# CODE BY: commit-master 🚀
# MADE ON: Saturday, September 9, 2017
# This macOS app is a simple status bar plugin that allows you to track your
# favourite cryptocurrencies in real time.
"""

import rumps
import requests

API_URL = 'https://api.coinmarketcap.com/v1/ticker/'
VALUES = {}

# Change the values of this array to the coins you are currently tracking.
# You can change the FIAT variable to the desired currency you want to convert
# the cryptos to.
CURRENCIES = ['monetha', '0x', 'ethereum']
FIAT = {'symbol': '$', 'value': 'USD'}

def fetch_api(coin):
    """ This function goes and fetch us the latest coins data """
    resp = requests.get(API_URL + coin + '/?convert=' + FIAT['value'])
    for key in resp.json():
        return [key["symbol"], float(key["price_usd"])]

def check_fluctuation(values):
    if (values[-3][1] > values[-2][1]) and (values[-2][1] > values[-1][1]):
        return '💀'
    elif (values[-2][1] > values[-1][1]):
        return '😱'
    elif (values[-3][1] < values[-2][1]) and (values[-2][1] < values[-1][1]):
        return '🔥'
    elif (values[-2][1] < values[-2][1]):
        return '🚀'
    else:
        return '😐'

class Cryptobar(rumps.App):
    """ This is the core component of the app, this class will be used to build
    all the stuff we need to show in the StatusBar. """
    def __init__(self):
        super(Cryptobar, self).__init__("Loading...")

    @rumps.timer(6 * len(CURRENCIES))
    def ticker(self, _):
        """ This ticker function allows us to update the price in the StatusBar
        every seconds to stay on top of the latest charts. """
        global VALUES

        for coin in CURRENCIES:
            VALUES.setdefault(coin, [])
            if len(VALUES[coin]) == 3:
                VALUES[coin] = VALUES[coin][1:] + [fetch_api(coin)]
                VALUES[coin][-1].append(check_fluctuation(VALUES[coin]))
            else:
                VALUES[coin].append(fetch_api(coin))
                VALUES[coin][-1].append('🤔')

        self.title = '▲  '.join("{0}: {1}{2} 〈{3}〉".format(x[-1][0],
                                                            x[-1][1],
                                                            FIAT['symbol'],
                                                            x[-1][2]) for x in VALUES.values())

if __name__ == "__main__":
    Cryptobar().run()
