#!/usr/bin/python3
#coding:utf-8
from modules.fundDB import useDB
import cgi,json

udb=useDB()
data = cgi.FieldStorage()
value = data.getvalue("value")
percent = data.getvalue("percent")
date=data.getvalue("date")
success = {"success":"True","code":0}
fail = {"success":"False","code":1}

#success['dateType']=type(tdate)
print (success)
if value and percent and date:
    udb.insertDB(value,percent,date)
    respense = json.dumps(success)
else:
    respense = json.dumps(fail)
#lastdata=udb.queryDB()
#print("Content-type:text/html")
print("Content-Type: application/json")
print()
print(respense)