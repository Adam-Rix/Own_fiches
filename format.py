import random as rd                                                                              #import the bibl. for our needs

x = ['Olya', 'Silyutina', 350000, 3], ['Vanya', 'Slivov', 150000, 2], \
    ['Siva', 'Mara', 80000, 6], ['Milosh', 'Zeman', 100000, 4], ['Valentin', 'Bell', 9999999, 8] #create a lists with an info. of people

worker = rd.choice(x)                                                                            #randomise the values of the lists


status = '{} {} is {}'                                                                           #billet of a result

user_name = worker[0]                                                                            #rename parts of values of our lists
user_family = worker[1]

for i in worker:                                                                                 #who it will be: jun, mid, senior?
    if worker[-1] < 2:
        v = 'junior'
    elif worker[-1] >= 2 and worker[-1] <=5:
        v = 'middle'
    else:
        v = 'senior'

status = status.format(user_name, user_family, v)                                                #formatting the parts of our result

print(status)