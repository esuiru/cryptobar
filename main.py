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
CURRENCIES = ['monetha', 'ethereum', 'bitcoin']
FIAT = {'symbol': '$', 'value': 'USD'}

def fetch_api(coin):
    """ This function goes and fetch us the latest coins data """
    resp = requests.get(API_URL + coin + '/?convert=' + FIAT['value'])
    for key in resp.json():
        return [key["symbol"], float(key["price_usd"])]

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
        previous_values = dict(VALUES)

        for coin in CURRENCIES:
            VALUES[coin] = fetch_api(coin)
            previous_values.setdefault(coin, VALUES[coin])

            fluctuation = '😱' if previous_values[coin][1] > VALUES[coin][1] \
                          else '🚀' if previous_values[coin][1] < VALUES[coin][1] \
                          else '😐'

            VALUES[coin].append(fluctuation)

        self.title = '▲  '.join("{0}: {1}{2} 〈{3}〉".format(value[0],
                                                            value[1],
                                                            FIAT['symbol'],
                                                            value[2]) for value in VALUES.values())

if __name__ == "__main__":
    Cryptobar().run()
