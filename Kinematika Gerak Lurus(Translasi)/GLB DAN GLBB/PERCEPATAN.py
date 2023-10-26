print("Kalkulator FISIKA GLB & GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB
print('Mencari Percepatan')
kecepatanawal= input('Vo (m/s):')
kecepatanakhir = input('Vt (m/s):')
waktuawal = input('t0 (s):')
waktuakhir = input('t1 (s):')

try:
    Vo=float(kecepatanawal)
    Vt=float (kecepatanakhir)
    t0=float(waktuawal)
    t1=float(waktuakhir)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    a= (Vt-Vo)/(t1-t0)
    print('kecepatan awal:',Vo,'m/s')
    print('kecepatan akhir:',Vt,'m/s')
    print('waktu awal:' ,t0,'s')
    print('waktu akhir',t1,'s')

    print('Percepatan:', a,'m/s^2')
