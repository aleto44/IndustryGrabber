# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import sqlite3 as sql

    
def makeConnection():
    conn = sql.connect('industryGrab.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE if not exists Companies 
          (Ticke6tr text,
          Company text,
          Industry text,
          PRIMARY KEY(`Ticker`)
          )""")
    
    conn.commit()
    return conn, c

def populate_income_statement():
    c.execute("""CREATE TABLE if not exists Income_Statement 
          (Ticker text,
          Year text
          )""")
    
    income_statement = parse_is('tsla')        
    is_names = income_statement[income_statement.columns[0]].tolist()
    
    for name in is_names:
        query = "ALTER TABLE Income_Statement ADD '{}' TEXT".format(name)
        c.execute(query)
        conn.commit()
        


def create_frame(page_number, industry): 

    companies = pd.DataFrame( columns=['Name', 'Symbol', 'Column'])
    for number in range(1,page_number+1):
        url = 'https://www.nasdaq.com/screening/companies-by-industry.aspx?industry={}&page={}'.format(industry, number)
        df = pd.read_html(url)
        df= df[1]
        df.drop(['Market Cap','IPO Year', 'Subsector'], axis=1, inplace = True)
        us = df.loc[df['Country'] == 'United States']
        
        companies = pd.concat([companies, us], sort = False)
    return companies[['Name', 'Symbol']]


def insert(ticker, company, industry):  
    c.execute("INSERT OR REPLACE INTO Companies(Ticker, Company, Industry) VALUES (?,?,?)", (ticker, company, industry))
    conn.commit()
    print('success')
    
def insert_df(df, industry):
    for row in df.iterrows():
        insert(row[1]['Symbol'],row[1]['Name'], industry)
     
        '''
def insert_income_statement(ticker, company, industry):  
    query = ""
    c.execute("INSERT OR REPLACE INTO (Ticker, Company, Industry) VALUES (?,?,?)", (ticker, company, industry))
    conn.commit()
    print('success')
    '''


def parse_is(ticker):
    url = 'https://www.marketwatch.com/investing/stock/{}/financials'.format(ticker)
    
    df = pd.read_html(url)
    
    df[0].drop(['5-year trend'], axis = 1, inplace = True)
    df[1].drop(['5-year trend'], axis = 1, inplace = True)
    
    df[0].columns = ['', '2013','2014','2015','2016','2017']
    df[1].columns = ['', '2013','2014','2015','2016','2017']
    
    return pd.concat([df[0],df[1]])

#def is_to_db(df):
    
    
running = False

conn, c = makeConnection()


while running:
    page_num = int(input('Page number? '))
    industry = input('Industry? ')
    
    df = create_frame(page_num, industry)
    insert_df(df, industry)
    
    keep_going = input('Continue? ')
    
    if keep_going is 'n':
        running = False
        

        

        
    

    


