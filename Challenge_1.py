# Challenge 2
# Wrote by Rock_Z

# Decoder below

original_str = "promofpba yv qeb ibkdqe? vbp, tb fkqbkqflkxiiv jxab qeb pqofkd qefp ilkd ybzxrpb tb txkqba vlr ql hklt elt jrze jlob bccfzfbkq mvqelk fp qexk vlro yxob exkap. klt exsb qeb hbv: qeb roi clo qeb kbuq zexiibkdb bkap tfqe zxbpxo.eqji"

decoded_str = ""

for i in original_str:
    num = ord(i)
    if 122 >= num >= 97:
        num = ((num+3)-97)%26+97
    i = chr(num)
    decoded_str = decoded_str + i

print(decoded_str)

