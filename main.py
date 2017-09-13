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
        return [key["symbol"], float(key["price_usd"]), float(key["price_btc"])]

def check_fluctuation(values):
    """ returns an emoji according to the fluctuation of each cryptocurrency
    the user is tracking. """
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
        self.menu = [MenuItem('Use BTC metric', callback=self.convert_currency, key='B'), None]

    def convert_currency(self, _):
        """ Small function to convert from FIAT currency to BTC currency. """
        global FIAT
        if FIAT['value'] == 'BTC':
            _.title = 'Use BTC metric'
            FIAT['value'] = 'USD'
            FIAT['symbol'] = '$'

        else:
            _.title = 'Use USD metric'
            FIAT['value'] = 'BTC'
            FIAT['symbol'] = '₿'

        self.update_values(_)

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

        self.update_values(_)

    def update_values(self, _):
        """ This function will print the correct title according to the chosen
        currency to display. """
        if FIAT['value'] == 'BTC':
            self.title = '▲  '.join("{0}: {1:.8f}{2} 〈{3}〉".format(x[-1][0],
                                                            x[-1][2],
                                                            FIAT['symbol'],
                                                            x[-1][3]) for x in VALUES.values())
        else:
            self.title = '▲  '.join("{0}: {1}{2} 〈{3}〉".format(x[-1][0],
                                                            x[-1][1],
                                                            FIAT['symbol'],
                                                            x[-1][3]) for x in VALUES.values())


if __name__ == "__main__":
    Cryptobar().run()
