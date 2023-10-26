print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Kecepatan Akhir Kuadrat dari GLBB (Vt^2)')
percepatan = input('percepatan (m/s^2):')
jarak = input('jarak (m):')
kecepatanawal= input('kecepatan awal (m/s):')


try:
    a=float(percepatan)
    S=float(jarak)
    Vo=float(kecepatanawal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    Vt2=Vo**2+2*a*S
    print('percepatan:',a,'m/s^2')
    print('Jarak:',S,'m')
    print('kecepatan awal:',Vo,'m/s')

    print('Kecepatan Akhir Kuadrat (Vt^2):',Vt2,'m/s')
