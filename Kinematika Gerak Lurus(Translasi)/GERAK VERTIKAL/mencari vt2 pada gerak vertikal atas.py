print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Kecepatan Akhir Kuadrat Gerak Vertikal Atas (Vt^2)')
gravitasi = input('gravitasi (m/s^2):')
ketinggian = input('ketinggian (m):')
kecepatanawal= input('kecepatan awal (m/s):')


try:
    g=float(gravitasi)
    h=float(ketinggian)
    Vo=float(kecepatanawal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    Vt2=Vo**2-2*g*h
    print('gravitasi:',g,'m/s^2')
    print('ketinggian:',h,'m')
    print('kecepatan awal:',Vo,'m/s')

    print('Kecepatan Akhir Kuadrat (Vt^2):',Vt2,'m/s')
