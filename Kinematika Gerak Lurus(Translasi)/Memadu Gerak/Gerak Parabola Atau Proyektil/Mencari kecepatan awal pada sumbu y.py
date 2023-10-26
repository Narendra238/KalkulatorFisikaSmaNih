print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Kecepatan awal sumbu y (Vt)')

kecepatan_awal= input('kecepatan awal pada sumbu y (m/s):')
print('Masukan Nilai Sin saja , misal 1,0.5 dsb')
sin = input ('Nilai Sin : ')

try:
    Vo=float(kecepatan_awal)
    c=float (sin)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    V=Vo*c
    print('kecepatan awal (Vo):',Vo,'m/s')
    print('Nilai Sin :',c,)
    

    print('Kecepatan awal sumbu y (Vt):',V,'m/s')

