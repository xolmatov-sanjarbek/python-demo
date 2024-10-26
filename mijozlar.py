# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 11:48:35 2024

@author: user
"""

def mijoz_info(ism, yosh, manzil, tel = '', email = None):
    """Mijozlarning ma'lumotlarini lug'at ko'rinishiga keltiradi"""
    mijoz = {
        'ism':ism,
        'yosh':yosh,
        'manzil':manzil,
        'tel':tel,
        'email':email
        }
    return mijoz
print("Mijozlarning ma'lumotlarini kiritng :")
mijozlar = []
while True:
    ism = input("Ismi : ")
    yosh = input("Yoshi : ")
    manzil = input("Yashash manzili : ")
    tel = input("Telefon raqami : ")
    email = input("Email manzili : ")
    mijozlar.append(mijoz_info(ism, yosh, manzil, tel, email))
    savol = input("Davom etasizmi? (ha/yo'q) ")
    if savol == 'yo\'q':
        break

print("Mijozlar ro'yxati : ")
for mijoz in mijozlar:
    print(f"{mijoz['ism'].title()}, {mijoz['yosh']} yoshda,")
    print(f"Yashash manzili - {mijoz['manzil'].title()}")
    if tel:
        print(f"Telefon raqami : {mijoz['tel']}")
    if email:
        print(f"Email manzili : {mijoz['email']}")
        


    