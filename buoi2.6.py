# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:19:13 2024

@author: Ngoc Anh
"""

import calendar

year = int(input("Nhập năm: "))
is_leap = calendar.isleap(year)
print(f"{year} là năm nhuận" if is_leap else f"{year} không phải là năm nhuận")