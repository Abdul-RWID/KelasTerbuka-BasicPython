# Latihan konversi satuan temperature

'''
Konversi Celsius ke satuan lain
'''
def celcius():
    print('\nProgram Konversi Celcius\n')

    celcius = float(input('Masukkan suhu dalam celcius : '))
    print(f'suhu adalah {celcius} Celcius')

    # reamur
    reamur = (4/5) * celcius
    print(f'suhu dalam reamur adalah {reamur} Reamur')

    # fahrenheit
    fahrenheit = ((9/5) * celcius) + 32
    print(f'suhu dalam fahrenheit adalah {fahrenheit} Fahrenheit')

    # Kelvin
    kelvin = celcius + 273
    print(f'suhu dalam kelvin adalah {kelvin} Kelvin')

celcius()

'''
Reamur
Celcius    = (5/4) * Reamur
Fahrenheit = ((9/4)*Reamur) + 32
Kelvin     = ((5/4)*R) + 273

Fahrenheit
Celcius = (5/9)*(Fahrenheit-32)
Reamur  = (4/9)*(Fahrenheit-32)
Kelvin  = Celcius + 273

Kelvin
Celcius    = K - 273
Reamur     = (4/5) * (K-273)
Fahrenheit = ((9/5)*Celcius) + 32
'''