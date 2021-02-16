import pandas as pd
import os
import time
from datetime import datetime

path = "/Users/swapnilyadav/Desktop/Ml/Dataparsing/intraQuarter"


def key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path+'/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    # print(stocklist)
    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split(
            "/Users/swapnilyadav/Desktop/Ml/Dataparsing/intraQuarter/_KeyStats/")[1].split(':')[0]
        if len(each_file) > 1:
            for file in each_file:
                date_stamp = datetime.strptime(file, "%Y%m%d%H%M%S.html")
                unix_time = time.mktime(date_stamp.timetuple())
                # print(unix_time, date_stamp)

                full_file_path = each_dir+'/'+file
                # print(full_file_path)
                source = open(full_file_path, 'r').read()
                # print(source)
                value = source.split(
                    gather+':</td><td class="yfnc_tabledata1">')[1].split('</td><tr>')[0]

                print(ticker+":", value)

            time.sleep(15)


key_Stats()
