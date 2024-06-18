# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 21:49:17 2024

@author: alexa
"""

def check_age(age):
    \"\"\"
    Determina si una persona es menor o adulta según su edad.
    Args:
        age (int): La edad de la persona.

    Returns:
        str: \"Menor\" si la edad es menor a 18, \"Adulto\" en caso contrario.
    \"\"\"
    if age >= 18:
        return \"Adulto\"  # Si la edad es mayor o igual a 18, se considera adulto.
    else:
        return \"Menor\"  # Si la edad es menor a 18, se considera menor de edad.
