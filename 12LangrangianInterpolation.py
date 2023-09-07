def langrangian_interpolation(x, x0, x1, x2, x3, fx0, fx1, fx2, fx3):
  f0 = fx0 * ((x - x1) * (x - x2) * (x - x3)) / ((x0 - x1) * (x0 - x2) * (x0 - x3))
  f1 = fx1 * ((x - x0) * (x - x2) * (x - x3)) / ((x1 - x0) * (x1 - x2) * (x1 - x3))
  f2 = fx2 * ((x - x0) * (x - x1) * (x - x3)) / ((x2 - x0) * (x2 - x1) * (x2 - x3))
  f3 = fx3 * ((x - x0) * (x - x1) * (x - x2)) / ((x3 - x0) * (x3 - x1) * (x3 - x2))

  return f0 + f1 + f2 + f3

x0, x1, x2, x3 = 5, 6, 9, 11
fx0, fx1, fx2, fx3 = 12, 13, 14, 16
x = 10

print(f'Langrangian Interpolation: {langrangian_interpolation(x, x0, x1, x2, x3, fx0, fx1, fx2, fx3)}')

def langrangian_interpolation(x, x0, x1, x2, x3, x4, x5, fx0, fx1, fx2, fx3, fx4, fx5):
  f0 = fx0 * ((x - x1) * (x - x2) * (x - x3) * (x - x4) * (x - x5)) / ((x0 - x1) * (x0 - x2) * (x0 - x3) * (x0 - x4) * (x0 - x5))
  f1 = fx1 * ((x - x0) * (x - x2) * (x - x3) * (x - x4) * (x - x5)) / ((x1 - x0) * (x1 - x2) * (x1 - x3) * (x1 - x4) * (x1 - x5))
  f2 = fx2 * ((x - x0) * (x - x1) * (x - x3) * (x - x4) * (x - x5)) / ((x2 - x0) * (x2 - x1) * (x2 - x3) * (x2 - x4) * (x2 - x5))
  f3 = fx3 * ((x - x0) * (x - x1) * (x - x2) * (x - x4) * (x - x5)) / ((x3 - x0) * (x3 - x1) * (x3 - x2) * (x3 - x4) * (x3 - x5))
  f4 = fx4 * ((x - x0) * (x - x1) * (x - x2) * (x - x3) * (x - x5)) / ((x4 - x0) * (x4 - x1) * (x4 - x2) * (x4 - x3) * (x4 - x5))
  f5 = fx5 * ((x - x0) * (x - x1) * (x - x2) * (x - x3) * (x - x4)) / ((x5 - x0) * (x5 - x1) * (x5 - x2) * (x5 - x3) * (x5 - x4))

  return f0 + f1 + f2 + f3 + f4 + f5

x0, x1, x2, x3, x4, x5 = 0, 10, 15, 20, 22.5, 30
fx0, fx1, fx2, fx3, fx4, fx5 = 0, 227.04, 362.78, 517.35, 602.97, 901.67
x = 16

print(f'Velocity using Langrangian Interpolation: {langrangian_interpolation(x, x0, x1, x2, x3, x4, x5, fx0, fx1, fx2, fx3, fx4, fx5)}')