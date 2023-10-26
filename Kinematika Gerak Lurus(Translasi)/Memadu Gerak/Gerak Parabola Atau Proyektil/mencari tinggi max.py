print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Tinggi Max (Hm)')
percepatan = input('gravitasi (m/s^2):')
print('cukup masukan nilainya saja , misal 0.5,0,1 dsb')
sin= input('Nilai Sin : ')
kecepatanawal= input('kecepatan awal (m/s):')


try:
    a=float(percepatan)
    s=float(sin)
    Vo=float(kecepatanawal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    c=Vo**2*s**2
    t=c/(2*a)
    print('gravitasi:',a,'m/s^2')
    print('Nilai sin :',s,)
    print('kecepatan awal :',Vo,'m/s')

    print('Tinggi Max(Hm):',t ,'m')
