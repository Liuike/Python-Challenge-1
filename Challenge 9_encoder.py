# Caesar cipher with a keyword
# the keyword is PYTHON
# Below is the encoder

cipher_dict = [
    "P", "Y", "T", "H", "O", "N", "A", "B", "C", "D", "E", "F", "G", "I", "J", "K", "L", "M", "Q", "R", "S",
    "U", "V", "W", "X", "Z"
]

normal_dict = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
]

Message = "CIPHERS EVOLVE, JUST LIKE HOW THIS ONE IS BETTER CODED THAN THE LAST CAESAR CIPHY YOU\
DECODED. BUT STILL, PYTHON HELPS. HERE'S THE WORD YOU'RE LOOKING FOR: ARCHIMEDES."

Encoded_message = []

for i in Message:
    if i in normal_dict:
        Ciphered_char = cipher_dict[normal_dict.index(i)]
        Encoded_message.append(Ciphered_char)
    else:
        Encoded_message.append(i)


Encoded_message = ''.join(Encoded_message)
print(Encoded_message)