import math as m
import scipy.integrate as s

def f(x):
  return 1 / (1 + x ** 2)

def h_func(upper_limit, lower_limit, n):
  return (upper_limit - lower_limit) / n

def value(h, lower_limit):
  val = [lower_limit]
  for i in range(1, n + 1):
    val = val + [lower_limit + (h * i)]
  return val

def formula(h, y0, yn, odd_sum, even_sum):
  return (h / 3) * (y0 + yn + 4 * (odd_sum) + 2 * (even_sum)) 

def simpson_1_3_rule(upper_limit, lower_limit, n):
  actual_value, err = s.quad(f, lower_limit, upper_limit)

  h = h_func(upper_limit, lower_limit, n)
  x = value(h, lower_limit)

  y = []
  for i in range(len(x)):
    y = y + [f(x[i])]

  odd_sum = 0
  even_sum = 0
  for i in range(1, n):
    if (i % 2 == 0):
      even_sum = even_sum + y[i]
    else:
      odd_sum = odd_sum + y[i]

  approx_value = formula(h, y[0], y[n], odd_sum, even_sum)

  print(f'x: {x}')
  print(f'y: {y}\n')
  print(f'Actual value of f(x): {actual_value}')
  print(f'Approx value of f(x): {approx_value}')
  print(f'True error: {abs(actual_value - approx_value)}')
  print(f'Relative error: {abs(actual_value - approx_value) / abs(actual_value)}')
  

upper_limit = 1
lower_limit = 0
n = 8
simpson_1_3_rule(upper_limit, lower_limit, n)


import math as m
import scipy.integrate as s

def f(t):
  return (2000 * m.log(140000 / (140000 - 2100 * t)) - 9.8 * t)

def h_func(upper_limit, lower_limit, n):
  return (upper_limit - lower_limit) / n

def value(h, lower_limit):
  val = [lower_limit]
  for i in range(1, n + 1):
    val = val + [lower_limit + (h * i)]
  return val

def formula(h, y0, yn, odd_sum, even_sum):
  return (h / 3) * (y0 + yn + 4 * (odd_sum) + 2 * (even_sum)) 

def simpson_1_3_rule(upper_limit, lower_limit, n):
  actual_value, err = s.quad(f, lower_limit, upper_limit)

  h = h_func(upper_limit, lower_limit, n)
  x = value(h, lower_limit)

  y = []
  for i in range(len(x)):
    y = y + [f(x[i])]

  odd_sum = 0
  even_sum = 0
  for i in range(1, n):
    if (i % 2 == 0):
      even_sum = even_sum + y[i]
    else:
      odd_sum = odd_sum + y[i]

  approx_value = formula(h, y[0], y[n], odd_sum, even_sum)

  print(f'x: {x}')
  print(f'y: {y}\n')
  print(f'Actual value of f(x): {actual_value}')
  print(f'Approx value of f(x): {approx_value}')
  print(f'True error: {abs(actual_value - approx_value)}')
  print(f'Relative error: {abs(actual_value - approx_value) / abs(actual_value)}')
  

upper_limit = 30
lower_limit = 8
n = 1
simpson_1_3_rule(upper_limit, lower_limit, n)

import math as m
import scipy.integrate as s

def f(t):
  return (2000 * m.log(140000 / (140000 - 2100 * t)) - 9.8 * t)

def h_func(upper_limit, lower_limit, n):
  return (upper_limit - lower_limit) / n

def value(h, lower_limit):
  val = [lower_limit]
  for i in range(1, n + 1):
    val = val + [lower_limit + (h * i)]
  return val

def formula(h, y0, yn, odd_sum, even_sum):
  return (h / 3) * (y0 + yn + 4 * (odd_sum) + 2 * (even_sum)) 

def simpson_1_3_rule(upper_limit, lower_limit, n):
  actual_value, err = s.quad(f, lower_limit, upper_limit)

  h = h_func(upper_limit, lower_limit, n)
  x = value(h, lower_limit)

  y = []
  for i in range(len(x)):
    y = y + [f(x[i])]

  odd_sum = 0
  even_sum = 0
  for i in range(1, n):
    if (i % 2 == 0):
      even_sum = even_sum + y[i]
    else:
      odd_sum = odd_sum + y[i]

  approx_value = formula(h, y[0], y[n], odd_sum, even_sum)

  print(f'x: {x}')
  print(f'y: {y}\n')
  print(f'Actual value of f(x): {actual_value}')
  print(f'Approx value of f(x): {approx_value}')
  print(f'True error: {abs(actual_value - approx_value)}')
  print(f'Relative error: {abs(actual_value - approx_value) / abs(actual_value)}')
  

upper_limit = 30
lower_limit = 8
n = 10
simpson_1_3_rule(upper_limit, lower_limit, n)