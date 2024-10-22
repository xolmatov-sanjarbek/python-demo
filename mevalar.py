# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:16:49 2024

@author: user
"""

mevalar = {
    "apple":"olma",
    "pear":"nok",
    "banana":"banan",
    "cherry":"olcha",
    "pineapple":"ananas",
    "apricot":"o'rik"
    }

meva = input("So'z kiriting: ").lower()
print(mevalar.get(meva, "Bunday so'z mavjud emas."))



