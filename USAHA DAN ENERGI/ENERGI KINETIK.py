print("Kalkulator FISIKA USAHA&ENERGI")
print("MUHAMMAD NARENDRA HAWARI")

#EK/Energi Kinetik : EK = (1/2)*m*v**2

massa = input('Massa benda (kg):')
kecepatan = input('Kecepatan Benda (m/s):')

try:
    m=float(massa)
    v=float(kecepatan)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    EK=(1/2)*m*v**2
    print('Massa:',m,'kg')
    print('Kecepatan:',v,'m/s')

    print('Energi Kinetik:', EK,'Joule/kgm^2s^2')
