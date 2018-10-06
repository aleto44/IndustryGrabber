# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


api_key = 'AIzaSyCYdVpmMbbCniIRKM3Gtwtsdwr_wQVYFEU'

#ticker = input('Ticker? ')
ticker = 'amd'

url = 'https://www.marketwatch.com/investing/stock/{}/financials'.format(ticker)


df = pd.read_html(url)

df[0].drop(['5-year trend'], axis = 1, inplace = True)
df[1].drop(['5-year trend'], axis = 1, inplace = True)

df[0].columns = ['', '2013','2014','2015','2016','2017']
df[1].columns = ['', '2013','2014','2015','2016','2017']

df = pd.concat([df[0],df[1]])

