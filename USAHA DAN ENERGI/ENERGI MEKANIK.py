print('Kalkulator Sederhana Fisika')
print("MUHAMMAD NARENDRA HAWARI")

#ENERGI MEKANIK
print("MENCARI ENERGI MEKANIK")

kinetik=input('Energi kinetik (joule):')
potensial=input('Energi potensial (joule):')

try:
    EK=float(kinetik)
    EP=float(potensial)
except:
    print('Masukan bukan angka atau bilangan!')
else:
    EM=EP+EK
    print('Energi kinetik (joule):',EK,'joule')
    print('Energi potensial (joule):',EP,'joule')

    print('Energi Mekanik:',EM,'Joule atau Kgm^2s^2')
