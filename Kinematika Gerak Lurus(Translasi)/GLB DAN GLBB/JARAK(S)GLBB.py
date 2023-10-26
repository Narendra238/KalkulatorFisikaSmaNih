print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Jarak dari GLBB (S)')
percepatan = input('percepatan (m/s^2):')
waktu = input('waktu (s):')
kecepatanawal= input('kecepatan awal (m/s):')


try:
    a=float(percepatan)
    t=float(waktu)
    Vo=float(kecepatanawal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    S=Vo*t+(1/2)*a*t**2
    print('percepatan:',a,'m/s^2')
    print('waktu:',t,'s')
    print('kecepatan awal:',Vo,'m/s')

    print('Jarak (S):',S,'m')
