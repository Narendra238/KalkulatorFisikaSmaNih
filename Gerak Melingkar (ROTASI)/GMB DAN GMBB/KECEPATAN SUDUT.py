print("Kalkulator FISIKA")
print("MUHAMMAD NARENDRA HAWARI")

#ROTASI

print('Mencari Kecepatan sudut(rad/s)')
sudut = input('sudut (radian):')
waktu = input('waktu (s):')


try:
    S=float(sudut)
    t=float(waktu)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    v=S/t
    print('sudut tempuh:',S,'radian')
    print('waktu:',t,'s')

    print('Kecepatan sudut:',v,'rad/s')
    
print('Mencari Kecepatan sudut apabila diketahui Periode')
periode=input('periode:(s)')
sudut = input('sudut (radian):')
try:
    p=float(periode)
    S=float(sudut)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    q=S/p
print('Periode:',p,'s')

print('Kecepatan sudut:',q, 'rad/s')


print('Mencari Kecepatan sudut apabila diketahui Frekuensi')
frekuensi=input('Frekuensi:(Hz)')
sudut = input('sudut (radian):')
try:
    f=float(frekuensi)
    S=float(sudut)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    w=S*f
print('Frekuensi:',f,'Hz')

print('Kecepatan sudut:',w, 'rad/s')
