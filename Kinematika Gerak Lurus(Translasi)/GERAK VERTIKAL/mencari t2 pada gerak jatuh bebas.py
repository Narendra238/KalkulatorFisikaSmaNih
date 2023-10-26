print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari waktu kuadrat Gerak Jatuh Bebas (t^2)')
gravitasi = input('gravitasi (m/s^2):')
ketinggian= input('tinggi (m):')


try:
    g=float(gravitasi)
    h=float(ketinggian)
    
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    t2=2*h/g
    print('gravitasi:',g,'m/s^2')
    print('Ketinggian:',h,'m')
    

    print('Waktu Kuadrat:',t2,'s^2')
