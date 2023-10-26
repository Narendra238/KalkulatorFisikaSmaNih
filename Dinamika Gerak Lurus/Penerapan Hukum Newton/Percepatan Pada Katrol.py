print('Kalkulator Fisika')
print('MUHAMMAD NARENDRA HAWARI')
#DINAMIKA GERAK LURUS

print('Mencari Percepatan Pada Katrol')


massa1=input('Massa 1 kg :')
massa2=input('Massa 2 kg :')
grav=input('Gravitasi m/s^2 :')


try:
 
    m=float(massa1)
    c=float(massa2)
    g=float(grav)

except:
    print('Masukan Angka / bilangan !!')

else:
    b=(m-c)*g
    a=b/(m+c)

    print('Massa 1:',m,'kg')
    print('Gravitasi m/s^2 :',g,'m/s^2')
    print('Massa 2:',c,'kg')

    print('Percepatan:',a,'m/s^2')
