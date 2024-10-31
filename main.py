"""
Написать программу, которая:
- Создаёт с помощью генератора списков, список случайных целых чисел от **-50** до **50** размером **25** элементов.
- Находит количество положительных, отрицательных и нулевых элементов в списке.
- Выводит значения и их (*положительных, отрицательных и нулевых*) количество вместе с процентом от общего количества.
- Выводит самое большое и самое маленькое значение
"""

import random #подключение модуля random

s = [random.randint(-50, 50) for i in range(25)] #генератор списка с использованием рандомных 25 элементов от -50 до 50
print(s) #вывод списка

kol_pol, kol_0, kol_otr = 0, 0, 0 #счетчик положительных, нулевых и отрицательных чисел
for i in s: #перебор элементов списка
    if(i > 0): #если элемент положительный
        kol_pol += 1 #работа счетчика для положительных чисел
    elif(i == 0): #если элемент равен 0
        kol_0 += 1 #работа счетчика для 0
    else: #если элемент отрицательный 
        kol_otr += 1 #работа счетчика для отрицательных
print("Количество положительных чисел: ", kol_pol) #вывод количества положительных
print("Количество 0: ", kol_0) #вывод количества 0
print("Количество отрицательных чисел: ", kol_otr) #вывод количества потрицательных

kol_pol_pr = float(kol_pol * 100 / 25) #подсчет пол. элементов в проценте
kol_0_pr = float(kol_0 * 100 / 25) #подсчет 0 в проценте
kol_otr_pr = float(kol_otr * 100 / 25) #подсчет отр. элементов в проценте
print("Количество положительных чисел в процентах: ", kol_pol_pr, "%") #вывод количества в проценте(пол.)
print("Количество 0 в процентах: ", kol_0_pr, "%") #вывод количества в проценте(0)
print("Количество отрицательных чисел в процентах: ", kol_otr_pr, "%") #вывод количества в проценте(отр.)

print(min(s)) #минимальное значение в списке
print(max(s)) #максимальное значение в списке