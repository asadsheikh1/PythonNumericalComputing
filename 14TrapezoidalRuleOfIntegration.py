import math as m
import scipy.integrate as s

def f(x):
  return 1 / (1 + x ** 2)

def h_func(upper_limit, lower_limit, n):
  return (upper_limit - lower_limit) / n

def value(h):
  val = [0]
  for i in range(1, n + 1):
    val = val + [h * i]
  return val

def formula(h, y0, yn, sum_of_y):
  return (h / 2) * (y0 + yn + 2 * (sum_of_y)) 

def trapezoid_rule(upper_limit, lower_limit, n):
  actual_value, err = s.quad(f, lower_limit, upper_limit)

  h = h_func(upper_limit, lower_limit, n)
  x = value(h)

  y = []
  for i in range(len(x)):
    y = y + [f(x[i])]

  sum_of_y = 0
  for i in range(1, n):
    sum_of_y = sum_of_y + y[i]

  approx_value = formula(h, y[0], y[n], sum_of_y)

  print(f'x: {x}')
  print(f'y: {y}\n')
  print(f'Actual value of f(x): {actual_value}')
  print(f'Approx value of f(x): {approx_value}')
  print(f'True error: {abs(actual_value - approx_value)}')
  print(f'Relative error: {abs(actual_value - approx_value) / abs(actual_value)}')


upper_limit = 1
lower_limit = 0
n = 5
trapezoid_rule(upper_limit, lower_limit, n)

import math as m
import scipy.integrate as s

def f(t):
  return (2000 * m.log(140000 / (140000 - 2100 * t)) - 9.8 * t)

def h_func(upper_limit, lower_limit, n):
  return (upper_limit - lower_limit) / n

def value(h):
  val = [0]
  for i in range(1, n + 1):
    val = val + [h * i]
  return val

def formula(h, y0, yn, sum_of_y):
  return (h / 2) * (y0 + yn + 2 * (sum_of_y)) 

def trapezoid_rule(upper_limit, lower_limit, n):
  actual_value, err = s.quad(f, lower_limit, upper_limit)

  h = h_func(upper_limit, lower_limit, n)
  x = value(h)

  y = []
  for i in range(len(x)):
    y = y + [f(x[i])]

  sum_of_y = 0
  for i in range(1, n):
    sum_of_y = sum_of_y + y[i]

  approx_value = formula(h, y[0], y[n], sum_of_y)

  print(f'x: {x}')
  print(f'y: {y}\n')
  print(f'Actual value of f(x): {actual_value}')
  print(f'Approx value of f(x): {approx_value}')
  print(f'True error: {abs(actual_value - approx_value)}')
  print(f'Relative error: {abs(actual_value - approx_value) / abs(actual_value)}')
  

upper_limit = 30
lower_limit = 8
n = 1
trapezoid_rule(upper_limit, lower_limit, n)

import math as m
import scipy.integrate as s

def f(t):
  return (2000 * m.log(140000 / (140000 - 2100 * t)) - 9.8 * t)

def h_func(upper_limit, lower_limit, n):
  return (upper_limit - lower_limit) / n

def value(h):
  val = [0]
  for i in range(1, n + 1):
    val = val + [h * i]
  return val

def formula(h, y0, yn, sum_of_y):
  return (h / 2) * (y0 + yn + 2 * (sum_of_y)) 

def trapezoid_rule(upper_limit, lower_limit, n):
  actual_value, err = s.quad(f, lower_limit, upper_limit)

  h = h_func(upper_limit, lower_limit, n)
  x = value(h)

  y = []
  for i in range(len(x)):
    y = y + [f(x[i])]

  sum_of_y = 0
  for i in range(1, n):
    sum_of_y = sum_of_y + y[i]

  approx_value = formula(h, y[0], y[n], sum_of_y)

  print(f'x: {x}')
  print(f'y: {y}\n')
  print(f'Actual value of f(x): {actual_value}')
  print(f'Approx value of f(x): {approx_value}')
  print(f'True error: {abs(actual_value - approx_value)}')
  print(f'Relative error: {abs(actual_value - approx_value) / abs(actual_value)}')
  

upper_limit = 30
lower_limit = 8
n = 2
trapezoid_rule(upper_limit, lower_limit, n)

import math as m
import scipy.integrate as s

def f(x):
  return (300 * x) / (1 + m.exp(x))

def h_func(upper_limit, lower_limit, n):
  return (upper_limit - lower_limit) / n

def value(h):
  val = [0]
  for i in range(1, n + 1):
    val = val + [h * i]
  return val

def formula(h, y0, yn, sum_of_y):
  return (h / 2) * (y0 + yn + 2 * (sum_of_y)) 

def trapezoid_rule(upper_limit, lower_limit, n):
  actual_value, err = s.quad(f, lower_limit, upper_limit)

  h = h_func(upper_limit, lower_limit, n)
  x = value(h)

  y = []
  for i in range(len(x)):
    y = y + [f(x[i])]

  sum_of_y = 0
  for i in range(1, n):
    sum_of_y = sum_of_y + y[i]

  approx_value = formula(h, y[0], y[n], sum_of_y)

  print(f'x: {x}')
  print(f'y: {y}\n')
  print(f'Actual value of f(x): {actual_value}')
  print(f'Approx value of f(x): {approx_value}')
  print(f'True error: {abs(actual_value - approx_value)}')
  print(f'Relative error: {abs(actual_value - approx_value) / abs(actual_value)}')
  

upper_limit = 10
lower_limit = 0
n = 32
trapezoid_rule(upper_limit, lower_limit, n)