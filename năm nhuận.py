# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 11:39:53 2024

@author: Ngoc Anh
"""

nam = int(input('Nhap nam nam: '))

# Kiem tra nam nhuan
if (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0)):
    print('Nam nhuan')
else:
    print('Nam khong nhuan')