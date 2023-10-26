print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#GHS (GERAK HARMONIK SEDERHANA ATAU OSILASI)
print('Mencari Simpangan (y)')

kec=input('Kecepatan Sudut (rad/s):')
amp=input('Amplitudo getaran(m):')
print('Masukan Nilai Sin, misal 0.1,0.5,1 dsb')
sin=input('Nilai Sin:')
twak=input('Waktu Getaran (s):')

try:
    a=float(amp)
    v=float(kec)
    s=float(sin)
    t=float(twak)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN/ANGKA! ')
else:
    y=a*s*v*t
    print('Amplitudo getaran :',a,'m')
    print('Nilai sin:',s,)
    print('Kecepatan sudut:',v,'rad/s')
    print('waktu getaran:',t,'s')

    print('Simpangan:',y,'m')
