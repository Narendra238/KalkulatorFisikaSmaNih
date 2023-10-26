print("Kalkulator FISIKA GLB")
print("MUHAMMAD NARENDRA HAWARI")

#GLB

print('Mencari Jarak(S)')
kecepatan = input('kecepatan (m/s):')
waktu = input('waktu (s):')


try:
    v=float(kecepatan)
    t=float(waktu)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    S=v*t
    print('kecepatan:',v,'m/s')
    print('waktu:',t,'s')

    print('Jarak:',S,'m')
