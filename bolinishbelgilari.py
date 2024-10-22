# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:41:28 2024

@author: user
"""


son = int(input("Istalgan sonni kiriting: "))

for n in range(2,11):
    if (son%n==0):
        print(f"{son} {n}ga qoldiqsiz bo'linadi.")
    