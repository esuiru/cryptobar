"""
# CODE BY: commit-master 🚀
# MADE ON: Saturday, September 9, 2017
# This macOS app is a simple status bar plugin that allows you to track your
# favourite cryptocurrencies in real time.
"""

import rumps
import requests

# Change the values of this array to the coins you are currently tracking.
CURRENCIES = ['monetha', 'ethereum', 'bitcoin']

def fetch_api(coin):
    """ This function goes and fetch us the latest coins data """
    resp = requests.get('https://api.coinmarketcap.com/v1/ticker/' + coin)
    for key in resp.json():
        return [key["symbol"], key["price_usd"] + "$"]

class Cryptobar(rumps.App):
    """ This is the core component of the app, this class will be used to build
    all the stuff we need to show in the StatusBar. """
    def __init__(self):
        super(Cryptobar, self).__init__("Loading...")

    @rumps.timer(6 * len(CURRENCIES))
    def ticker(self, _):
        """ This ticker function allows us to update the price in the StatusBar
        every seconds to stay on top of the latest charts. """

        k = []
        for coin in CURRENCIES:
            k.append(fetch_api(coin))

        self.title = ' ⚡️ '.join("{0}: {1}".format(x[0], x[1]) for x in k)

if __name__ == "__main__":
    Cryptobar().run()
