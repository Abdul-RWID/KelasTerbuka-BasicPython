## Operasi Aritmatika

a = 10
b = 3

# operasi tambah +
hasil = a + b
print(f'a + b = {hasil}')

# operasi kurang -
hasil = a - b
print(f'a - b = {hasil}')

# operasi kali *
hasil = a * b
print(f'a * b = {hasil}')

#operasi bagi /
hasil = a / b
print(f'a / b = {hasil}')

# operasi eksponen (pangkat) **
hasil = a ** b
print(f'a ** b = {hasil}')

# operasi modulus (sisa pembagian) %
hasil = a % b
print(f'a % b = {hasil}')

# operasi floor division (kebalikan modulus) //
hasil = a // b
print(f'a // b = {hasil}')

# prioritas operasi, operational presedence
'''
    1. Parenthenes()
    2. Exponen **
    3. Perkalian dkk * / % //
    4. Pertambahan + Pengurangan -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y % z // x
print(f'x ** y * z + x / y % z // x = {hasil}')