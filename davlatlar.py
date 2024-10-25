# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 21:29:19 2024

@author: user
"""
davlatlar = {
    'rossiya':{
        'poytaxt':'moskva',
        'pul':'rubl',
        'til':'rus'
        },
    'germaniya':{
        'poytaxt':'berlin',
        'pul':'yevro',
        'til':'nemis'
        },
    'fransiya':{
        'poytaxt':'parij',
        'pul':'yevro',
        'til':'fransuz'
        },
    'aqsh':{
        'poytaxt':'vashington',
        'pul':'dollar',
        "til":'ingliz'
        },
    'meksika':{
        'poytaxt':'meksika',
        'pul':'peso',
        'til':'ispan'
        },
    'o\'zbekiston':{
        'poytaxt':'toshkent',
        'pul':'so\'m',
        'til':'o\'zbek'
        },
    'tojikiston':{
        'poytaxt':'dushanbe',
        'pul':'tojikiston somoni',
        'til':'tojik'
        },
    'qozog\'iston':{
        'poytaxt':'astana',
        'pul':'tenge',
        'til':'qozoq'
        }
    }

davlat = input("Davlat nomini kiriting: ").lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"{davlat.title()}ning poytaxti {info['poytaxt'].title()}. " 
          f"Pul birligi - {info['pul']}. " 
          f"Tili - {info['til']}.")
else:
    print('Bizda bunday ma\'lumot yo\'q')
    









