# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 14:44:55 2024

@author: user
"""

son1 = float(input("Birinchi sonni kiriting : "))
son2 = float(input("Ikkinchi sonni kiritng : "))
amal = input("Qaysi amal bajarilsin? : ")
if amal == '+':
    print(f"{son1} {amal} {son2} = {son1 + son2}")
elif amal == '-':
    print(f"{son1} {amal} {son2} = {son1 - son2}")
elif amal == '*':
    print(f"{son1} {amal} {son2} = {son1 * son2}")
elif amal == '/':
    print(f"{son1} {amal} {son2} = {son1 / son2}")
else:
    print("Bunday amalni bajara olmayman.")
    