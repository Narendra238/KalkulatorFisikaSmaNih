print('Kalkulator Sederhana')
print('MUHAMMAD NARENDRA HAWARI')
#Gaya Gesek

print('mencari gaya gesek statis(diam/tepat akan bergerak)')

nor=input('Gaya Normal (N) :')
mu=input('Koefisien gesekan statis:')

try:
    n=float(nor)
    m=float(mu)

except:
    print('INPUT BUKAN MERUPAKAN ANGKA / BILANGAN !!!!')

else:
    f=m*n
    print('Gaya Normal:',n,'kgm/s^2')
    print('Koefisien gesekan Statis:',m,)

    print('Gaya gesek statis:',f,'kgm/s^2')

