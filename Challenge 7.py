import random
#97-122
#65 - 90
#PROgraMED

list_letter = ['P','R','O','g','r','a','M','E','D']
num_lower = range(98,102) + range(104,113) + range(115,122)
num_caps = range(65, 67) + range(70,76)+ range(78,78) + range(81,81) + range(82,90)
main_str = ''

for i in range(9000):
    x = random.randint(1,5)
    if x > 1:
        pick = random.choice(num_lower)
        main_str += chr(pick)
    else:
        pick = random.choice(num_caps)
        main_str += chr(pick)
    if i%5000 == 0 and i != 0:
        main_str += 'PROgraMED'

list = []
list_reference = [True,True,True,False,False,False,True,True,True]
list_answer = []

def split(word):
    return [char for char in word]

list_proto = split(main_str)
count = 0
count_total = 0
for j in list_proto:
    for i in range(9):
        y = list_proto[count+count_total]
        x = y.isupper()
        list_answer.append(x)
        list.append(y)
        count += 1
    if list_answer == list_reference:
        print(list)
        break
    count_total += 1

    list_answer = []
    list = []
    count = 0




