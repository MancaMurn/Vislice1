import model

def izpis_igre(igra):
    return (
        "=============================================================\n" + 
        f"Pazi! Če narediš še {model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1} napak, boš izgubil! \n " +
        f"Pravilni del gesla: {igra.pravilni_del_gesla()} \n " + 
        f"Neuspeli poskusi: {igra.nepravilni_ugibi()} \n" +
        "=============================================================" 
    )

def izpis_zmage(igra):
    return f"Čestitam! Uganil si pravilno besedo {igra.geslo}"

def izpis_poraza(igra):
    return f"Kakšna Škoda, napravil si že preveč napak. Igro si izgubil. Pravilna beseda je bila {igra.geslo}"

def zahtevaj_vnos():
    return input('Črka: ')

def pozeni_vmesnik():
    igra = model.nova_igra()
    while True:
        print(izpis_igre(igra))
        crka = zahtevaj_vnos()
        stanje = igra.ugibaj(crka)
        if stanje == model.ZMAGA:
            print(izpis_zmage(igra))
            break
        elif stanje == model.PORAZ:
            print(izpis_poraza(igra))
            break


