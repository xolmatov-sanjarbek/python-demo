# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:47:21 2024

@author: user
"""

e_bozor = {}
while True:
    savol = input("Mahsulot nomini kiriting: ")
    if savol == 'exit':
        break
    narx = input(f"{savol.title()}ning narxini kiriting: ")
    e_bozor[savol] = int(narx)
print("Mahsulotlar ro'yxati:")
for savol, narx in e_bozor.items():
    print(f"{savol.title()}ning narxi {narx} so'm")    