# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 12:47:04 2024

@author: user
"""

def doira_info(radius, diametr, yuz, perimetr):
    """Foydalanuvchidan doiraning radiusini
    so'rab, uning radiusini, yuzini va perimetrini
    topuvchi funksiya"""
    doira = {
        'radius':radius,
        'diametr':diametr,
        'yuz':yuz,
        'perimetr':perimetr
        }
    return doira

PI = 3.14
doira_infos = []
radius = float(input("Doiraning radiusini kiriting (cmda) "))
diametr = radius*2
yuz = PI*(radius**2)
perimetr = diametr*PI
doira_infos.append(doira_info(radius, diametr, yuz, perimetr))

print(f"{radius} cmli doiraning diametri {diametr} cm, "
      f"yuzi {yuz} cm kvadrat, perimetri esa {perimetr} cmga teng")






    