print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Kecepatan Akhir kuadrat Gerak Jatuh Bebas (Vt^2)')
gravitasi = input('gravitasi (m/s^2):')
ketinggian= input('tinggi (m):')


try:
    g=float(gravitasi)
    h=float(ketinggian)
    
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    Vt2=2*g*h
    print('gravitasi:',g,'m/s^2')
    print('Ketinggian:',h,'s')
    

    print('Kecepatan Akhir Kuadrat:',Vt2,'m/s')
