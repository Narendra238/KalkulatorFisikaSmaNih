print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Jarak Max (Xm)')
percepatan = input('gravitasi (m/s^2):')
print('Masukan Nilai Sin seperti , 0,0.5,1 dsb')
sin= input('Nilai 2 x Sin : ')
kecepatanawal= input('kecepatan awal (m/s):')


try:
    a=float(percepatan)
    s=float(sin)
    Vo=float(kecepatanawal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    x=Vo**2*s/a
    print('gravitasi:',a,'m/s^2')
    print('Nilai sin :')
    print('kecepatan awal :',Vo,'m/s')

    print('Jarak Max(Xm):',x,'s')
