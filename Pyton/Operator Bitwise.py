# Operasi bitwise, biner atau binery

a = 8
b = 5

# bitwise OR (|)

c = a | b
print('\n=====OR=====')
print('nilai :',a, ' , binary : ',format(a,'08b'))
print('nilai :',b, ' , binary : ',format(b,'08b'))
print('nilai :',c, ' , binary : ',format(c,'08b'))

# bitwise AND (&)

c = a & b
print('\n=====AND=====')
print('nilai :',a, ' , binary : ',format(a,'08b'))
print('nilai :',b, ' , binary : ',format(b,'08b'))
print('nilai :',c, ' , binary : ',format(c,'08b'))

# bitwise XOR (^)
c = a ^ b
print('\n=====XOR=====')
print('nilai :',a, ' , binary : ',format(a,'08b'))
print('nilai :',b, ' , binary : ',format(b,'08b'))
print('nilai :',c, ' , binary : ',format(c,'08b'))

# bitwise NOT (~)
c = ~a
print('\n=====NOT=====')
print('nilai :',a, ' , binary : ',format(a,'08b'))
print('nilai :',c, ' , binary : ',format(c,'08b'))

# shifting

# shifing right (>>)
c = a >> 2
print('\n=====SHIFTING RIGHT=====')
print('nilai :',a, ' , binary : ',format(a,'08b'))
print('nilai :',c, ' , binary : ',format(c,'08b'))

# shifing right (<<)
c = a << 2
print('\n=====SHIFTING LEFT=====')
print('nilai :',a, ' , binary : ',format(a,'08b'))
print('nilai :',c, ' , binary : ',format(c,'08b'))