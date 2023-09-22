# Input User

 # data yang dimasukkan pasti String
data = input('Masukkan data:')

print(f'data = {data}, type = {type(data)}')

# Jika ingin mengambil integer / float, maka
angka = float(input('Masukkan angka:'))
print(f'data = {float}, type = {type(float)}')

angka = int(input('Masukkan angka'))
print(f'data = {int}, type = {type(int)}')

# Bagaimana dengan Boolean
biner = bool(int(input('Masukkan nilai boolean 1 atau 0 :')))
print(f'data = {biner}, type = {type(biner)}')