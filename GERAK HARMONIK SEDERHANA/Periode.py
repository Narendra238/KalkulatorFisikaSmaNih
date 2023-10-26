print('Kalkulator Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#ROTASI

print('Mencari Periode')
jumlah=input('banyaknya putaran: (n)')
waktu=input ('waktu putaran: (t)')

try:
    n=float(jumlah)
    t=float(waktu)
    
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!!!!')

else:
    p=t/n
    print('banyak putaran:', n ,)
    print('waktu putaran:' ,t , 's')

    print('Periode :',p, 's')

print('~Mencari Periode apabila diketahui frekuensi~')
frekuensi=input('frekuensi:(Hz)')
try:
    f=float(frekuensi)
    
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!!')
else:
    g=1/f
    print('frekuensi:',f,'Hz')

    print('Periode:',g, 's')
