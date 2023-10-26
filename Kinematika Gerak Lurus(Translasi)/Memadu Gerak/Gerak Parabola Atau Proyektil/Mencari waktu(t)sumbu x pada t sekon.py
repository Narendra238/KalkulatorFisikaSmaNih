print("Kalkulator FISIKA GLB")
print("MUHAMMAD NARENDRA HAWARI")

#GLB

print('Mencari waktu(t)sumbu x pada t sekon')
kecepatan = input('kecepatan (m/s):')
jarak = input('jarak (m):')


try:
    v=float(kecepatan)
    S=float(jarak)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    t=v/S
    print('kecepatan:',v,'m/s')
    print('jarak:',S,'m')

    print('Waktu pada sumbu x:',t,'s')
