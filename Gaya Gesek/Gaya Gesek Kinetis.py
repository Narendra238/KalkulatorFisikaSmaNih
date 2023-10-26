print('Kalkulator Sederhana')
print('MUHAMMAD NARENDRA HAWARI')
#Gaya Gesek

print('mencari gaya gesek kinetis(bergerak)')

nor=input('Gaya Normal (N) :')
mu=input('Koefisien gesekan kinetis:')

try:
    n=float(nor)
    m=float(mu)

except:
    print('INPUT BUKAN MERUPAKAN ANGKA / BILANGAN !!!!')

else:
    f=m*n
    print('Gaya Normal:',n,'kgm/s^2')
    print('Koefisien gesekan kinetis:')

    print('Gaya gesek kinetis:',f,'kgm/s^2')
