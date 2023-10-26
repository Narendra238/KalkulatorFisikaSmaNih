print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#GHS (GERAK HARMONIK SEDERHANA ATAU OSILASI)
print('Mencari Kecepatan benda bergerak harmonik')

kec=input('Kecepatan Sudut (rad/s):')
amp=input('Amplitudo getaran(m):')
print('Masukan Nilai Cos, misal 0.1,0.5,1 dsb')
cos=input('Nilai Cos:')
twak=input('Waktu Getaran (s):')

try:
    a=float(amp)
    v=float(kec)
    s=float(cos)
    t=float(twak)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN/ANGKA! ')
else:
    x=v*a*s
    print('Amplitudo getaran :',a,'m')
    print('Nilai cos:',s,)
    print('Kecepatan sudut:',v,'rad/s')

    print('Kecepatan:',x,'m/s')
