# Buat program yang meminta input nama dari pengguna dan menampilkan pesan "Hallo <nama>!"

#nama = input("Siapa Nama Mu? ")
#print(f"Hello, {nama} !")

# Buat program yang meminta data angka dari pengguna dan mencetak apakah angka tersebut ganjil atau genap

while True:
    try:
        angka =int(input("Masukan angka: "))
        break
    except ValueError:
        print("Tolong masukan angka")


if angka % 2 == 0:
    print(f"{angka} adalah angka genap")

else:
    print(f"{angka} adalah angka ganjil")