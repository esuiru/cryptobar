"""
# CODE BY: commit-master 🚀
# MADE ON: Saturday, September 9, 2017
# Lorem ipsum et dolor amet. Su colores et un ich bin un berliner ya
# du bist la description of el project right there.
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'iconfile': './assets/app_logo.icns',
    'packages': ['rumps', 'requests'],
}

setup(
    name="Cryptobar",
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)