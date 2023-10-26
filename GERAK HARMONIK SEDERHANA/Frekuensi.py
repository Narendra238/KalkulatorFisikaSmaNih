print('Kalkulator Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#ROTASI

print('Mencari frekuensi')
jumlah=input('banyaknya putaran: (n)')
waktu=input ('waktu putaran: (t)')

try:
    n=float(jumlah)
    t=float(waktu)
    
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')

else:
    f=n/t
    print('banyak putaran:', n ,)
    print('waktu putaran:' ,t , 's')

    print('frekuensi:',f, 'Hz')

print('~Mencari frekuensi apabila diketahui periode~')
periode=input('Periode: (s)')

try:
     p=float(periode)

except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    s=1/p
print('periode:',p,'s')
print('frekuensi:',s,'Hz')
