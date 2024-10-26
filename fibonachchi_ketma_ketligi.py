# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:17:26 2024

@author: user
"""

def fibonachi_ketma_ketligi():
    sonlar = []
    miqdor = int(input("Miqdor kiriting : "))
    for n in range(miqdor):
        if n == 0 or n == 1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[n-1] + sonlar[n-2])
    for x in sonlar:
        print(x, end = ' ')
        
fibonachi_ketma_ketligi()
    