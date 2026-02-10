#!/usr/bin/env python3

import sys

params = sys.argv[1:]

if len(params) == 0:
        print("none")
else:
        for p in params:
                if p.find("ism") == len(p) - 3:
                    continue

                print(p + "ism")
            