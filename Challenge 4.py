

import math

Total_number = int(input('Please input number: '))
Prime_number_count = 0
Divisor = 0
time = 0

for i in range (Total_number):
    num = i + 1
    if num > 1:
        Divisor = 0
        for i in range (2, num):
            if num % i == 0:
                Divisor = Divisor + 1
        if Divisor == 0:
            Prime_number_count = Prime_number_count + 1
    time += 1
    if time % 1000 == 0:
        print('*')

print ("total prime number count =", str(Prime_number_count))
