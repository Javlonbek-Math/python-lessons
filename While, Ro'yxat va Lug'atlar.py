#Amaliyot 17/11/2024
#While,Lists and Dictionaries
buyurtmalar=[]
n=1
while True:
    savol=f"{n}-buyrtmanggizni kiriting: "
    maxsulot=input(savol)
    buyurtmalar.append(maxsulot)
    javob=input("Yana qo'shishni xohlaysizmi? (ha/yo'q)")
    if javob == "ha":
        n+=1
    else: break
print(buyurtmalar)

e_bozor={}
while True:
    maxsulot=input('Maxsulotinggizni kiriting: ')
    narxi= input(f"{maxsulot.title()}ning narxini kiriting: ")
    e_bozor[maxsulot]=narxi
    javob=input("Yana qo'shishni xohlaysizmi? (ha/yo'q)")
    if javob != "ha":
        break
print(e_bozor)

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}
while buyurtmalar:
    buyurtma=buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh=mahsulotlar[buyurtma]
        print(f"Bizda {buyurtma} {narh} so'm")
    else: print(f"bizda bu {buyurtma} mavjud emas")
            
    

    
    
    

