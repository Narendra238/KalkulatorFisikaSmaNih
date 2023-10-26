print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Ketinggian Gerak Jatuh Bebas(h)')
gravitasi = input('gravitasi (m/s^2):')
waktu= input('waktu (s):')


try:
    g=float(gravitasi)
    t=float(waktu)
    
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    h=(1/2)*g*t**2
    print('gravitasi:',g,'m/s^2')
    print('waktu:',h,'s')
    

    print('Ketinggian:',h,'m')
