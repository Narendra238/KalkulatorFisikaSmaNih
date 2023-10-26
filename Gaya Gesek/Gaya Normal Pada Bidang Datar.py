print('Kalkulator Sederhana')
print('MUHAMMAD NARENDRA HAWARI')
#Gaya Normal

print('Mencari gaya Normal pada bidang datar)')

massa=input('Massa benda (kg) :')
grav=input('Gravitasi (m/s^2) :')

try:
    m=float(massa)
    g=float(grav)

except:
    print('INPUT BUKAN MERUPAKAN ANGKA / BILANGAN !!!!')

else:
    f=m*g
    print('Massa Benda :',m,'kg')
    print('Gravitasi:',g,'m/s^2')

    print('Gaya Normal:',f,'kgm/s^2')
