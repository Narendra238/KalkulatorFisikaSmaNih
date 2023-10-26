print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Ketinggian Maximum Gerak Vertikal Atas (hmax)')
gravitasi = input('gravitasi (m/s^2):')
kecepatanawal=input('Kecepatan awal (m/s):')


try:
    g=float(gravitasi)
    Vo=float(kecepatanawal)
    
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    h=(Vo**2)/(2*g)
    print('gravitasi:',g,'m/s^2')
    print('kecepatan awal',Vo,'m/s')

    print('Ketinggian maximum:',h,'m')
