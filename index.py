class car:
 
    def __init__(self, znacka: str, rok: int, model: str, barva: str, typ_prevodovky: str, cena: float,):
        self.znacka = znacka
        self.rok = rok
        self.model = model
        self.barva = barva
        self.typ_prevodovky = typ_prevodovky
        self.cena = cena
 
    def vypis(self):
        return f"Název auta: {self.znacka}, Rok výroby: {self.rok}"
 
audi = car("Audi", 1999, "A4", "Stříbrná", "Manuáln", 45000)
skoda = car("Škoda", 2014, "Superb", "Bílá", "Manuální", 3100000)
 
print(audi.cena)
print(skoda.model)
print(audi.vypis())