print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#GHS (GERAK HARMONIK SEDERHANA ATAU OSILASI)
print('Mencari Energi KInetik pada GHS')

ket=input('Ketetapan Pegas (N/m):')
sim=input('Simpangan (m):')
amp=input('Amplitudo(m):')


try:
    y=float(sim)
    k=float(ket)
    a=float(amp)

except:
    print('INPUT BUKAN MERUPAKAN BILANGAN/ANGKA! ')
else:
    n=(1/2)*k*(a**2-y**2)
    
    print('Simpangan(y) :',y,'m')
    print('Ketetapan Pegas:',k,'N/m')
    print('Amplitudo(A)',a,'m')
    

    print('ENERGI KINETIK:',n,'Joule')
