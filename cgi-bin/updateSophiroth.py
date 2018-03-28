#!/usr/bin/python3
#-*-coding:utf-8-*-
import subprocess
print("Content-type:text/html")
print()

a=subprocess.call('/home/alvin/bin/syncsophiroth.py',shell=True)
if str(a) == '0':
    print('update success')
else:
    print('update may not success')