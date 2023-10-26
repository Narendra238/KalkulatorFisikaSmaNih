
print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')
#ROTASI

print('Mencari Percepatan Roda/linier (m/s^2)')

kecepatan=input('Kecepatan Sudut: (rad/s)')
jarijari=input('Jari-jari putaran: (m)')

try:
    v=float(kecepatan)
    r=float(jarijari)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    a=v*r
    print('Kecepatan Sudut:',v,'rad/s')
    print('Jari-jari putaran:',r,'m')


    print('Percepatan roda:',a,'m/s^2')
