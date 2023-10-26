print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Kecepatan Akhir Kuadrat pada sumbu y (Vt^2)')
percepatan = input('gravitasi (m/s^2):')
jarak = input('jarak(Y) (m):')
kecepatanawal= input('kecepatan awal pada titik y(m/s):')


try:
    a=float(percepatan)
    S=float(jarak)
    Vo=float(kecepatanawal)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    Vt2=Vo**2+2*a*S
    print('gravitasi:',a,'m/s^2')
    print('Jarak (Y):',S,'m')
    print('kecepatan awal pada titik y:',Vo,'m/s')

    print('Kecepatan Akhir Kuadrat (Vt^2):',Vt2,'m/s')
