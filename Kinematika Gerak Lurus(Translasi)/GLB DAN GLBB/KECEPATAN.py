print("Kalkulator FISIKA GLB")
print("MUHAMMAD NARENDRA HAWARI")

#GLB

print('Mencari Kecepatan(m/s)')
jarak = input('jarak (m):')
waktu = input('waktu (s):')


try:
    S=float(jarak)
    t=float(waktu)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    v=S/t
    print('jarak:',S,'m')
    print('waktu:',t,'s')

    print('Kecepatan:',v,'m/s')
