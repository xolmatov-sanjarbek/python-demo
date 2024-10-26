# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:07:05 2024

@author: user
"""

def katta_son(son1, son2):
    """Foydalanuvchidan ikkita son olib,
    ulardan kattasini ko'rsatuvchi funksiya.
    Agar sonlar teng bo'lsa 'Sonlar teng' 
    degan xabar chiqadi"""
    son1 = float(son1)
    son2 = float(son2)
    if son1 > son2:
        print(f"{son1} > {son2}")
    elif son1 < son2:
        print(f"{son1} < {son2}")
    else:
        print("Sonlar teng.")

son1 = input("Istalgan son kiriting : ")
son2 = input("Istalgan son kiritng : ")
katta_son(son1, son2)

