print('Kalkulator Sederhana')
print('MUHAMMAD NARENDRA HAWARI')
#Gaya Gravitasi

print('mencari Medan gravitasi Newton')

print('Nilai G = 6.67*(10**(-11))')
grav=input('Konstanta Gravitasi (Nm^2/kg^2):6.67*(10**(-11)) ')
massa1=input('Massa Benda  (kg):')
radius=input('Jarak Benda (m):')

try:
    g=6.67*(10**(-11))
    m=float(massa1)
    r=float(radius)

except:
    print('INPUT BUKAN MERUPAKAN ANGKA / BILANGAN !!!!')

else:
    f=g*m
    w=f/(r**2)
    print('Massa Benda :',m,'kg')
    print('Konstanta Gravitasi :',g,'Nm^2/kg^2')
    print('Jarak:',r,'m')

    print('Medan Gravitasi Newton:',w,'m/s^2')
