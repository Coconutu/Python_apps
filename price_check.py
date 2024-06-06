def magazin_pret_minim(produs):
    pret_minim=9999
    magazin_ieftin='Nu e setat'
    fp = open('preturi.txt', 'r')
    continut = fp.read()
    fp.close()
    lista_continut=continut.split('\n')
    for i in lista_continut:
        j=i.split('-')
        if j[0]==produs:
            if pret_minim>float(j[2]):
                pret_minim=float(j[2])
                magazin_ieftin=j[1]
        raspuns=produs+'->'+magazin_ieftin

    return raspuns
print(magazin_pret_minim('Lapte_1.8L'))



