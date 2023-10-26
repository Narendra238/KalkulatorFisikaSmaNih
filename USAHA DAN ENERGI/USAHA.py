print("Kalkulator FISIKA USAHA&ENERGI")
print("MUHAMMAD NARENDRA HAWARI")

#W/Usaha adalah : W = (F*cosθ)*∆S

print('Usaha=(Gaya*cosθ)*perpindahan')
Gaya = input('Gaya(Newton):')

print('Contoh Cos 90°=0&Cos 60°= 0.5 Cos yang dituliskan cukup nilainya saja.')

cosθ = input('Nilai cosθ ():')
      
Perpindahan = input('perpindahan (m):')


try:
    F = float(Gaya)
    cosθ = float (cosθ)
    S = float (Perpindahan)

except:
    print('INPUT BUKAN MERUPAKAN BILANGAN !!!')
else:
    W = F*cosθ*S
    print('Gaya:' , F ,'Newton')
    print('cosθ:' ,cosθ , '°')
    print('perpindahan:' ,S ,'m')

    print('Usaha', W ,'Juole/kgm^2s^2')

    
