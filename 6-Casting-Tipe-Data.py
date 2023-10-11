# Belajar Casting Tipe Data
# Merubah dari satu tipe ke tipe lain
# Tipe data = int, float, str, bool

## INTEGER
print('====INTEGER====')
data_int = 9
print(f'data = {data_int}, type = {type(data_int)}')

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int) # akan FALSE jika nilai int = 0
print(f'data = {data_float}, type = {type(data_float)}')
print(f'data = {data_str}, type = {type(data_str)}')
print(f'data = {data_bool}, type = {type(data_bool)}')

## FLOAT
print('====FLOAT====')
data_float = 9.9
print(f'data = {data_float}, type = {type(data_float)}')

data_int   = int(data_float)    # akan dibulatkan ke bawah
data_str   = str(data_float)
data_bool  = bool(data_float)
print(f'data = {data_int}, type = {type(data_int)}')
print(f'data = {data_str}, type = {type(data_str)}')
print(f'data = {data_bool}, type = {type(data_bool)}')

## BOOLEAN
print('====BOOLEAN====')
data_bool = True
print(f'data = {data_bool}, type = {type(data_bool)}')

data_int   = int(data_bool)
data_str   = str(data_bool)
data_float  = bool(data_bool)
print(f'data = {data_int}, type = {type(data_int)}')
print(f'data = {data_str}, type = {type(data_str)}')
print(f'data = {data_float}, type = {type(data_float)}')

## STRING
print('====STRING====')
data_str = '10'
print(f'data = {data_str}, type = {type(data_str)}')

data_int   = int(data_str)  # string harus angka
data_bool   = bool(data_str) # False jika string kosong
data_float  = float(data_str)    # string harus angka
print(f'data = {data_int}, type = {type(data_int)}')
print(f'data = {data_bool}, type = {type(data_bool)}')
print(f'data = {data_float}, type = {type(data_float)}')