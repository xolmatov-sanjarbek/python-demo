# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:35:26 2024

@author: user
"""

loginlar = ["Anvar", "Sarvar", "Olim", "Ali", "Vali"]

login = input("Login yarating: ")
if login in loginlar:
    print("Bu login band. Boshqasini yarating.")
else:
    print("Xush kelibsiz,", login+".")
    