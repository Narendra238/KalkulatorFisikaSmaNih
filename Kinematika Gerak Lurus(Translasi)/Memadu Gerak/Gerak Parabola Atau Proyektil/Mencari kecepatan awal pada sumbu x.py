print("Kalkulator FISIKA GLBB")
print("MUHAMMAD NARENDRA HAWARI")

#GLBB

print('Mencari Kecepatan awal sumbu x (Vt)')

kecepatan_awal= input('kecepatan awal pada sumbu y (m/s):')
print('Masukan Nilai Cos saja , misal 1,0.5 dsb')
cos = input ('Nilai Cos : ')

try:
    Vo=float(kecepatan_awal)
    c=float (cos)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    V=Vo*c
    print('kecepatan awal (Vo):',Vo,'m/s')
    print('Nilai Cos :',c,)
    

    print('Kecepatan awal sumbu x (Vt):',V,'m/s')

