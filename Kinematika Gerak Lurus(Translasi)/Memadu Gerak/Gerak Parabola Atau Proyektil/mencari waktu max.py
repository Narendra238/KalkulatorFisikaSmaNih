print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Waktu Max')
percepatan = input('gravitasi (m/s^2):')
sin= input('Nilai Sin : ')
kecepatanawal= input('kecepatan awal (m/s):')


try:
    a=float(percepatan)
    s=float(sin)
    Vo=float(kecepatanawal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    t=2*Vo*s/a
    print('gravitasi:',a,'m/s^2')
    print('Nilai sin :')
    print('kecepatan awal :',Vo,'m/s')

    print('Waktu Max(Tm):',t,'s')
