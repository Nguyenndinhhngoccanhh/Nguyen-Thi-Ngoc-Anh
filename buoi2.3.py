# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 05:37:55 2024

@author: Ngoc Anh
"""
import math

a = float(input("Nhập hệ số a"))
b = float(input("Nhập hệ số b"))
c = float(input("Nhập hệ số c"))
delta = b*b - 4*a*c
if delta< 0:
    print("Phương trình vô nghiệm")
elif delta== 0:
    x= -b/(2*a)
    print("Phương trình có nghiệm kép x1=x2", x)
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x2 = ", (-(b) + math.sqrt(delta))/(2*a) )
    
    
    
    
    
    
    
    
    
    
    
          
    
    
    
    
    
    
    
    




