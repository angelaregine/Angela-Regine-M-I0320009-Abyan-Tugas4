berat_bagasi = float(input('Masukkan berat koper(kg): '))
berat_bagasi = berat_bagasi * 2.2
y = berat_bagasi <= 50
if y == True:
    print(True, ': diperbolehkan masuk ke dalam pesawat')
else:
    print(False, ': tidak diperbolehkan masuk ke dalam pesawat')