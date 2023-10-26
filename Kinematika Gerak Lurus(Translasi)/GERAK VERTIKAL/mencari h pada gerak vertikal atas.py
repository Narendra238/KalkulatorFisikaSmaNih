print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Ketinggian Gerak Vertikal Atas (h)')
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
   h=Vo*t-(1/2)*g*t**2
print('gravitasi:',g,'m/s^2')
print('waktu:',t,'s')
print('kecepatan awal',Vo,'m/s')

print('Ketinggian:',h,'m')
