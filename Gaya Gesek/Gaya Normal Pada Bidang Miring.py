print('Kalkulator Sederhana')
print('MUHAMMAD NARENDRA HAWARI')
#Gaya Normal

print('Mencari gaya Normal pada bidang datar)')

massa=input('Massa benda (kg) :')
grav=input('Gravitasi (m/s^2) :')
print('Masukan Nilai cos , misalnya 0.5,1 dsb')
cos=input('Nilai Cos:')

try:
    m=float(massa)
    g=float(grav)
    c=float(cos)
    
except:
    print('INPUT BUKAN MERUPAKAN ANGKA / BILANGAN !!!!')

else:
    f=m*g*c
    print('Massa Benda :',m,'kg')
    print('Gravitasi:',g,'m/s^2')
    print('Nilai cos:',c,)
    
    print('Gaya Normal:',f,'kgm/s^2')
