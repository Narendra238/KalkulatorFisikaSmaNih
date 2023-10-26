print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')
#ROTASI

print('Mencari Kecepatan Translasi Roda (m/s)')

kecepatan=input('Kecepatan Sudut: (rad/s)')
jarijari=input('Jari-jari putaran: ')

try:
    v=float(kecepatan)
    r=float(jarijari)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    a=v*r
    print('Kecepatan Sudut:',v,'rad/s')
    print('Jari-jari putaran:',r,'m')


    print('Kecepatan Tranlasi:',a,'m/s')
