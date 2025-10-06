class car:
    def __init__(self, znacka: str, rok: int, model: str, barva: str, typ_prevodovky: str, cena: float):
        self.znacka = znacka
        self.rok = rok
        self.model = model
        self.barva = barva
        self.typ_prevodovky = typ_prevodovky
        self.cena = cena
 
    def cena_bez_dph(self):
        return f"{self.cena * 0.79:.2f} kč"
 
    def vypis(self):
        return (
            f"Název auta: {self.znacka} \n"
            f"Rok výroby: {self.rok} \n"
            f"Model: {self.model} \n"
            f"Barva: {self.barva} \n"
            f"Typ převodovky: {self.typ_prevodovky} \n"
            f"Cena včetně DPH: {self.cena} Kč, \n"
            f"Cena bez DPH: {self.cena_bez_dph()}"
        )
 
    def priplatkova_vybava(self, vybava: str, cena_vybavy: float):
        return (
            f"Připlatková výbava: {vybava}, cena příplatkové výbavy je: {cena_vybavy} Kč, "
            f"celková cena auta s příplatkovou výbavou je: {self.cena + cena_vybavy} Kč"
        )
 
audi = car("Audi", 2001, "A4", "Stříbrná", "Manuální", 45000)
skoda = car("Škoda", 2014, "Superb II", "Bílá", "Manuální", 3100000)
 
seznam_aut = [
    car("Mercedes", 2020, "A4", "stříbrná", "Manuální", 45000),
    car("McLaren", 2014, "Superb II", "Bílá", "Manuální", 310000),
    car("BMW", 2022, "X5", "Černá", "Automatická", 1500000),
    car("Fiat", 2020, "500", "Červená", "Automatická", 350000),
    car("Lamborghini", 2021, "Aventador", "Zelená", "Automatická", 10000000),
    car("Porsche", 2019, "911", "Modrá", "Automatická", 2500000),
    car("Nissan", 2018, "Juke", "Žlutá", "Manuální", 450000),
    car("Ford", 2020, "Focus", "Stříbrná", "Automatická", 550000),
    car("Opel", 2017, "Astra", "Šedá", "Manuální", 300000),
    car("Mazda", 2021, "CX-5", "Zlatá", "Automatická", 850000),
    car("Renault", 2019, "Clio", "Bílá", "Manuální", 400000)
]
 
 
 
#vypis vsech aut
for auto in seznam_aut:
    print(auto.vypis())
    print("-------------------------")
 
#vypis jednoho auta
print(seznam_aut[0].znacka)          
 
print(audi.rok)                      
print(skoda.model)                  
print(audi.vypis())                  
print(f"Cena auta bez DPH je: {audi.cena_bez_dph()}")
print(skoda.priplatkova_vybava("metalíza", 15000))