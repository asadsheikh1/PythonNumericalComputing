import math as m
import sympy as s

def f(x):
    return s.cos(x) - 1.3 * x

def f_derivative(x):
    x_symbol = s.Symbol('x')
    eq = f(x_symbol)
    return s.diff(eq, x_symbol).evalf(subs={x_symbol:x})

def newton_raphson(x, e):
    result = [None] * 5
    
    for i in range(5):
        result[i] = (x - (f(x) / f_derivative(x)))
        x = result[i]
        
        if (result[i - 1] != None):
            tolerance = abs(result[i] - result[i - 1])
            
            if (tolerance <= e):
                print(f'tolerance: {tolerance} <= e: {e}')
                break
            
            print(f'{i + 1} {result[i]}, Tolerance: {tolerance}')
            
        else:
            print(f'{i + 1} {result[0]}')
            
        print()

newton_raphson(0, 0.000001)

import math as m
import sympy as s

def f(x):
    return x * s.cos(x) - 2 * (x ** 2) + 3 * x - 1

def f_derivative(x):
    x_symbol = s.Symbol('x')
    eq = f(x_symbol)
    return s.diff(eq, x_symbol).evalf(subs={x_symbol:x})

def newton_raphson(x, e):
    result = [None] * 5
    
    for i in range(5):
        result[i] = (x - (f(x) / f_derivative(x)))
        x = result[i]
        
        if (result[i - 1] != None):
            tolerance = abs(result[i] - result[i - 1])
            
            if (tolerance <= e):
                print(f'tolerance: {tolerance} <= e: {e}')
                break
            
            print(f'{i + 1} {result[i]}, Tolerance: {tolerance}')
            
        else:
            print(f'{i + 1} {result[0]}')
            
        print()

newton_raphson(0, 0.000001)

import math as m
import sympy as s

def f(x):
    return 2 * x * s.cos(2 * x) - (x + 1) ** 2

def f_derivative(x):
    x_symbol = s.Symbol('x')
    eq = f(x_symbol)
    return s.diff(eq, x_symbol).evalf(subs={x_symbol:x})

def newton_raphson(x, e):
    result = [None] * 5
    
    for i in range(5):
        result[i] = (x - (f(x) / f_derivative(x)))
        x = result[i]
        
        if (result[i - 1] != None):
            tolerance = abs(result[i] - result[i - 1])
            
            if (tolerance <= e):
                print(f'tolerance: {tolerance} <= e: {e}')
                break
            
            print(f'{i + 1} {result[i]}, Tolerance: {tolerance}')
            
        else:
            print(f'{i + 1} {result[0]}')
            
        print()

newton_raphson(0.25, 0.000000001)

import math as m
import sympy as s

def f(x):
    return (x ** 3) - 0.165 * x ** 2 + 0.0003993

def f_derivative(x):
    x_symbol = s.Symbol('x')
    eq = f(x_symbol)
    return s.diff(eq, x_symbol).evalf(subs={x_symbol:x})

def newton_raphson(x, e):
    result = [None] * 5
    
    for i in range(5):
        result[i] = (x - (f(x) / f_derivative(x)))
        x = result[i]
        
        if (result[i - 1] != None):
            tolerance = abs(result[i] - result[i - 1])
            
            if (tolerance <= e):
                print(f'tolerance: {tolerance} <= e: {e}')
                break
            
            print(f'{i + 1} {result[i]}, Tolerance: {tolerance}')
            
        else:
            print(f'{i + 1} {result[0]}')
            
        print()

newton_raphson(0.25, 0.0001)