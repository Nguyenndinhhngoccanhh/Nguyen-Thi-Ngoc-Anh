# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:51:43 2024

@author: Ngoc Anh
"""

km = float(input("Nhập số km: "))
if km <= 1:
    fare = 20
elif km <= 3:
    fare = 20 + (km - 1) * 13
elif km <= 8:
    fare = 20 + 2 * 13 + (km - 3) * 12
else:
    fare = 20 + 2 * 13 + 5 * 12 + (km - 8) * 10

if fare > 100:
    fare *= 0.92  # Giảm 8%

print(f"Tổng tiền: {fare}k")