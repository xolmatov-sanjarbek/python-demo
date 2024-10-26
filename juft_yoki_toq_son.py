# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 09:01:56 2024

@author: user
"""

def juft_toq(son):
    """Foydalanuvchidan son so'rab,
    uni juft yoki toq son ekanligini
    ko'rsatadi"""
    son = float(son)
    if son % 2 ==0:
        print(f"{son} juft son.")
    else:
        print(f"{son} toq son.")

son = input("Istalgan sonni kiriting : ")
juft_toq(son)
