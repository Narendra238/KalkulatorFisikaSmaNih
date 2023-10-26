print('Kalkulator Fisika')
print('MUHAMMAD NARENDRA HAWARI')
#DINAMIKA GERAK LURUS

print('Mencari Percepatan Pada bidang miring')


massa=input('Massa  kg :')
grav=input('Gravitasi m/s^2 :')
print('MASUKAN NILAI Sin SAJA , MISALNYA 0.5 , 1,dsb')
sin=input('Nilai sin:')

try:
 
    m=float(massa)
    c=float(sin)
    g=float(grav)

except:
    print('Masukan Angka / bilangan !!')

else:
    a=(m*g*c)/m

    print('Massa:',m,'kg')
    print('Gravitasi m/s^2 :',g,'m/s^2')
    print('Nilai sin:',c,)

    print('Percepatan:',a,'m/s^2')
