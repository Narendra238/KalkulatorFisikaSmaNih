print('Kalkulator Sederhana')
print('MUHAMMAD NARENDRA HAWARI')
#Gaya Gravitasi

print('mencari gaya gravitasi Newton')

print('Nilai G= 6.67*(10**(-11))')
grav=input('Konstanta Gravitasi (Nm^2/kg^2): 6.67*(10**(-11))')
massa1=input('Massa Benda 1 (kg):')
massa2=input('Massa Benda 2 (kg):')
radius=input('Jarak Antara 2 Benda (m):')

try:
    g=6.67*(10**(-11))
    m=float(massa1)
    n=float(massa2)
    r=float(radius)

except:
    print('INPUT BUKAN MERUPAKAN ANGKA / BILANGAN !!!!')

else:
    f=g*m*n
    w=f/(r**2)
    print('Massa Benda 1:',m,'kg')
    print('Massa Benda 2:',n,'kg')
    print('Konstanta Gravitasi :',g,'Nm^2/kg^2')
    print('Jarak Antara Kedua Benda:',r,'m')

    print('Gaya Gravitasi Newton:',w,'kgm/s^2')
