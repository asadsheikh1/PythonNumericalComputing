# Find Slope

import sympy as s
import math as m

x1 = 3
x2 = 5
y1 = 36
y2 = 100

m = (y2 - y1) / (x2 - x1)

print(f'Slope: {m}')

x_symbol = s.Symbol('x')
fx = 4 * x_symbol ** 2

result = s.diff(fx).evalf(subs={x_symbol:3})
print(f'True value of f\'(3): {result}')

# Limit

import math as m
import sympy as s

def f(x):
  return 4 * x ** 2

x_symbol = s.Symbol('x')
a = 3

fx = f(x_symbol)
fa = f(a)

func = (fx - fa) / (x_symbol - a)
limit = s.limit(func, x_symbol, a)

print(f'Approx value of f\'({x}): {limit}')