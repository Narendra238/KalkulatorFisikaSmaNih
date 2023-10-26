print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Kecepatan Akhir Gerak Vertikal Bawah (Vt)')
gravitasi = input('gravitasi (m/s^2):')
waktu= input('waktu (s):')
kecepatanawal=input('Kecepatan awal (m/s):')


try:
    g=float(gravitasi)
    t=float(waktu)
    Vo=float(kecepatanawal)
    
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    Vt=Vo+g*t
    print('gravitasi:',g,'m/s^2')
    print('waktu:',t,'s')
    print('kecepatan awal',Vo,'m/s')

    print('Kecepatan Akhir:',Vt,'m/s')
