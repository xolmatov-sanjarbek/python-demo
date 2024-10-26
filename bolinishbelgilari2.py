# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:13:58 2024

@author: user
"""

def bolinish_belgilar(son):
    """Foydalanuvchidan son olib,
    uni 2dan 10gacha bo'lgan sonlarga qoldiqsiz
    bo'linishini hisoblovchi funksiya"""
    for n in range(2, 11):
        if son % n == 0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi.")

son = int(input("Son kiritng : "))
bolinish_belgilar(son)
        
            
        