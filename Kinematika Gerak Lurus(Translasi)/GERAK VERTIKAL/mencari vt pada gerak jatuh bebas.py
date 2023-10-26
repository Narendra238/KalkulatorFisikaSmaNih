print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Kecepatan Akhir Gerak Jatuh Bebas (Vt)')
gravitasi = input('gravitasi (m/s^2):')
waktu= input('waktu (s):')



try:
    g=float(gravitasi)
    t=float(waktu)

except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    Vt=g*t
    print('gravitasi:',g,'m/s^2')
    print('waktu:',t,'s')

    print('Kecepatan Akhir:',Vt,'m/s')
