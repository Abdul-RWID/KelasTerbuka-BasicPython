# a = 10, a adalah variabel dengan nilai 10

# tipe data: Integer >> Angka satuan yang gak ada koma
data_integer = 11
print(f'data : {data_integer}')
print(f'- bertipe : {type(data_integer)}')

# tipe data: Float >> angka dengan koma
data_float = 1.5
print(f'data : {data_float}')
print(f'- bertipe : {type(data_float)}')

# tipe data: String >> Kumpulan karakter
data_string = 'ucup'
print(f'data : {data_string}')
print(f'- bertipe : {type(data_string)}')

# tipe data: Boolean >> Biner True/False
data_bool = False
print(f'data : {data_bool}')
print(f'- bertipe : {type(data_bool)}')

## tipe data khusus

# Bilangan kompleks
data_complex = complex(5,6)
print(f'data : {data_complex}')
print(f'- bertipe : {type(data_complex)}')

# tipe data dari bahasa C

from ctypes import c_double

data_c_double = c_double(10.5)
print(f'data : {data_c_double}')
print(f'- bertipe : {type(data_c_double)}')