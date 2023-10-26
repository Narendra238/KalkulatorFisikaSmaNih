print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#GHS (GERAK HARMONIK SEDERHANA ATAU OSILASI)
print('Mencari Kecepatan Max benda bergerak harmonik')

kec=input('Kecepatan Sudut (rad/s):')
amp=input('Amplitudo getaran(m):')


try:
    a=float(amp)
    v=float(kec)
   
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN/ANGKA! ')
else:
    x=v*a
    print('Amplitudo getaran :',a,'m')
    print('Kecepatan sudut:',v,'rad/s')

    print('Kecepatan Max:',x,'m/s')
