import random

# acak angka
a = 1
b = 10
acak = random.randint(a, b)

# input user
inputUser = int(input('Silahkan tebak angka, mulai dari angka 1 sampai 10 = '))

# output program

# LOGIC = selama input user tidak sama dengan variabel acak maka program akan mengulang perintah while 
# yg berisi perintah if dan else, jika inputUser sama dengan variabel acak maka perintah while tidak akan di eksekusi 
# dan perintah print setelah while akan langsung di eksekusi

while inputUser != acak:
    if inputUser < acak:
        print('Tebakanmu terlalu rendah')
    else:
        print('Tebakanmu terlalu tinggi')
    inputUser = int(input('Coba lagi : '))

print('Selamat tebakan mu benar')

