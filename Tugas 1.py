# 1. Buatlah program validasi login dengan if-else
user_name = input('Masukkan User Name: ')
password = input('Masukkan Password: ')

if user_name == "admin" and password == "admin1234":
    print("Login Berhasil")

else:
    print("Username & Password Salah")

# 2. Buat loop for yang mencetak angka dari 1-10
for angka in range(1,   101):
    print("Loop ke-", angka)

# 3. Buat loop while yang meminta user memasukkan angka hingga mereka mengetik angka 0

angka = '0'
tebak = ''

while tebak != angka:
    tebak = input('Tebak Sebuah Angka Rahasia: ')
    if tebak != angka:
        print("Anda Belum Beruntung! Ayo Coba Lagi!")

print("Selamat Anda Pemenangnya!!")