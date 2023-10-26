print("Kalkulator FISIKA")
print("MUHAMMAD NARENDRA HAWARI")

#ROTASI

print('Mencari sudut tempuh benda (θ)')
percepatan = input('percepatan sudut α (m/s^2):')
waktu = input('waktu (s):')
kecepatanawal= input('kecepatan sudut awal (rad/s):')


try:
    a=float(percepatan)
    t=float(waktu)
    Vo=float(kecepatanawal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    S=Vo*t+(1/2)*a*t**2
    print('percepatan sudut α:',a,'m/s^2')
    print('waktu:',t,'s')
    print('kecepatan sudut awal:',Vo,'rad/s')

    print('sudut tempuh benda (θ):',S,'m')
