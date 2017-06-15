# coding:utf-8 
#
# The MIT License (MIT)
#
# Copyright (c) 2016-2017 yutiansut/QUANTAXIS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from QUANTAXIS.QAFetch import QATushare
from QUANTAXIS.QAUtil import QA_util_date_stamp,QA_Setting,QA_util_date_valid,QA_util_log_info
import json
import pymongo
import datetime
import re
import time

def QA_update_stock_day(name,startDate,endDate):
    data=QATushare.QA_fetch_get_stock_day(name,startDate,endDate)
    
    
def QA_update_stock_day_all(client):
    coll_stocklist=client.quantaxis.stock_list
    stock_list=coll_stocklist.find_one()['stock']['code']
    coll_stock_day=client.quantaxis.stock_day

    for item in stock_list:
        QA_util_log_info('updating stock data -- %s'%item)
        #coll.find({'code':str(item)[0:6]}).count()
        #先拿到最后一个记录的交易日期
        start_date=str(coll_stock_day.find({'code':str(item)[0:6]})[coll_stock_day.find({'code':str(item)[0:6]}).count()-1]['date'])
        end_date=str(datetime.date.today())

        QA_util_log_info('updating from %s to %s' %(start_date,end_date))
        data=QATushare.QA_fetch_get_stock_day(str(item)[0:6],start_date,end_date)[1::]
        try:
            coll_stock_day.insert_many(data)
        except:
            QA_util_log_info('error in updating--- %s'%item)
            


def QA_update_standard_sql():
    print('正在整理和更新数据,请稍等.....')
    coll=pymongo.MongoClient().quantaxis.stock_day
    coll.ensure_index('code')



