def f(x):
  return m.cos(x) - 1.3 * x - 0

def root(x_positive, x_negative):
  return (x_positive + x_negative) / 2

def bisection_method(x_positive, x_negative):
  xr = []
  tolerance = 0
  for i in range(10):
    xr = xr + [root(x_positive, x_negative)]
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
bisection_method(x_positive, x_negative)

import math as m

def f(x):
  return x * m.cos(x) - 2 * x ** 2 + 3 * x - 1

def root(x_positive, x_negative):
  return (x_positive + x_negative) / 2

def bisection_method(x_positive, x_negative):
  xr = []
  tolerance = 0
  for i in range(10):
    xr = xr + [root(x_positive, x_negative)]
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
bisection_method(x_positive, x_negative)

import math as m

def root_func(x1, x2):
    return (x1 + x2) / 2

def f(x):
    return 2 * x * m.cos(2 * x) - (x + 1) ** 2

def bisection_method(x_negative, x_positive):
    for i in range(12):
        root = root_func(x_negative, x_positive)
        print(f'{i + 1}.', end=" ")
        if (f(root) < 0):
            x_negative = root
            print(f'Change in x_negative: {x_negative}')
        else:
            x_positive = root
            print(f'Change in x_positive: {x_positive}')
        
x_negative = 0
x_positive = -1
bisection_method(x_negative, x_positive)

import math as m

def root_func(x1, x2):
    return (x1 + x2) / 2

def f(x):
    return x ** 3 - 0.165 * x ** 2 + 0.0003993

def bisection_method(x_negative, x_positive):
    for i in range(3):
        print(f'xl: {x_negative}, xu: {x_positive}')
        root = root_func(x_negative, x_positive)
        fx = f(root)
        if (f(root) < 0):
            x_negative = root
            print(f'Change in x_negative: {x_negative}', end=" ")
        else:
            x_positive = root
            print(f'Change in x_positive: {x_positive}', end=" ")
        print(f'f(x): {fx}\n')
      
x_negative = -1
x_positive = 0
bisection_method(x_negative, x_positive)
