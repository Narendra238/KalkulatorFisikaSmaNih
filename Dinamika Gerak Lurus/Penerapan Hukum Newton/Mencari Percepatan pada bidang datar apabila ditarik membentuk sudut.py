print('Kalkulator Fisika')
print('MUHAMMAD NARENDRA HAWARI')
#DINAMIKA GERAK LURUS

print('Mencari Percepatan Pada bidang datar diberikan gaya membentuk sudut')

gaya=input('Gaya kgm/s^2(Newton):')
massa=input('Massa  kg :')
print('MASUKAN NILAI COS SAJA , MISALNYA 0.5 , 1,dsb')
cos=input('Nilai Cos:')

try:
    f=float(gaya)
    m=float(massa)
    c=float(cos)

except:
    print('Masukan Angka / bilangan !!')

else:
    a=(f*c)/m
    print('Gaya :',f,'kgm/s^2(Newton)')
    print('Massa:',m,'kg')
    print('Nilai Cos:',c,)

    print('Percepatan:',a,'m/s^2')
