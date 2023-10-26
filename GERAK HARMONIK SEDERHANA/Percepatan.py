print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#GHS (GERAK HARMONIK SEDERHANA ATAU OSILASI)
print('Mencari percepatan benda bergerak harmonik')

kec=input('Kecepatan Sudut (rad/s):')
sim=input('Simpangan (m):')



try:
    y=float(sim)
    v=float(kec)

except:
    print('INPUT BUKAN MERUPAKAN BILANGAN/ANGKA! ')
else:
    x=(-v**2)*y
    print('Simpangan(y) :',y,'m')
    print('Kecepatan sudut:',v,'rad/s')

    print('percepatan:',x,'m/s^2')
