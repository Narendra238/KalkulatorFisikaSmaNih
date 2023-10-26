print("Kalkulator FISIKA")
print("MUHAMMAD NARENDRA HAWARI")

#ROTASI

print('Mencari Percepatan Sentripetal (aS)')
kecepatan = input('kecepatan (m/s):')
jarijari = input('Jari-jari Putaran (m):')



try:
    v=float(kecepatan)
    r=float(jarijari)

except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    a=v**2/r
    print('percepatan:',v,'m/s')
    print('jari-jari putaran:',r,'m')
    

    print('Jarak (aS):',a,'m/s^2')
