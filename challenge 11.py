import random

file_name_lst = []
count = 0
num_list = []
for i in range(1000):
    num_list.append(i)

while True:
    add = random.randint(1,500)
    file_name = num_list[count] + add
    if file_name in file_name_lst:
        count -= 1
    else:
        file_name_lst.append(file_name)
    count += 1
    if count == 1000:
        break

print(file_name_lst)




