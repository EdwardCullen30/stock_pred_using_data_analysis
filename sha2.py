import pandas as pd
import os
import time
from bs4 import BeautifulSoup
from datetime import datetime

path = "/Users/swapnilyadav/Desktop/Ml/Dataparsing/intraQuarter"


def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path + '/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns=['Date', 'Unix', 'Ticker', 'DE ratio'])

    sp500_df = pd.read_csv("GSPC.csv")
    # print(sp500_df)

    for each_dir in stock_list[1:25]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split(
            "/Users/swapnilyadav/Desktop/Ml/Dataparsing/intraQuarter/_KeyStats/")[1].split(':')[0]
        if len(each_file) > 0:
            for file in each_file:
                try:
                    date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                    unix_time = time.mktime(date_stamp.timetuple())
                except Exception as e:
                    pass

                full_file_path = each_dir + '/' + file

                source = open(full_file_path, 'r',
                              encoding="utf8", errors='ignore').read()
                source1 = BeautifulSoup(source, "html.parser")
                # print(source)
                try:
                    value = float(source1.body.find(
                        text='Total Debt/Equity (mrq):').findNext('td').text)
                    stock_price = float(source.split(
                        '</small><big><b>')[1].split('</b></big>')[0])
                    # print(stock_price , ticker)
                    # sp500_date=datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                    # print(sp500_date)
                    # row=sp500_df[sp500_df['index']==sp500_date]
                    # print(row)

                    # try:
                    #     # print(sp500_df)
                    #     sp500_date = datetime.fromtimestamp(
                    #     unix_time).strftime('%Y-%m-%d')
                    #     # print(sp500_date)
                    #     row = sp500_df[(sp500_df.index == sp500_date)]
                    #
                    #     sp500_value = float(row["Adj Close"])
                    #     print(sp500_value)
                    #
                    # except:
                    #     sp500_date = datetime.fromtimestamp(
                    #     unix_time - 259200).strftime('%Y-%m-%d')
                    #     row = sp500_df[(sp500_df.index == sp500_date)]
                    #     sp500_value = float(row["Adj Close"])

                    df = df.append({'Date': date_stamp, 'Unix': unix_time,
                                    'Ticker': ticker, 'DE ratio': value}, ignore_index=True)

                    # print(date_stamp ,unix_time,value , ticker)
                except Exception as e:
                    pass
                # print(ticker+':', value)
    save = gather.replace(' ', '').replace(')', '').replace(
        '(', '').replace('/', '') + ('.csv')
    print(save)
    df.to_csv(save)


Key_Stats()
