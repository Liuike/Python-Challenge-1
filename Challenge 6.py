from __future__ import print_function

f = open('alice in wonderland')
text = f.read()
unwanted_char = [',', '.', '?','!','(',')','`',';',':','-']
main_dict = dict()

for i in unwanted_char:
    text = text.replace(i,'')


text_modified = text.split(' ')

for i in text_modified:
    if i in main_dict:
        main_dict[i] = main_dict[i]+1
    else:
        main_dict[i] = 1



main_dict = sorted(main_dict.items(), reverse= True, key=lambda x : x[1])

print(main_dict[3])