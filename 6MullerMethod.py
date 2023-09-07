import math as m

def f(x):
  return (x ** 3) - 3 * x + 1

def muller_method(x0, x1, x2, e):
  result = [None] * 10
  for i in range(8):
    d1 = f(x0) - f(x2)
    d2 = f(x1) - f(x2)
    h1 = x0 - x2
    h2 = x1 - x2

    a = ((h1 * d2) - (h2 * d1)) / ((h1 * h2) * (x1 - x0))
    b = ((h1 ** 2) * d2 - ((h2 ** 2) * d1)) / ((x0 - x1) * h2 * h1)
    c = f(x1)

    if (b > 0):
      result[i] = x1 - (2 * c) / (b + m.sqrt((b ** 2) - 4 * a * c))
    else:
      result[i] = x1 - (2 * c) / (b - m.sqrt((b ** 2) - 4 * a * c))

    if (x1 > result[i]):
      x2 = x1
      x1 = result[i]
    else:
      x0 = x1
      x1 = result[i]

    if (result[i - 1] != None):
            tolerance = abs(result[i] - result[i - 1])
            
            if (tolerance <= e):
                print(f'tolerance: {tolerance} <= e: {e}')
                break
            
            print(f'{i + 1} {result[i]}, Tolerance: {tolerance}')
            
    else:
        print(f'{i + 1} {result[0]}')
        
    print()

x0 = 0
x1 = 0.5
x2 = 1
e = 0.0001

muller_method(x0, x1, x2, e)

import math as m

def f(x):
  return m.cos(x) - 1.3 * x - 0

def muller_method(x0, x1, x2, e):
  result = [None] * 10
  for i in range(8):
    d1 = f(x0) - f(x2)
    d2 = f(x1) - f(x2)
    h1 = x0 - x2
    h2 = x1 - x2

    a = ((h1 * d2) - (h2 * d1)) / ((h1 * h2) * (x1 - x0))
    b = ((h1 ** 2) * d2 - ((h2 ** 2) * d1)) / ((x0 - x1) * h2 * h1)
    c = f(x1)

    if (b > 0):
      result[i] = x1 - (2 * c) / (b + m.sqrt((b ** 2) - 4 * a * c))
    else:
      result[i] = x1 - (2 * c) / (b - m.sqrt((b ** 2) - 4 * a * c))

    if (x1 > result[i]):
      x2 = x1
      x1 = result[i]
      
    else:
      x0 = x1
      x1 = result[i]

    if (result[i - 1] != None):
            tolerance = abs(result[i] - result[i - 1])
            
            if (tolerance <= e):
                print(f'tolerance: {tolerance} <= e: {e}')
                break
            
            print(f'{i + 1} {result[i]}, Tolerance: {tolerance}')
            
    else:
        print(f'{i + 1} {result[0]}')
        
    print()

x0 = 0
x1 = 0.5
x2 = 1
e = 0.0001

muller_method(x0, x1, x2, e)

import math as m

def f(x):
  return x * m.cos(x) - 2 * (x ** 2) + 3 * x - 1

def muller_method(x0, x1, x2, e):
  result = [None] * 10
  for i in range(8):
    d1 = f(x0) - f(x2)
    d2 = f(x1) - f(x2)
    h1 = x0 - x2
    h2 = x1 - x2

    a = ((h1 * d2) - (h2 * d1)) / ((h1 * h2) * (x1 - x0))
    b = ((h1 ** 2) * d2 - ((h2 ** 2) * d1)) / ((x0 - x1) * h2 * h1)
    c = f(x1)

    if (b > 0):
      result[i] = x1 - (2 * c) / (b + m.sqrt((b ** 2) - 4 * a * c))
    else:
      result[i] = x1 - (2 * c) / (b - m.sqrt((b ** 2) - 4 * a * c))

    if (x1 > result[i]):
      x2 = x1
      x1 = result[i]
    else:
      x0 = x1
      x1 = result[i]

    if (result[i - 1] != None):
            tolerance = abs(result[i] - result[i - 1])
            
            if (tolerance <= e):
                print(f'tolerance: {tolerance} <= e: {e}')
                break
            
            print(f'{i + 1} {result[i]}, Tolerance: {tolerance}')
            
    else:
        print(f'{i + 1} {result[0]}')
        
    print()

x0 = 0
x1 = 0.5
x2 = 1
e = 0.0001

muller_method(x0, x1, x2, e)

import math as m

def f(x):
  return 2 * x * m.cos(2 * x) - (x + 1) ** 2

def muller_method(x0, x1, x2, e):
  result = [None] * 10
  for i in range(8):
    d1 = f(x0) - f(x2)
    d2 = f(x1) - f(x2)
    h1 = x0 - x2
    h2 = x1 - x2

    a = ((h1 * d2) - (h2 * d1)) / ((h1 * h2) * (x1 - x0))
    b = ((h1 ** 2) * d2 - ((h2 ** 2) * d1)) / ((x0 - x1) * h2 * h1)
    c = f(x1)

    if (b > 0):
      result[i] = x1 - (2 * c) / (b + m.sqrt((b ** 2) - 4 * a * c))
    else:
      result[i] = x1 - (2 * c) / (b - m.sqrt((b ** 2) - 4 * a * c))

    if (x1 > result[i]):
      x2 = x1
      x1 = result[i]
    else:
      x0 = x1
      x1 = result[i]

    if (result[i - 1] != None):
            tolerance = abs(result[i] - result[i - 1])
            
            if (tolerance <= e):
                print(f'tolerance: {tolerance} <= e: {e}')
                break
            
            print(f'{i + 1} {result[i]}, Tolerance: {tolerance}')
            
    else:
        print(f'{i + 1} {result[0]}')
        
    print()

x0 = -1
x1 = -1.5
x2 = -2
e = 0.01

muller_method(x0, x1, x2, e)