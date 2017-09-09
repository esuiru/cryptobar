# Cryptobar

## What's that
Cryptobar is a macOS status bar app that track your favorite cryptocurrencies 🚀.

It looks like the following:
![preview](./assets/preview.png)

You can track all your favorite cryptocurrences in **real time** within the blink of an eye to keep your producitivity.

## Installation

```
$ g clone git@github.com:commit-master/cryptobar.git
$ cd cryptobar
$ python3 setup.py py2app -A
```

A `dist` folder has been created and contain the basic app (the same as the one provided within the repository).

In order to track other cryptocurrencies, open `main.py` with your favorite editor and edit the following:

```python
(l.12) CURRENCIES = ['monetha', 'ethereum', 'bitcoin']
```

Change this list with any cryptocurrency you want that is listed on https://coinmarketcap.com/assets/.

Then you will need to build the app again:
```
$ python3 setup.py py2app -A
```

## Other
This README is a work in progress.

If you have any questions, or want to contribute to this repository, open up an issue, I'd be glad to answer it.