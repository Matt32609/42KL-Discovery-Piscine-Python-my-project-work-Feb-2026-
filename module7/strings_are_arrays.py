#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
        print("none")
        sys.exit()
    
text = sys.argv[1]
count = 0

for character in text:
        if character == "z":
            print('z' , end ='')

if count == 0:  
    print("none")