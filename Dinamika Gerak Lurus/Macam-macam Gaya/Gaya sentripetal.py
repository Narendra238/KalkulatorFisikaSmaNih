print("Kalkulator FISIKA")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari gaya sentripetal (Fs)')
massa = input('massa (kg):')
kec=input('Kecepatan :')
jari=input('Jari-jari putaran :')


try:
    v=float(kec)
    m=float(massa)
    r=float(jari)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    f=m*v**2/r
    print('kecepatan benda :',v,'m/s')
    print('massa benda:',m,'kg')
    print('jari-jari benda:',r,'m')

    
    print('Gaya sentripetal :',f,'kgm/^2')
