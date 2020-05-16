import random


#encoder
list = []
list_small = ['m','o','u','n','t','a','i','n']
count_total = 0
count_for_small = 0

for i in range(80000):
    if count_total % 500 == 0 and count_total != 0:
        list.append('\n')
    if count_total % 10000 == 0:
        list.append(list_small[count_for_small])
        count_for_small += 1

    x = random.randint(65, 90)
    list.append(chr(x))

    count_total += 1

list = ''.join(list)
print(list)




#decoder
decoded = ''
f = open('file for lowercase in uppercase')
text = f.read()

for i in text:
    if i.islower() == True:
        decoded += i

print(decoded)
