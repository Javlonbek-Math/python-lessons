Amaliyot 04/14/2024
Funksiya va ro'yxat
def ismla(shaxslar):
    katta_harf=[]
    while shaxslar:
        shaxs=shaxslar.pop()
        katta_harf.append(shaxs.title())
    return katta_harf
ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf=ismla(ismlar[:])
print(katta_harf)
print(ismlar)


def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
    return matnlar


ismlar = ["ali", "vali", "hasan", "husan"]
yangi_ismlar=katta_harf(ismlar[:])
print(ismlar)
print(yangi_ismlar)
def bahola(ismlar):
    baholar = {}
    for i in range(len(ismlar)):
            ism=ismlar[i]
            baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
            baholar[ism]=baho
            
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)

