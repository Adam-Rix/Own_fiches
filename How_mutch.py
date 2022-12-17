import numpy as np

x = np.array([120, 98, 150, 65, 42, 100, 190, 220, 140, 110, 88, 89, 100, 120,
                 50, 180, 155, 42, 89, 77, 200, 190, 125, 98, 77, 40, 39, 59, 30,
                 67])

y = np.mean(x)
u = np.median(x)

print('Our mean is =', y, '\nOur median is =', u)
print('===========')

r = 0
for i in x:
    if i > y:
        r += 1
print(r)
