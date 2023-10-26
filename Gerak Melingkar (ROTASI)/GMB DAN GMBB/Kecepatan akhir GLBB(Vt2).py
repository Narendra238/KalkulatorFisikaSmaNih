print("Kalkulator FISIKA")
print("MUHAMMAD NARENDRA HAWARI")

#ROTASI

print('Mencari Kecepatan Sudut Akhir Kuadrat (Vt^2)')
percepatan = input('percepatan sudut (m/s^2):')
jarak = input('sudut tempuh (m):')
kecepatanawal= input('kecepatan sudut awal (m/s):')


try:
    a=float(percepatan)
    S=float(jarak)
    Vo=float(kecepatanawal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    Vt2=Vo**2+2*a*S
    print('percepatan:',a,'m/s^2')
    print('sudut tempuh:',S,'m')
    print('kecepatan sudut awal:',Vo,'m/s')

    print('Kecepatan Akhir Kuadrat (Vt^2):',Vt2,'m/s')
