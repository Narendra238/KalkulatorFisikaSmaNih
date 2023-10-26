print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#GHS (GERAK HARMONIK SEDERHANA ATAU OSILASI)
print('Mencari Percepatan gerak harmonik')

kec=input('Kecepatan Sudut (rad/s):')
sim=input('Simpangan(m):')


try:
    y=float(sim)
    v=float(kec)

except:
    print('INPUT BUKAN MERUPAKAN BILANGAN/ANGKA! ')
else:
    a=v**2*y
    print('Nilai simpangan(y) :',y,'m')
    print('Kecepatan sudut:',v,'rad/s')

    print('Percepatan:',a,'m/s^2')
