# Soal Pertama ==> ------ 0 +++++ 5 ------ 8 +++++ 11 ------
# Soal Kedua ==> +++++ 0 ----- 5 +++++ 8 ----- 11 +++++


#Soal Pertama
print('=====Soal Pertama=====')
#Variabel nya >0 = True, <5 = True, >8 = True, <11 = True, ini adalah soal slicing 
#kita coba dengan 'and'

inputUser = float(input('Masukkan nilai antara 0-5 atau 8-11 ? '))

#Slice 0-5 (slicePertama)
lebihDari_zero = (inputUser >= 0)
kurangDari_lima = (inputUser <= 5)

slicePertama = lebihDari_zero and kurangDari_lima
#print(slicePertama)

#Slice 8-11 (sliceKedua)
lebihDari_delapan = (inputUser >= 8)
kurangDari_sebelas = (inputUser <= 11)

sliceKedua = lebihDari_delapan and kurangDari_sebelas
#print(sliceKedua)

#untuk hasil kita akan menggunakan penggabungan dua potongan dan kita akan menggunakan 'or'
hasil = slicePertama or sliceKedua
print('Your Answer is ',hasil)



#Soal Kedua
print('=====Soal Kedua=====')

#Variabelnya = <0 = True, >5 = True, <8 = True, >11 = True
#Pada variabel diatas kita akan memotong nilai diantara 5 dan 8 kita akan menggunakan 'and'
#untuk nilai 0 dan 11 kita akan menggabung kan kedua nilai dan akan menggunakan 'or'
#untuk penggabungan nilai akhir kita coba menggunakan 'or'

inputUser = float(input('Masukkan nilai kurang dari 0, diantara 5-8 atau nilai lebih dari 11 ? '))

#Variable Pertama
kurangDari_zero = (inputUser < 0)
lebihDari_sebelas = (inputUser >= 11)

hasilGabung = kurangDari_zero or lebihDari_sebelas

#Slice 5-8
kurangDari_delapan = (inputUser <= 8)
lebihDari_lima = (inputUser >= 5)

hasilSlice = kurangDari_delapan and lebihDari_lima



hasil = hasilGabung or hasilSlice
print('Your Answer is ',hasil)
