#!/usr/bin/python3
#coding:utf-8
import cgi,os,subprocess,re

data=cgi.FieldStorage()
sp={}
sp['port']=data.getvalue('port')
sp['ip']=data.getvalue('ip')
sp['prot']=data.getvalue('prot')
iptablesGrepNum='sudo iptables -L -n --line-number|grep {ip}|grep {port}|grep {prot}|wc -l'.format_map(sp)
iptablesGrep='sudo iptables -L -n --line-number|grep {ip}|grep {port}|grep {prot}'.format_map(sp)
iptablesInsert='sudo iptables -I INPUT -p {prot} --dport {port} -s {ip} -j ACCEPT'.format_map(sp)

grepNumResult=subprocess.getoutput(iptablesGrepNum)
grepResult=subprocess.getoutput(iptablesGrep).split('\n')

if grepNumResult != 0:
    for i in grepResult:
        sp['num']=re.findall(r'(\d+)\s+ACCEPT',i)
        subprocess.call('iptables -D INPUT {num}'.format_map(sp))

result = subprocess.call(iptablesInsert)




print("Content-type:text/html")
print()
if result == 0:
    print('Insertion Success')
else:
    print('Insertion Failed')