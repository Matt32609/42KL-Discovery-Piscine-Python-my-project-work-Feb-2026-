#!/usr/bin/env python3

number = int(input("Enter a number less than 25"))

if number >= 25:
        print("None")
else:
        while number <= 25:
                print(f"Inside the variable , my number is {number}")
                number = number + 1