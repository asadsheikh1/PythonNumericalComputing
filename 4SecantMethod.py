import math as m

def f(x):
    return m.cos(x) - 1.3 * x - 0

def secant_method(x0, x1, e):
    xi = [None] * 10
    for i in range(1, 5):
        xi[i] = x1 - (((f(x1) * (x1 - x0)) / (f(x1) - f(x0))))
        
        x0 = x1
        x1 = xi[i]
        
        print(f'{i} xi: {xi[i]}, x0: {x0}')
        
        if (xi[i - 1] != None):
            tolerance = abs(xi[i] - xi[i - 1])
            print(f'Tolerance: {tolerance}')
            # print(f'Tolerance by formula: {abs((xi[i] - xi[i - 1]) / xi[i])}')
            
            if (tolerance >= 0.1):
                print('tolerance > 0.1')
            
            elif (tolerance >= 0.01):
                print('tolerance > 0.01')
            
            elif (tolerance >= 0.001):
                print('tolerance > 0.001')
            
            elif (tolerance >= 0.0001):
                print('tolerance > 0.0001')
            
            elif (tolerance >= 0.00001):
                print('tolerance > 0.00001')
                
            else:
                print('tolerance > 0.000001')
                
        print()

secant_method(0, 1, 0.0001)

import math as m

def f(x):
    return x * m.cos(x) - 2 * (x ** 2) + 3 * x - 1

def secant_method(x0, x1, e):
    xi = [None] * 10
    for i in range(1, 7):
        xi[i] = x1 - (((f(x1) * (x1 - x0)) / (f(x1) - f(x0))))
        
        x0 = x1
        x1 = xi[i]
        
        print(f'{i} xi: {xi[i]}, x0: {x0}')
        
        if (xi[i - 1] != None):
            tolerance = abs(xi[i] - xi[i - 1])
            print(f'Tolerance: {tolerance}')
            # print(f'Tolerance by formula: {abs((xi[i] - xi[i - 1]) / xi[i])}')
            
            if (tolerance >= 0.1):
                print('tolerance > 0.1')
            
            elif (tolerance >= 0.01):
                print('tolerance > 0.01')
            
            elif (tolerance >= 0.001):
                print('tolerance > 0.001')
            
            elif (tolerance >= 0.0001):
                print('tolerance > 0.0001')
            
            elif (tolerance >= 0.00001):
                print('tolerance > 0.00001')
                
            else:
                print('tolerance > 0.000001')
                
        print()

secant_method(1, 0, 0.0001)

import math as m

def f(x):
    return 2 * x * m.cos(2 * x) - (x + 1) ** 2

def secant_method(x0, x1, e):
    xi = [None] * 10
    for i in range(1, 8):
        xi[i] = x1 - (((f(x1) * (x1 - x0)) / (f(x1) - f(x0))))
        
        x0 = x1
        x1 = xi[i]
        
        print(f'{i} xi: {xi[i]}, x0: {x0}')
        
        if (xi[i - 1] != None):
            tolerance = abs(xi[i] - xi[i - 1])
            print(f'Tolerance: {tolerance}')
            # print(f'Tolerance by formula: {abs((xi[i] - xi[i - 1]) / xi[i])}')
                
        print()

secant_method(-1, 0, 0.0001)

import math as m

def f(x):
    return (x ** 3) - 0.165 * x ** 2 + 0.0003993

def secant_method(x0, x1, e):
    xi = [None] * 10
    for i in range(1, 5):
        xi[i] = x1 - (((f(x1) * (x1 - x0)) / (f(x1) - f(x0))))
        
        x0 = x1
        x1 = xi[i]
        
        print(f'{i} xi: {xi[i]}, x0: {x0}')
        
        if (xi[i - 1] != None):
            tolerance = abs(xi[i] - xi[i - 1])
            print(f'Tolerance: {tolerance}')
            # print(f'Tolerance by formula: {abs((xi[i] - xi[i - 1]) / xi[i])}')
            
            if (tolerance <= e):
                print(f'tolerance: {tolerance} <= e: {e}')
                break
                
        print()

secant_method(-1, 0, 0.000001)