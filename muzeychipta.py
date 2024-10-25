# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:00:48 2024

@author: user
"""

savol = 'Yoshingizni kiriting: '

while True:
    yosh = input(savol)
    if yosh == 'stop' or yosh == 'quit':
        break
    
    yosh = int(yosh)
    
    if yosh < 7:
        narh = 2000
    elif yosh < 18:
        narh = 3000
    elif yosh < 65:
        narh = 5000
    else:
        narh = 0
    
    if narh == 0:
        print("Sizga kirish bepul")
    else:
        print(f'Sizga kirish {narh} so\'m')
    

    
    


