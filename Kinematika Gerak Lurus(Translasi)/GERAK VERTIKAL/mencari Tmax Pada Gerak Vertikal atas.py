
print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Waktu Maksimum Gerak Vertikal Atas (tmax)')
gravitasi = input('gravitasi (m/s^2):')
kecepatanawal=input('Kecepatan awal (m/s):')


try:
    g=float(gravitasi)
    Vo=float(kecepatanawal)
    
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    t=Vo/g
    print('gravitasi:',g,'m/s^2')
    print('kecepatan awal',Vo,'m/s')

    print('Waktu Maksimum:',t,'s')
