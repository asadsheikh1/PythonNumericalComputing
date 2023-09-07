def formula(x, y, x_val, delta_1_fx, delta_2_fx, delta_3_fx):
    i = 0
    return y[i] + (x_val - x[i]) * delta_1_fx[i] + (x_val - x[i]) * (x_val - x[i + 1]) * delta_2_fx[i] + (x_val - x[i]) * (x_val - x[i + 1]) * (x_val - x[i + 2]) * delta_3_fx[i]


x = [5, 6, 9, 11]
y = [12, 13, 14, 16]
x_val = 10

delta_1_fx = []
delta_2_fx = []
delta_3_fx = []

for i in range(1, len(x)):
    delta_1_fx = delta_1_fx + [(y[i] - y[i - 1]) / (x[i] - x[i - 1])]

for i in range(1, len(delta_1_fx)):
    delta_2_fx = delta_2_fx + [(delta_1_fx[i] - delta_1_fx[i - 1]) / (x[i + 1] - x[i - 1])]

for i in range(1, len(delta_2_fx)):
    delta_3_fx = delta_3_fx + [(delta_2_fx[i] - delta_2_fx[i - 1]) / (x[i + 2] - x[i - 1])]

print(f'Δ1fx: {delta_1_fx}')
print(f'Δ2fx: {delta_2_fx}')
print(f'Δ3fx: {delta_3_fx}')

print(f'\nAnswer: {formula(x, y, x_val, delta_1_fx, delta_2_fx, delta_3_fx)}')

def formula(x, y, x_val, delta_1_fx, delta_2_fx, delta_3_fx, delta_4_fx, delta_5_fx):
    i = 0
    return y[i] + (x_val - x[i]) * delta_1_fx[i] + (x_val - x[i]) * (x_val - x[i + 1]) * delta_2_fx[i] + (x_val - x[i]) * (x_val - x[i + 1]) * (x_val - x[i + 2]) * delta_3_fx[i] + (x_val - x[i]) * (x_val - x[i + 1]) * (x_val - x[i + 2]) * (x_val - x[i + 3]) * delta_4_fx[i] + (x_val - x[i]) * (x_val - x[i + 1]) * (x_val - x[i + 2]) * (x_val - x[i + 3]) * (x_val - x[i + 4]) * delta_5_fx[i]


x = [0, 10, 15, 20, 22.5, 30]
y = [0, 227.04, 362.78, 517.35, 602.97, 901.67]
x_val = 16

delta_1_fx = []
delta_2_fx = []
delta_3_fx = []
delta_4_fx = []
delta_5_fx = []

for i in range(1, len(x)):
    delta_1_fx = delta_1_fx + [(y[i] - y[i - 1]) / (x[i] - x[i - 1])]

for i in range(1, len(delta_1_fx)):
    delta_2_fx = delta_2_fx + [(delta_1_fx[i] - delta_1_fx[i - 1]) / (x[i + 1] - x[i - 1])]

for i in range(1, len(delta_2_fx)):
    delta_3_fx = delta_3_fx + [(delta_2_fx[i] - delta_2_fx[i - 1]) / (x[i + 2] - x[i - 1])]

for i in range(1, len(delta_3_fx)):
    delta_4_fx = delta_4_fx + [(delta_3_fx[i] - delta_3_fx[i - 1]) / (x[i + 3] - x[i - 1])]

for i in range(1, len(delta_4_fx)):
    delta_5_fx = delta_5_fx + [(delta_4_fx[i] - delta_4_fx[i - 1]) / (x[i + 4] - x[i - 1])]

print(f'Δ1fx: {delta_1_fx}')
print(f'Δ2fx: {delta_2_fx}')
print(f'Δ3fx: {delta_3_fx}')
print(f'Δ4fx: {delta_4_fx}')
print(f'Δ5fx: {delta_5_fx}')

print(f'\nAnswer: {formula(x, y, x_val, delta_1_fx, delta_2_fx, delta_3_fx, delta_4_fx, delta_5_fx)}')