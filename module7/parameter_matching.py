#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
    sys.exit()

param = sys.argv[1]

input = input("What was the parameter?")

if param == input:
        print("Good job!")
else:
        print("Aww , try harder next time.")