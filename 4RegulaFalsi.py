def f(x):
  return m.cos(x) - 1.3 * x - 0

def root(x_positive, x_negative):
  return (x_positive + x_negative) / 2

def regula_falsi_method(x_positive, x_negative):
  xr = []
  tolerance = 0
  for i in range(10):
    xr = xr + [((x_negative * f(x_positive)) - (x_positive * f(x_negative))) / (f(x_positive) - f(x_negative))]
    print(f'{i + 1}.', end=" ")
    if (f(xr[i]) < 0):
      x_negative = xr[i]
      print(f'Change in x_negative: {x_negative}')
    else:
      x_positive = xr[i]
      print(f'Change in x_positive: {x_positive}')

    tolerance = abs(xr[i] - xr[i - 1])
    print(f'Tolerance: {tolerance}')
    print()


x_negative = 1
x_positive = 0
regula_falsi_method(x_positive, x_negative)

import math as m

def f(x):
    return x * m.cos(x) - 2 * x ** 2 + 3 * x - 1

def false_position_method(x0, x1):
    xr = [None] * 10
    for i in range(6):
        xr[i] = (((x1) * (f(x0))) - ((x0) * (f(x1)))) / ((f(x0)) - (f(x1)))
        
        if (xr[i] < 0):
            x0 = xr[i]
            print(f'Change in x0: {x0}')
            
        else:
            x1 = xr[i]
            print(f'{i + 1} Change in x1: {x1 - x0}')
            print(f'f(x): {f(xr[i])}')
            if (xr[i - 1] != None):
                tolerance = abs(xr[i] - xr[i - 1])
                print(f'Tolerance: {tolerance}') 

        print()
        
x0 = 0
x1 = 1

false_position_method(x0, x1)

import math as m

def f(x):
    return 2 * x * m.cos(2 * x) - (x + 1) ** 2

def false_position_method(x0, x1):
    xr = [None] * 10
    for i in range(5):
        xr[i] = (((x1) * (f(x0))) - ((x0) * (f(x1)))) / ((f(x0)) - (f(x1)))
        
        if (xr[i] < 0):
            x0 = xr[i]
            print(f'{i + 1} Change in x0: {x0}')
            print(f'f(x): {f(xr[i])}')
            if (xr[i - 1] != None):
                tolerance = abs(xr[i] - xr[i - 1])
                print(f'Tolerance: {tolerance}') 
            
        else:
            x1 = xr[i]
            print(f'{i + 1} Change in x1: {x1 - x0}')
            print(f'f(x): {f(xr[i])}')
            if (xr[i - 1] != None):
                tolerance = abs(xr[i] - xr[i - 1])
                print(f'Tolerance: {tolerance}') 

        print()
        
x0 = 0
x1 = -1

false_position_method(x0, x1)