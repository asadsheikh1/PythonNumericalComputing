def fx(y, z):
  return (95 - 11 * y + 4 * z) / 83

def fy(x, z):
  return (104 - 7 * x - 13 * z) / 52

def fz(x, y):
  return (71 - 3 * x - 8 * y) / 29
  
def jacobi_method(x, y, z, e):
  for i in range(7):
    val_x = fx(y, z)
    val_y = fy(x, z)
    val_z = fz(x, y)

    tolerance_x = abs(x - val_x)

    x = val_x
    y = val_y
    z = val_z

    print(f'{i + 1} Tuple: {tuple((val_x, val_y, val_z))}')
    print(f'Tolerance: {tolerance_x}\n')

x = 0
y = 0
z = 0
e = 0.0001
jacobi_method(x, y, z, e)

def fx(y, z):
  return (3 * y - 2 * z + 45) / 8

def fy(x, z):
  return (-4 * x + z + 71) / 11

def fz(x, y):
  return (-6 * x - 3 * y + 35) / 12
  
def jacobi_method(x, y, z, e):
  for i in range(9):
    val_x = fx(y, z)
    val_y = fy(x, z)
    val_z = fz(x, y)

    tolerance_x = abs(x - val_x)

    x = val_x
    y = val_y
    z = val_z

    print(f'{i + 1} Tuple: {tuple((val_x, val_y, val_z))}')
    print(f'Tolerance: {tolerance_x}\n')

x = 0
y = 0
z = 0
e = 0.01
jacobi_method(x, y, z, e)