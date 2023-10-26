print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Kecepatan akhir pada arah sumbu y(Vt)')
percepatan = input('gravitasi (m/s^2):')
waktu = input('waktu (s):')
kecepatan_awal= input('kecepatan awal pada sumbu y (m/s):')


try:
    a=float(percepatan)
    t=float(waktu)
    Vo=float(kecepatan_awal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    Vt=Vo+a*t
    print('kecepatan awal pada sumbu y:',Vo,'m/s')
    print('gravitasi:',a,'m/s^2')
    print('waktu:',t,'s')
    

    print('Kecepatan akhir pada sumbu y:',Vt,'m/s')

