#!/usr/bin/env python3

w = str(input("What you gonna say?"))

word = "STOP"

if w != word:
        while w != word:
            print("I got that , anything else?")  
            w = str(input("What you gonna say?"))
else:
        print("ok")