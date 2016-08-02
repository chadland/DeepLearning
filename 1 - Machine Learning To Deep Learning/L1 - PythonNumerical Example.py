# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 14:31:22 2016

@author: christerhadland
"""

num = 1000000

for x in range (0, 1000000):
    num= num + 0.000001

num = num - 1000000
print num