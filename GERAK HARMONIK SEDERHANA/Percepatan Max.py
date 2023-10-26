print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#GHS (GERAK HARMONIK SEDERHANA ATAU OSILASI)
print('Mencari percepatan max benda bergerak harmonik')

kec=input('Kecepatan Sudut (rad/s):')
amp=input('Amplitudo getaran(m):')


try:
    a=float(amp)
    v=float(kec)

except:
    print('INPUT BUKAN MERUPAKAN BILANGAN/ANGKA! ')
else:
    x=(-v**2)*a
    print('Amplitudo(a) :',a,'m')
    print('Kecepatan sudut:',v,'rad/s')

    print('percepatan max:',x,'m/s^2')
