usia = 0

# == sama dengan
# > lebih dari
# < kurang dari
# != tidak sama dengan
# >= lebih dari sama dengan
# <= kurang dari sama dengan

if usia == 0:
    print('Belum Lahir')
elif usia > 0 and usia <= 3:
    print('Masih Bayi')
elif usia > 3 and usia <= 10:
    print('Masih Anak-Anak')
elif usia > 10 and usia <= 20:
    print('Sudah Remaja')
else:
    print('Sudah Dewasa')