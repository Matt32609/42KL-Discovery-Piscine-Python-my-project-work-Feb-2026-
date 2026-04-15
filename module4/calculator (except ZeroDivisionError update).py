#!/usr/bin/env python3

a = int(input("Enter the first number :"))
b = int(input("Enter the second number :"))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")

try:
        result = a/b
        if result.is_integer():
                print(f"{a} / {b} = {int(result)}")
        else:
                print(f"{a} / {b} = {result:.3f}")
except ZeroDivisionError:
        print(f"{a} / 0 = 0")