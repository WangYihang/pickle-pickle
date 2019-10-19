#!/usr/bin/env python
# encoding:utf-8

class Exploit():
    def __init__(self, command):
        self.command = command
    
    def run(self):
        import os
        return os.system(self.command)

print(Exploit("whoami").run())