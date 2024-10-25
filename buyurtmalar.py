# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:41:36 2024

@author: user
"""

buyurtmalar = []
while True:
    buyurtma = input("Nima buyurtma qilmoqchisiz? (dasturni to'xtatish uchun 'stop' deb yozing)")
    if buyurtma == 'stop':
        break
    else:
        buyurtmalar.append(buyurtma)
    