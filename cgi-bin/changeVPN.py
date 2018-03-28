#!/usr/bin/python3
#coding:utf8

import subprocess,cgi
from modules.md5 import md5


print("Content-type:text/html")
print()

data=cgi.FieldStorage
cv={}
cv['type']=data.getvalue('type')
cv['password']=md5(data.getvalue('password'))
if cv['password'] and cv['type'] :
    if cv['password'] != '20a2495a46e8d2aa6600dec33501326f':
        print('wrong password, please ensure you have permission to access this api.')
        exit(1)
else:
    print('you should specify key and value.')
    exit(1)

if cv['type'] not in ('ikv2','l2tp'):
    print('wrong vpn type, just support both of ikev2 and ipsec')
    exit(1)

if cv['type'] == 'l2tp':
    subprocess.call('sudo docker stop ikev2-vpn-server',shell=True)
    subprocess.call('sudo docker start ipsec-vpn-server',shell=True)
    print('l2tp vpn startup')
else:
    subprocess.call('sudo docker stop ipsec-vpn-server',shell=True)
    subprocess.call('sudo docker start ikev2-vpn-server', shell=True)
    print('ikev2 vpn startup')