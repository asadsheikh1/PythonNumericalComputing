def add_matrix(resultant_matrix, matrix_a, matrix_b):
  for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
      resultant_matrix[i][j] = matrix_a[i][j] + matrix_b[i][j]
  return resultant_matrix

def sub_matrix(resultant_matrix, matrix_a, matrix_b):
  for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
      resultant_matrix[i][j] = matrix_a[i][j] - matrix_b[i][j]
  return resultant_matrix

def mul_matrix(resultant_matrix, matrix_a, matrix_b):
  if (len(matrix_a[0]) == len(matrix_b)):
    for i in range(len(matrix_a)):
      for j in range(len(matrix_b[0])):
        total = 0
        for k in range(len(matrix_a[0])):
          total = total + (matrix_a[i][k] * matrix_b[k][j])
          resultant_matrix[i][j] = total
    return resultant_matrix

def scalar_multiplication(resultant_matrix, matrix, n):
  for i in range(len(matrix_a)):
    for j in range(len(matrix_a[0])):
      resultant_matrix[i][j] = matrix[i][j] * n
  return resultant_matrix
  

matrix_a = [[5, 2, 3],
            [1, 2, 7]]

matrix_b = [[6, 7, -2],
            [3, 5, 19]]

matrix_b_2 = [[3, -2],
              [5, -8],
              [9, -10]]

resultant_matrix_1 = [[0, 0],
                      [0, 0]]

resultant_matrix_2 = [[0, 0, 0],
                      [0, 0, 0]]
                    
print(f'Add Matrix: {add_matrix(resultant_matrix_2, matrix_a, matrix_b)}')
print(f'Sub Matrix: {sub_matrix(resultant_matrix_2, matrix_a, matrix_b)}')
print(f'Scalar Multiplication: {scalar_multiplication(resultant_matrix_2, matrix_a, 2)}')
print(f'Mul Matrix: {mul_matrix(resultant_matrix_1, matrix_a, matrix_b_2)}')

matrix_a = [[5, 2, 3],
            [1, 2, 7]]

matrix_b = [[6, 7, -2],
            [3, 5, 19]]

matrix_c = [[6, 7, -2],
            [3, 5, 19]]

resultant_matrix_1 = [[0, 0, 0],
                      [0, 0, 0]]

resultant_matrix_2 = [[0, 0, 0],
                      [0, 0, 0]]

resultant_matrix_3 = [[0, 0, 0],
                      [0, 0, 0]]

resultant_matrix_4 = [[0, 0, 0],
                      [0, 0, 0]]
            
result1 = scalar_multiplication(resultant_matrix_1, matrix_b, 2)
result2 = scalar_multiplication(resultant_matrix_2, matrix_b, 0.5)
result3 = sub_matrix(resultant_matrix_3, result1, result2)
result4 = add_matrix(resultant_matrix_4, matrix_a, result3)

print(f'Result: {result4}')