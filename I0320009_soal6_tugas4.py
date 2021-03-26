a = 4               # 4  = 0100
b = 11              # 11 = 1011
c = 0

c = a | b           # 15 = 1111
print("Hasil dari 4 | 11 adalah", c)

c = a >> b          # 0  = 0000
print("Hasil dari 4 >> 11 adalah", c)

c = a ^ b           # 15 = 1111
print("Hasil dari 4 ^ 11 adalah", c)

c = ~a              # -5 = 0101
print("Hasil dari ~4 adalah", c)

c = b & a           # 0 =  0000
print("Hasil dari 11 & 4 adalah", c)