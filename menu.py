# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:16:29 2024

@author: user
"""

mahsulotlar = ["anor", "olma", "nok", "uzum", "olcha", "gilos", "tarvuz", "banan"]
savat = []

for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni kiriting: "))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if bor_mahsulotlar:
    print("Quyidagi mahsulotlar mavjud emas:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha mahsulotlar bor.")

        

        
        





    