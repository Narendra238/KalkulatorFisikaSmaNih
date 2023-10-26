print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Jarak (Y) pada arah sumbu Y (Y)')
percepatan = input('gravitasi (m/s^2):')
waktu = input('waktu (s):')
kecepatanawal= input('kecepatan awal pada sumbu y (m/s):')


try:
    a=float(percepatan)
    t=float(waktu)
    Vo=float(kecepatanawal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    S=Vo*t-(1/2)*a*t**2
    print('gravitasi:',a,'m/s^2')
    print('waktu:',t,'s')
    print('kecepatan awal pada sumbu y:',Vo,'m/s')

    print('Jarak (Y):',S,'m')
