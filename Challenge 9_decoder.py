# Caesar cipher with a keyword
# the keyword is PYTHON
# Below is the decoder

cipher_dict = [
    "P", "Y", "T", "H", "O", "N", "A", "B", "C", "D", "E", "F", "G", "I", "J", "K", "L", "M", "Q", "R", "S",
    "U", "V", "W", "X", "Z"
]

normal_dict = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
]

Cipher = "TCKBOMQ OUJFUO, DSQR FCEO BJV RBCQ JIO CQ YORROM TJHOH RBPI RBO FPQR TPOQPM TCKBX XJSHOTJHOH. \
YSR QRCFF, KXRBJI BOFKQ. BOMO'Q RBO VJMH XJS'MO FJJECIA NJM: PMTBCGOHOQ."

Decoded_message = []

for i in Cipher:
    if i in cipher_dict:
        Deciphered_char = normal_dict[cipher_dict.index(i)]
        Decoded_message.append(Deciphered_char)
    else:
        Decoded_message.append(i)


Decoded_message = ''.join(Decoded_message)
print(Decoded_message)