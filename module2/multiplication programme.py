#!/usr/bin/env python3

first_number = int(input("Enter the first number :"))
second_number = int(input("Enter the second number :"))


result = first_number * second_number
print(f"{first_number} x {second_number} = {result}")

if result == 0:
        print("The number is both positive and negative")
elif result >= 0:
        print("The number is positive")
elif result <= 0:
        print("The number is negative")