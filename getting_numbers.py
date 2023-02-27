# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 22:27:22 2023

@author: Rami
"""
def get_numbers(x):
    normal = "0123456789"
    sub_s = "₀₁₂₃₄₅₆₇₈₉"
    res = x.maketrans(''.join(sub_s), ''.join(normal))
    string = x.translate(res)
    string =string.replace("x"," ")
    string =string.replace("- ","-")
    s = []
    for t in string.split():

            try:
                s.append(float(t))
                
            except ValueError:
                pass
            
    extracted = s
    return extracted


string = "eq₂: 3x₃ -8x₁ - 1x₂ = -1 "
string=get_numbers(string)

