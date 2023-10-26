print('Kalkulator Fisika')
print('MUHAMMAD NARENDRA HAWARI')
#DINAMIKA GERAK LURUS

print('Mencari Gaya Normal Pada Lift Naik Ke atas')


massa=input('Massa  kg :')
grav=input('Gravitasi m/s^2 :')
per=input('Percepatan m/s^2 :')

try:
 
    m=float(massa)
    a=float(per)
    g=float(grav)

except:
    print('Masukan Angka / bilangan !!')

else:
    N=(m*a)+(m*g)

    print('Massa:',m,'kg')
    print('Gravitasi m/s^2 :',g,'m/s^2')
    print('Percepatan:',a,'m/s^2')

    print('Gaya Normal:',N,'m/s^2')
