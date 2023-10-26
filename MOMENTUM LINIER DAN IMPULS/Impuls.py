print('Kalkulator sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#MOMENTUM DAN IMPULS

print('Mencari Impuls')

gaya=input('Gaya (N):')
swak=input('Selang Waktu (s):')


try:
    f=float(gaya)
    t=float(swak)
except:
    print('Input Bukan Merupakan Bilangan!')
else:
    i=f*t
    print('Gaya :',f,'N')
    print('Selang Waktu:',t,'s')

    print('Impuls:',i,'Ns atau Kgm/s')
