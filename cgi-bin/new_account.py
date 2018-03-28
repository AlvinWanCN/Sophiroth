#!/usr/bin/python3
#coding:utf-8
import cgi
from modules.alphaDB import useDB
from modules.md5 import md5

udb=useDB()
print("Content-type:text/html")
print()

data=cgi.FieldStorage()
new_account={}
new_account['app']=data.getvalue('app')
new_account['username']=data.getvalue('username')
new_account['password']=data.getvalue('password')
new_account['comment']=data.getvalue('comment')
new_account['acp']=md5(data.getvalue('acp'))

if new_account['app'] and new_account['username'] and new_account['password'] and new_account['acp']:
    if new_account['acp'] != '20a2495a46e8d2aa6600dec33501326f':
        print('wrong password, please ensure you have permission to access this api.')
        exit(1)
    new_account['insert_result']=udb.insertDB(new_account['username'],new_account['password'],new_account['app'],new_account['comment'])
    new_account['result'] ='{app}的{username}账号已存储到数据库。{insert_result}'.format_map(new_account)
else:
    new_account['result']='缺少关键内容，application,username,password,acp 是必填项。'
#print(new_account)
html="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>添加新账号结果</title>
</head>
<body>
    {result}
</body>
</html>
"""
#print("Content-Type: application/json")

print(html.format_map(new_account))