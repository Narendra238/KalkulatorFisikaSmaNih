print('<<<<<<<<<<Kalkulator Fisika Sederhana>>>>>>>>>>)
print('"MAS NARENDRO"')

#Gaya Newton

percepatan=input('Percepatan (m/s^2):')
massa=input('Massa (kg):')

try:
    a=float(percepatan)
    m=float(massa)

except:
    print('"Salah Input BORRRR!!!!!!"')

else:
    f=m*a
    print('Percepatan:',a,'m/s^2')
    print('Massa Benda:',m,'kg')

    print('Gaya :',F, 'kgm/s^2 atau Newton')
