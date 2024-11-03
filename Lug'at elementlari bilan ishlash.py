02/11/2024
Lu'gat elementlari bilan ishlash
lugat={'Boolean':'Mantiqiy qiymat', 'Float':"O'nlik son", 'Integer': 'Butun son', 'For':'Biror amalni qayta bajarish sikli'}
for k,q in sorted(lugat.items()):
    print(f"{k}-{q}")
davlatlar = {
    "o'zbekiston":'toshkent',
    'aqsh':'washington d.c.',
    'rossiya':'moskva',
    'tojikiston':'dushanbe',
    "qirg'iziston":'bishkek',
    'qozog\'iston':'nursulton',
    'malayziya':'kuala-lumpur',
    'singapur':'singapur',
    'italiya':'rim'}
country=input("Bilmoqchi_bolgan_davlatinngizni_kiriting: ").lower()
for capital in davlatlar.get(country):
    if capital==None:
        print(f"kechirasiz bizda bunday {country} haqida ma'lumot yo'q")
    else: print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
for a in sorted(davlatlar):
    print(a.upper())
for b in sorted(davlatlar.values()):
    print(b.upper())
menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }

print('3 ta taom buyurtma bering.')
taom=[]
for n in range(3):
    taom.append(input(f"{n+1}-taominggizni kiritng: "))
    print(f"{n+1}-taom: {taom[n]}\n")
for x in taom:
    if x in menu:
        print(f"{x} {menu[x]} so'm ")
    else: print(f"kechirasiz bizda {x} yo'q")
for x in taom:
    if x not in menu:
       print(f"bizda {x} yo'q")
ciao=menu.get('osh')
print(ciao)

    


    
    