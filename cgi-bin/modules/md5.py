#!/usr/bin/python
import hashlib
def md5(alpha):
    return hashlib.md5(alpha.encode('utf-8')).hexdigest()