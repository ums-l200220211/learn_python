pilihan = input("Masukkan pilihan konversi suhu (C ke F atau F ke C): ")
if pilihan == "1":
    suhu = float(input("Masukkan suhu dalam Celcius: ")) # konversi input ke float
    fahrenheit = (9/5) * suhu + 32
    print("Suhu dalam Fahrenheit adalah: ", fahrenheit)
elif pilihan == "2":
    suhu = float(input("Masukkan suhu dalam Fahrenheit: ")) # konversi input ke float
    celcius = (5/9) * (suhu - 32)
    print("Suhu dalam Celcius adalah: ", celcius)
else:
    print("Pilihan tidak valid")

