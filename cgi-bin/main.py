#!/usr/bin/python3
#coding:utf-8
import modules.get_weather as get_weather
import os,time,cgi,hashlib
indexDick={}
def md5(alpha):
    return hashlib.md5(alpha.encode('utf-8')).hexdigest()
data = cgi.FieldStorage()
username = data.getvalue("username")
password = md5(data.getvalue("password"))
if username == 'alvin' and password == '20a2495a46e8d2aa6600dec33501326f':
    auth = True
else:
    auth = False

weather={}
weather['weatherStatus']=get_weather.get_status()
weather['weatherMax']=get_weather.get_max_temperature()
weather['weatherMin']=get_weather.get_min_temperature()
filename=os.path.join(os.path.dirname(__file__),'../html/main.html')
htmlfile=open(filename,'r',encoding='UTF-8')
htmlcontent=htmlfile.read()
htmlfile.close()

indexDick['nowTime']=time.strftime('%Y-%m-%d %H:%M:%S')
indexDick.update(weather)
print("Content-type:text/html")
print()
if auth:
    print(htmlcontent.format_map(indexDick))
else:
    print('username or password error')