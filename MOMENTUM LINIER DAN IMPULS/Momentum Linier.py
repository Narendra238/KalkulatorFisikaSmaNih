print('Kalkulator sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#MOMENTUM DAN IMPULS

print('Mencari Momentum Linier')

kec=input('Kecepatan (m/s):')
massa=input('Massa (kg):')

try:
    v=float(kec)
    m=float(massa)
except:
    print('Input Bukan Merupakan Bilangan!')
else:
    p=m*v
    print('Kecepatan :',v,'m/s')
    print('Massa:',m,'kg')

    print('Momentum:',p,'Ns atau Kgm/s')
