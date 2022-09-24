from random import random
from random import randint
import math


def Zadacha0():  # Находим квадрат числа
    number = int(input('Введите число от 0 до 10: '))
    print(f'Квадрат числа {number} = {number ** 2}')


def Zadacha1():  # Определяем, являются ли числа квадратами друг друга
    a = int(input('Введите число от 0 до 100: '))
    b = int(input('Введите число от 0 до 100: '))
    if a == b ** 2:
        print(f'{a} является квадратом {b}')
    elif b == a ** 2:
        print(f'{b} является квадратом {a}')
    else:
        print(f'{a} и {b} не являются квадратами друг друга')


def Zadacha2():  # Находим максимальное число из списка
    nums = []
    size = 5
    for j in range(size):
        nums.append(randint(0, 9))
    print(nums)
    maxx = nums[0]
    for i in nums:
        if i > maxx:
            maxx = i
    print(f'Максимальное значение = {maxx}')


def Zadacha3():  # 3. Напишите программу, которая будет на вход принимать число N
    # и выводить числа от -N до N
    num = abs(int(input('Введите число от 1 до 10: ')))
    print(f'Числовой ряд от -{num} до {num}', end=': ')
    for i in range(-num, num + 1):
        print(f'{i}', end=' ')
    print()
    
    #start_num = - num
    #print(f'Числовой ряд от -{num} до {num}', end=': ')
    # while start_num <= num:
    #    print(f'{start_num}', end=' ')
    #    start_num += 1
    # print()

    


def Zadacha4():  # 4. Напишите программу, которая будет принимать
    # на вход дробь и показывать первую цифру дробной части числа.
    num = float(input('Введите дробное число: '))
    print(f'Первая цифра после запятой - {int(num * 10  % 10)}')


def Zadacha5():  # 5. Напишите программу, которая принимает на вход число и
    # проверяет, кратно ли оно 5 и 10 или 15, но не 30.
    num = int(input('Введите число: '))
    if ((num % 5 == 0 and num % 10 == 0) or num % 15 == 0) and num % 30 != 0:
        print(f'Число {num} кратно 5 и 10 или 15 но не 30')
    else:
        print(f'Условие нарушено!')
        
def Zadacha6(): #Напишите программу, которая принимает на вход цифру, обозначающую 
                #день недели, и проверяет, является ли этот день выходным.
    day = int(input('Введите № дня недели: '))
    if day in range(6):
        print(f'{day}й день недели это будний день!')
    elif day in range(6,8):
        print(f'{day}й день недели это выходной день!')
    else:
        print(f'Такого дня недели не существует!')
        
            
def Zadacha7(): #    7. Напишите программу для. проверки истинности утверждения
                # ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
    for x in range(2):
        for y in range(2):
            for z in range(2):
                f = not(x or y or z)
                print(x, y, z, f, end = ' = ')
                f = not(x) and not(y) and not(z) 
                print(x, y, z, f)
    

def Zadacha8(): # Напишите программу, которая принимает на вход координаты точки (X и Y), 
                # причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится 
                # эта точка (или на какой оси она находится).
    x = int(input('Введите координату X точки (от -9 до 9): '))
    y = int(input('Введите координату Y точки (от -9 до 9): '))
    if x in range(-9, 10) and y in range(-9, 10):
        if x > 0 and y > 0 and x in range(-9, 10) and y in range(-9, 10):
            place = 1
        elif x > 0 and y < 0:
            place = 2
        elif x < 0 and y < 0:
            place = 3
        elif x < 0 and y > 0:
            place = 4    
        print(f'X={x}, Y={y}, Четверть {place}')
    else:
        print('Точки с такими координатами не существует!')
        

def Zadacha9():  # Напишите программу, которая по заданному номеру четверти, показывает диапазон 
                # возможных координат точек в этой четверти (x и y).
    place = int(input('Введите номер четверти плоскости, в которой находится точка (1 - 4): '))
    if place in range(5):
        if place == 1:
            str = 'X = 0 ~ 9, Y = 0 ~ 9'
        elif place == 2:
            str = 'X = 0 ~ 9, Y = -9 ~ 0'
        elif place == 3:
            str = 'X = -9 ~ 0, Y = -9 ~ 0' 
        elif place == 4:
            str = 'X = -9 ~ 0, Y = 0 ~ 9'   
        print(f'Точка, лежащая в {place}й четверти имеет следующий диапазон координат: {str}')
    else:
        print('Такого номера четверти не существует!')
        

def Zadacha10(): # Напишите программу, которая принимает на вход координаты двух точек и находит 
                # расстояние между ними в 2D пространстве.
    ax = int(input('Введите координату X точки A (от -9 до 9): '))
    ay = int(input('Введите координату Y точки A (от -9 до 9): '))
    bx = int(input('Введите координату X точки B (от -9 до 9): '))
    by = int(input('Введите координату Y точки B (от -9 до 9): '))
    ab = math.sqrt((bx - ax) ** 2 + ((by - ay) ** 2))
    print(f'Расстояние между точками A({ax}, {ay}) и B({bx}, {by}) = {ab}')
    
    
        

# Zadacha0()
# Zadacha1()
# Zadacha2()
# Zadacha3()
# Zadacha4()
# Zadacha5()
# Zadacha6()
# Zadacha7()
# Zadacha8()
# Zadacha9()
# Zadacha10()