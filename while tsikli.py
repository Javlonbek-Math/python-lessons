# Amaliyot 15/11/2024
# While tsikli
ism = input("Ismingiz nima? ")
savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
yosh = input(savol)
kasb = input(f"Yoshinggiz {yosh}da ekan xursandman, kasbinggiz nima?")
print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)
son = 0
while son<10:    
    if son%2!=0:
        continue
    else:
        print(son)
    son += 1
savol='Sevimli kitobinggizni kiriting: '
qiymat=''
while True:
    qiymat=input(savol)
    if qiymat == 'stop':
        break
    else: print(qiymat)
savol='Sevimli kitobinggizni kiriting: '
qiymat=''
while qiymat !='stop':
    qiymat=input(savol)
    if qiymat !='stop':
        print(qiymat)
savol='Sevimli kitobinggizni kiriting: '
ishora=True
while ishora:
    qiymat=input(savol)
    if qiymat == 'stop':
        ishora=False
    else: print(qiymat)
savol='Yoshinggizni kiriting: '
qiymat=''
ishora=True
while ishora:
    qiymat=input(savol)
    if qiymat == ('exit') or qiymat== ('quit'):
        ishora=False
    else: 
        yosh=int(qiymat)
      
        if yosh==7:
          print("Sizga 2000 ming so'm")
        elif yosh>7 and yosh<=18:
          print("Sizga 3000 ming so'm")
        elif yosh>18 and yosh<=65:
          print("Sizga 10000 ming so'm")
        elif yosh>65: print('Sizga bepul')
savol='Yoshinggizni kiriting: '
qiymat=''
while True:
    qiymat=input(savol)
    if qiymat == ('exit') or qiymat== ('quit'):
        break
    else: 
        yosh=int(qiymat)
      
        if yosh==7:
          print("Sizga 2000 ming so'm")
        elif yosh>7 and yosh<=18:
          print("Sizga 3000 ming so'm")
        elif yosh>18 and yosh<=65:
          print("Sizga 10000 ming so'm")
        elif yosh>65: print('Sizga bepul')
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
qiymat=''
while True:
    qiymat = input(savol)
    if qiymat=='Exit':
        break
    elif int(qiymat)<0:
        continue
    elif qiymat=='Exit':
        break
    else: 
        ildiz=float(qiymat)
        ildiz = float((qiymat))**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
    
    
    
    

    

