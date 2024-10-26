# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 08:49:59 2024

@author: user
"""

def kvadrat_kub_hisobla(son):
    """Foydalanuvchidan son so'rab,
    uning kvadrati va kubini chiqaruvchi funksiya"""
    print(f"{son}ning kvadrati {son**2}, kubi esa {son**3}ga teng.")

son = input("Son kiriting : ")
son = int(son)
kvadrat_kub_hisobla(son)

