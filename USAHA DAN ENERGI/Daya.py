print('Kalkulator Sederhana Fisika')
print('MUHAMMAD NARENDRA HAWARI')

#USAHA DAN ENERGI
print('Mencari Daya (P) watt')

usaha=input('Usaha yang diberikan (joule):')
waktu=input('Waktu yang berlangsung (s): ')

try:
    w=float(usaha)
    t=float(waktu)
except:
    print('INPUT BUKAN MERUPAKAN BILANGAN/ANGKA')
else:
    p=w/t
    print('Usaha yang diberikan:',w,'joule')
    print('Waktu yang berlangsung:',t,'s')

    print('Daya :',p,'Joule/s atau watt')
