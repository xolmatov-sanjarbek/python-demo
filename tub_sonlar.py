# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 16:00:16 2024

@author: user
"""

def tub_son_top(min, max):
    """Berilgan oraliqdagi tub sonlarni chiqaruvchi funksiya"""
    tub_sonlar = []
    for n in range(min, max+1):
        tub = True
        if n==1:
            tub = False
        elif n==2:
            tub = True
        else:
            for x in range(2, n):
                if n%x == 0:
                    tub = False
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar

    
            
min = int(input("Boshlang'ich son kiriting : "))
max = int(input("Oxirgi sonni kiriting : "))
print(tub_son_top(min, max))
            
            
            

            

        