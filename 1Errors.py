import sympy as s
import math as m

def f(x):
  e = m.exp(0.5)
  return 7 * e ** x

x = 2
h = 0.3

x_symbol = s.Symbol('x')

true_value = s.diff(f(x_symbol)).evalf(subs= {x_symbol : 2})
approx_value = (f(x + h) - f(x)) / h
true_error = abs(true_value - approx_value)

print(f'True value of f\'(2): {true_value}')
print(f'Approx value of f\'(2): {approx_value}')
print(f'True error: {true_error}')