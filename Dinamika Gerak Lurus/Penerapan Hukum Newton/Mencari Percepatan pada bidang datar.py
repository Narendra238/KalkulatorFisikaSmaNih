print('Kalkulator Fisika')
print('MUHAMMAD NARENDRA HAWARI')
#DINAMIKA GERAK LURUS

print('Mencari Percepatan Pada bidang datar diberikan gaya secara horizontal')

gaya=input('Gaya kgm/s^2(Newton):')
massa=input('Massa  kg :')

try:
    f=float(gaya)
    m=float(massa)

except:
    print('Masukan Angka / bilangan !!')

else:
    a=f/m
    print('Gaya :',f,'kgm/s^2(Newton)')
    print('Massa:',m,'kg')

    print('Percepatan:',a,'m/s^2')
