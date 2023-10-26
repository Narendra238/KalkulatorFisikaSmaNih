print("Kalkulator FISIKA")
print("MUHAMMAD NARENDRA HAWARI")

#ROTASI

print('Mencari Kecepatan sudut akhir(Vt)')
percepatan = input('percepatan sudut (m/s^2):')
waktu = input('waktu (s):')
kecepatan_awal= input('kecepatan sudut awal (rad/s):')


try:
    a=float(percepatan)
    t=float(waktu)
    Vo=float(kecepatan_awal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    Vt=Vo+a*t
    print('percepatan sudut:',a,'m/s^2')
    print('waktu:',t,'s')
    print('kecepatan awal:',Vo,'rad/s')

    print('Kecepatan sudut akhir:',Vt,'m/s')

