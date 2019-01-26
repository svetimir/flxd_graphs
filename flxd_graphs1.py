# -*- coding: utf-8 -*-

# рисуем графики заданных пользователем функций
# AUTHOR: fluxoid, ifi@yandex.ru
# STARTED: 22.01.2019
# VERSION: 0.1
# LATEST FILE REVISION: 22.01.2019

import numpy as np
import math
import matplotlib.pyplot as plt
import sympy
from sympy.abc import x
from sympy import sympify
from sympy.utilities.lambdify import lambdastr

# затравочная функция :)
def f(x):
    return math.sin(x)

# показ сообщения
def show_help():
    print('To quit app type \'q\' or \'exit\' and press Enter')

# разбор математического выражения
def parse_math(expr):
    if expr!='':
        # вот здесь самая главная часть программы
        res=lambdastr(x,expr)
        res=eval(res)
        # ----------
        return res
    else:
        return False

# постройка графика
def plot_graph(func,a,b,st):
    xrange=np.arange(a,b,(b-a)/st)
    yrange=[func(i) for i in xrange]
    plt.plot(yrange)
    plt.show()    

# debug
def debug(v):
    for i in v:
        print(i)

def main():
    text=''
    expr=''
    show_help()

    while 1:
        text=input('input_function(x)>')
        if text=='q' or text=='exit':
            break
        elif text=='help':
            show_help()
            continue
        expr=parse_math(text)
        if expr:
            x0=float(input('x0>'))
            x1=float(input('x1>'))
            steps=float(input('steps>'))
            v=[expr,x0,x1,steps]
            debug(v)
            plot_graph(expr,x0,x1,steps)
        else:
            continue

if __name__=='__main__':
    main()
