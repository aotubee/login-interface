#!/usr/bin/env python
# coding=utf-8

import getpass

account_file='/python/account.txt'
lock_file='/python/lock.txt'
N=0
for i in range(3):
    name=raw_input("Please input your name:")
#    password=raw_input("Please input your password:")
    password=getpass.getpass('password:')
    N+=1
    if len(name) !=0 and len(password) !=0:
        LOGIN=False
        f=file(account_file)
        w=file(lock_file,'a')
        l=file(lock_file)
        if name in l.read():
            print "Your account was lock,contact admin."
            break
        #one by one search account and password
        for lines in f.readlines():
            line=lines.split()
            if name==line[0] and password==line[1]:
                print "Welcome to %s login." %name
                LOGIN=True
                break
        if LOGIN is True:
            break
        elif N==3:
            w.write(name)
            w.write('\n')
            w.close()
            print "Your account is lock."
        else:
            print "Please check your account or password."
    else:
        print "Account or password can't be blank."


            
    
