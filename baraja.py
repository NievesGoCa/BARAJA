
def crear_baraja(n,p):
    numero = n
    palo = p
    baraja = []

    for p in palo:
        for n in numero:
            baraja.append(p+n)

    return baraja

  
