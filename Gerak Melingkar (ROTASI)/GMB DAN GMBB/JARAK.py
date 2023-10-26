print("Kalkulator FISIKA")
print("MUHAMMAD NARENDRA HAWARI")

#ROTASI

print('Mencari Jarak (S)')
sudut = input('Sudut yang ditempuh (Radian):')
jarijari = input('Jari jari putaran (R):')


try:
    O=float(sudut)
    r=float(jarijari)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    S=O*r
    print('Sudut:',O,'Radian')
    print('Jari Jari:',r,'m')

    print('Jarak:',S,'m')
