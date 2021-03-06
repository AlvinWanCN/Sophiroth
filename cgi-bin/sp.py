#!/usr/bin/python3
#coding:utf-8
import cgi,subprocess,re,hashlib

print("Content-type:text/html")
print()
data=cgi.FieldStorage()
def md5(alpha):
    return hashlib.md5(alpha.encode('utf-8')).hexdigest()
sp={}
sp['port']=data.getvalue('port')
sp['ip']=data.getvalue('ip')
sp['prot']=data.getvalue('prot')
sp['password']=md5(data.getvalue('password'))

if sp['port'] and sp['ip'] and sp['prot'] and sp['password']:
    if sp['password'] != '20a2495a46e8d2aa6600dec33501326f':
        print('wrong password, please ensure you have permission to access this api.')
        exit(1)
else:
    print('you should specify key and value.')
    exit(1)
iptablesGrepNum='sudo iptables -L INPUT -n --line-number|grep :{port}$|grep {prot}|grep ACCEPT|wc -l'.format_map(sp)
iptablesGrep='sudo iptables -L INPUT -n --line-number|grep :{port}$|grep {prot}|grep ACCEPT'.format_map(sp)
iptablesInsert='sudo iptables -I INPUT -p {prot} --dport {port} -s {ip} -j ACCEPT'.format_map(sp)

while str(subprocess.getoutput(iptablesGrepNum)) != str(0):
    grepResult = subprocess.getoutput(iptablesGrep).split('\n')[0]
    try:
        sp['num'] = re.findall(r'(\d+)\s+ACCEPT', grepResult)[0]
        subprocess.call('sudo iptables -D INPUT {num}'.format_map(sp),shell=True)
    except Exception as e:
        print(e)
        exit(1)
try:
    result = subprocess.call(iptablesInsert,shell=True)
except Exception as e:
    print(e)
    exit(1)
finally:
    if result == 0:
        print('Insertion Success')
    else:
        print('Insertion Failed</br>')
        print(subprocess.getoutput(iptablesInsert))
