print("Kalkulator FISIKA")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari gaya berat (w)')
percepatan = input('percepatan gravitasi (m/s^2):')
massa = input('massa (kg):')


try:
    g=float(percepatan)
    m=float(massa)
    
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    w=m*g
    print('percepatan gravitasi:',g,'m/s^2')
    print('massa benda:',m,'kg')

    print('Gaya berat :',w,'kgm/^2')
