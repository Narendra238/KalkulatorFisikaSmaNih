print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Kecepatan akhir(Vt)')
percepatan = input('percepatan (m/s^2):')
waktu = input('waktu (s):')
kecepatan_awal= input('kecepatan awal (m/s):')


try:
    a=float(percepatan)
    t=float(waktu)
    Vo=float(kecepatan_awal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    Vt=Vo+a*t
    print('percepatan:',a,'m/s^2')
    print('waktu:',t,'s')
    print('kecepatan awal:',Vo,'m/s')

    print('Kecepatan akhir:',Vt,'m/s')

