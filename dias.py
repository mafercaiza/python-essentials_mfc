# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 13:32:36 2021

@author: usuario
"""

def es_bisiesto(anio: int) -> bool:
    return anio % 4 == 0 and ( not not anio % 100 != 0 or anio % 400 == 0)



def obtener_dias_del_mes(mes: int, anio: int) -> int:
    # Abril, junio, septiembre y noviembre tienen 30
    if mes in [4, 6, 9, 11]:
        return 30
    # Febrero depende de si es o no bisiesto
    if mes == 2:
        if es_bisiesto(anio):
            return 29
        else:
            return 28
    else:
        # En caso contrario, tiene 31 días
        return 31

"""mes = 11
anio = 1987
dias = obtener_dias_del_mes(mes, anio)
print(dias)"""

testYears = [1900, 2000, 2016, 1987]

testMonths = [2, 2, 1, 11]

testResults = [28, 29, 31, 30]

for i in range(len(testYears)):

                yr = testYears[i]

                mo = testMonths[i]

                print(yr, mo, "->", end="")

                result = obtener_dias_del_mes(mo, yr)

                if result == testResults[i]:

                                print("OK")

                else:

                                print("Failed")