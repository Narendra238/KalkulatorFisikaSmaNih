print('Kalkulator Sederhana')
print('MUHAMMAD NARENDRA HAWARI')
#Gaya Gravitasi

print('mencari Percepatan gravitasi Newton')

print('Nilai G = 6.67*(10**(-11))')
grav=input('Konstanta Gravitasi (Nm^2/kg^2):6.67*(10**(-11)) ')
print('Massa Bumi : 6*(10**(24))')
massa=input('Massa Bumi  (kg):6*(10**(24))')
radius=input('Jarak tempat terhadap pusat bumi:')
tinggi=input('Jarak tinggi diatas permukaan bumi:')

try:
    g=6.67*(10**(-11))
    m=6*(10**(24))
    r=float(radius)
    h=float(tinggi)
    

except:
    print('INPUT BUKAN MERUPAKAN ANGKA / BILANGAN !!!!')

else:
    f=g*m
    e=((r+h)**2)
    w=f/e
    print('Massa Bumi :',m,'kg')
    print('Konstanta Gravitasi :',g,'Nm^2/kg^2')
    print('Jarak tempat terhadap pusat bumi:',r,)
    print('Jarak tinggi diatas permukaan bumi:',h,)
    
    print('Percepatan Gravitasi Newton:',w,'m/s^2')
