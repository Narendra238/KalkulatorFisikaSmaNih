print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#GHS (GERAK HARMONIK SEDERHANA ATAU OSILASI)
print('Mencari Energi potensial pada GHS')

ket=input('Ketetapan Pegas (N/m):')
sim=input('Simpangan (m):')



try:
    y=float(sim)
    k=float(ket)

except:
    print('INPUT BUKAN MERUPAKAN BILANGAN/ANGKA! ')
else:
    n=(1/2)*k*y**2
    
    print('Simpangan(y) :',y,'m')
    print('Ketetapan Pegas:',k,'N/m')

    print('ENERGI POTENSIAL:',n,'Joule')
