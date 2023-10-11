# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah Boolean

# Tanda > , < , >= , <= , != , is , is not

a = 4
b = 2

# Lebih dari >
print('==== lebih dari (>) ====')
hasil = a > 3
print(f'{a} > 3 = {hasil}')
hasil = b > 3
print(f'{b} > 3 = {hasil}')
hasil = b > 2
print(f'{a} > 2 = {hasil}')

# Kurang dari <
print('==== kurang dari (<) ====')
hasil = a < 3
print(f'{a} < 3 = {hasil}')
hasil = b < 3
print(f'{b} < 3 = {hasil}')
hasil = b < 2
print(f'{a} < 2 = {hasil}')

# Lebih dari sama dengan >=
print('==== lebih dari sama dengan (>=) ====')
hasil = a >= 3
print(f'{a} >= 3 = {hasil}')
hasil = b >= 3
print(f'{b} >= 3 = {hasil}')
hasil = b >= 2
print(f'{a} >= 2 = {hasil}')

# Kurang dari sama dengan <=
print('==== kurang dari sama dengan (<=) ====')
hasil = a <= 3
print(f'{a} <= 3 = {hasil}')
hasil = b <= 3
print(f'{b} <= 3 = {hasil}')
hasil = b <= 2
print(f'{a} <= 2 = {hasil}')

# sama dengan (==)
print('==== sama dengan (==) ====')
hasil = a == 4
print(f'{a} == 4 = {hasil}')
hasil = b == 4
print(f'{b} == 4 = {hasil}')

# tidak sama dengan (!=)
print('==== sama dengan (!=) ====')
hasil = a != 4
print(f'{a} != 4 = {hasil}')
hasil = b != 4
print(f'{b} != 4 = {hasil}')


## 'is' sebagai komparasi object identity
print('==== object identity (is) ====')
x = 5 # ini adalah assignment membuat object
y = 5
print(f'nilai x = {x}, id = {hex(id(x))}')
print(f'nilai x = {y}, id = {hex(id(y))}')
hasil = x is y
print(f'x is y = {hasil}')

x = 5 # ini adalah assignment membuat object
y = 6
print(f'nilai x = {x}, id = {hex(id(x))}')
print(f'nilai x = {y}, id = {hex(id(y))}')
hasil = x is y
print(f'x is y = {hasil}')


## 'is not' sebagai komparasi object identity
print('==== object identity (is not) ====')
x = 5 # ini adalah assignment membuat object
y = 5
print(f'nilai x = {x}, id = {hex(id(x))}')
print(f'nilai x = {y}, id = {hex(id(y))}')
hasil = x is not y
print(f'x is not y = {hasil}')

x = 5 # ini adalah assignment membuat object
y = 6
print(f'nilai x = {x}, id = {hex(id(x))}')
print(f'nilai x = {y}, id = {hex(id(y))}')
hasil = x is not y
print(f'x is not y = {hasil}')