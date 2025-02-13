# Membuat gabungan area rentang dari angka

#Soal pertama ==> +++++3-------10++++++ ( Jika nilai kurang dari 3 True dan lebih dari 10 True)

#inputUser = float(input('Silahkan masukkan angka kurang dari 3 atau lebih dari 10 : '))

#Memeriksa Input User

#kurangDari = (inputUser < 3)
#lebihDari = (inputUser > 10)

#if inputUser < 3:
    #print(kurangDari)
#elif inputUser > 10:
    #print(lebihDari)
#else:
    #print(False)

#The Logic = Kita ingin jika nilai 'a = <3 = True' dan 'b= >10=True'
#Jika nilai salah satu True maka Hasilnya True
#Contohnya seperti ini jika user menginput nilai 2 maka nila a = True dan b = False, 
#Maka hasil akhirnya akan menjadi True karena perintahnya adalah jika nilainya <3 = True atau >10 = True
#Perhatikan kata "Atau"

InputUser = float(input('Silahkan masukkan angka kurang dari 3 atau lebih dari 10 : '))

kurangDari = (InputUser < 3)
lebihDari = (InputUser > 10)

jawabanBenar = kurangDari or lebihDari
print('Jawaban mu',jawabanBenar)

print('\n',10*'=','\n')
#Soal kedua irisan -------3++++++10------- (Diantara angka 3 dan 10 True)
#The Logic = Kita ingin hasil '> 3 = True' dan hasil dari '< 10 = True' jika hanya salah satunya bernilai True maka hasilnya tetap False

InputUser = float(input('Silahkan masukkan angka lebih dari 3 atau kurang dari 10 : '))

kurangDari =(InputUser < 10)
lebihDari =(InputUser > 3)

jawabanBenar = kurangDari and lebihDari
print('Jawaban mu',jawabanBenar)



