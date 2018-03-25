#!/usr/bin/python3
#coding:utf-8
from modules.fundDB import useDB
import cgi,json

udb=useDB()
#state = {"success":"True","code":0}
#respense = json.dumps(state)
lastdata=udb.queryDB('select value,percent,date from fund_tab ORDER by id desc limit 1')[0]
lastValue=lastdata[0]
lastPercent=lastdata[1]
lastDate=lastdata[2].strftime('%Y-%m-%d %H:%M:%S')
state={"lastValue":lastValue,"lastPercent":lastPercent,"lastDate":lastDate}
respense = json.dumps(state)
#print (state)
#print("Content-type:text/html")
print("Content-Type: application/json")
print('')
print(respense)