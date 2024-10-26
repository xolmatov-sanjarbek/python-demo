# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:29:54 2024

@author: user
"""

def kopaytir():
    sonlar = []
    while True:
        son = input("Son kiriting : ")
        if son == 'quit':
            break
        son = int(son)
        sonlar.append(son)
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    print(kopaytma)

kopaytir()