# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:09:21 2024

@author: user
"""

davlatlar = {
    "o'zbekiston":"toshkent",
    "rossiya":"moskva",
    "aqsh":"vashington",
    "yaponiya":"tokyo",
    "korea":"seul"
    }

davlat = input("Qaysi davlatning poytaxtini bilmoqchisiz? ").lower()
poytaxt = davlatlar.get(davlat)
if poytaxt == None:
    print("Kechirasiz, bizda bunday ma'lumot yo'q.")
elif davlat == 'aqsh':
    print(f"{davlat.upper()}ning poytaxti {poytaxt.title()}.")
elif davlat == "o'zbekiston":
    print("O'zbekistonning poytaxti {poytaxt.title()}.")
else:
    print(f"{davlat.title()}ning poytaxti {poytaxt.title()}.")

