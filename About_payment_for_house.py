import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000,
                 160000, 230000, 280000, 290000, 300000, 500000,
                 420000, 100000, 150000, 280000])

u = np.mean(data)                   #The average value
o = np.median(data)

print('Our mean is = ', u, '\nOur median is =', o)

x = int(np.std(data))               #The standard deviation


r = 0
for i in data:
   if i > u-x and i < u+x:
       r += 1
#print(r)

y = (r/len(data)) * 100
print(y)

