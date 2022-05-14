print("lista zakupów".capitalize())
lista = {
    "piekarnia".capitalize(): ["chleb".capitalize(), "bułki".capitalize(), "pączek".capitalize()],
    "warzywniak".capitalize(): ["marchew".capitalize(), "seler".capitalize(), "rukola".capitalize()],
}
for sklep, rzeczy in lista.items():
    print("idę do %s i kupuję tam: %s".capitalize() % (sklep, rzeczy))
   
lista1 = lista ["Piekarnia"]
lista2 = lista ["Warzywniak"]
print(f"w sumie kupuję {len(lista1) + len(lista2)} produktów".capitalize())

print("hello, dawno mnie tu nie było")
print("muszę szybko nadrobić zaległości")
