# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:37:29 2024

@author: user
"""

def katta_son():
    """Foydalanuvchidan uchta son
    qabul qilib, ulardan eng kaatasini
    chiqaruvchi funksiya"""
    son1 = int(input("Birinchi sonni kiriting : "))
    son2 = int(input("Ikkinchi sonni kiriting : "))
    son3 = int(input("Uchinchi sonni kiriting : "))
    print(max(son1, son2, son3))
katta_son()