# Challenge 2
# Wrote by Rock_Z

# Decoder below

original_str = ""

decoded_str = ""

for i in original_str:
    num = ord(i)
    if 122 >= num >= 97:
        num = ((num+2)-97)%26+97
    i = chr(num)
    decoded_str = decoded_str + i

print(decoded_str)