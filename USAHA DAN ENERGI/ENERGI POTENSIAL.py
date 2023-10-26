print("Kalkulator FISIKA USAHA&ENERGI")
print("MUHAMMAD NARENDRA HAWARI")

#EP/Energi Potensial : EP = m*g*h

massa = input('massa (kg):')
gravitasi = input('gravitasi (m/s^2):')
ketinggian = input('ketinggian (m):')

try:
    m=float(massa)
    g=float(gravitasi)
    h=float(ketinggian)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    EP=m*g*h
    print('Massa:',m,'kg')
    print('Gravitasi:',g,'m/s^2')
    print('Ketinggian:' ,h,'m')

    print('Energi Potensial:', EP,'Joule/kgm^2s^2')
