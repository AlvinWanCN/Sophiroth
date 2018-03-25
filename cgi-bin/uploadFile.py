#!/usr/bin/python3
#conding:utf-8
import cgi,json
data=cgi.FieldStorage()
#all=data.getvalue(all())
text=data.getvalue('text')
file=data.getvalue('file')


#success['dateType']=type(tdate)


#lastdata=udb.queryDB()
#print("Content-type:text/html")
print("Content-Type: text/html")
print()
print('test is %s, file is %s'%(text,file))