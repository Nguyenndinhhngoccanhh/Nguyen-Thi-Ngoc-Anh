# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 05:22:35 2024

@author: Ngoc Anh
"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a== 0 and b!=0:
    print("Phương trình vô nghiệm")
elif a== 0 and b== 0:
    print("Phương trình vô số nghiệm")
else:
    print("Nghiệm của phương trình là: ", -b/a)
    

          