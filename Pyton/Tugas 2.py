Saldo_Awal = 1000
Deposit = input('Masukkan Jumlah Deposit')
Utang = 9000

Saldo_Akhir = int(Deposit) - Utang

if Saldo_Akhir >= 0:
    print('Utang Anda Sudah Lunas')
else:
    print('Maaf Utang Anda Masih Belum Lunas')