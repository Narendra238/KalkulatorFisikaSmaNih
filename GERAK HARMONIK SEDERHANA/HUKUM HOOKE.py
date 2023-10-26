print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#GHS (GERAK HARMONIK SEDERHANA ATAU OSILASI)
print('Mencari Hukum Hooke')

ket=input('Ketetapan Pegas (N/m):')
sim=input('Simpangan (m):')



try:
    y=float(sim)
    k=float(ket)

except:
    print('INPUT BUKAN MERUPAKAN BILANGAN/ANGKA! ')
else:
    n=(-k)*y
    print('Simpangan(y) :',y,'m')
    print('Ketetapan Pegas:',k,'N/m')

    print('Hukum Hooke:',n,'Newton')
