Amaliyot 26/11/2024
Qiymat qaytaruvchi funksiya
def oraliq(min,max,qadam=''):
    sonlar=[]
    while min<max:
        sonlar.append(min)
        if qadam:
            min+=qadam
        else:
            min+=1
    return sonlar
print(oraliq(1,10))
def foydalanuvchi(ism,familiya,yoshi,t_yil,t_joy,t_raqam=None,email=''):
    shaxs={'ismi':ism, 
            'familiya':familiya, 
            'yoshi':yoshi,
            't_yil':t_yil,
            't_joy':t_joy,
            't_raqam':t_raqam,
            'email':email}
    return shaxs
mijozlar=[]
while True:
    ism = input("Ismi: ")
    yoshi=input("Yoshi: ")
    familiya = input("Familiyasi: ")
    t_yil = int(input("Tug'ilgan yili: "))
    t_joy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    t_raqam = input("Telefon raqami: ")
    mijozlar.append(foydalanuvchi(ism, familiya, yoshi, t_yil, t_joy))
    javob=input("Davom etasizmi? (yes/no): ")
    if javob=='no':
        break
print(mijozlar)
def kattasini_top(a,b,c):
    if a>b and a>c:
        katta=a
    elif b>a and b>c:
        katta=b
    else: katta=c
    return katta
print(kattasini_top(5, 6, 7))
def kattasini_top(a,b,c):
    while True:
        if a>b and a>c:
                katta=a
        elif b>a and b>c:
                katta=b
        else: katta=c
        return katta
        javob=input("Davom etasizmi? (yes/no): ")
        if javob=='no':
            break
print(kattasini_top(5,3,8))
r=int(input("Radius: "))
def aylana_top(r):
   
    d=2*r
    p=4*r
    s=r**2
    aylana={'Radius':r,
            'Diametr':d,
            'Perimetr':p,
            'Yuzi':s}
    return aylana
print(aylana_top(r))
r = int(input("Radius: "))

def aylana_top(r):
    d = 2 * r
    p = 2 * 3.14 * r  # Corrected to calculate the perimeter (circumference)
    s = r ** 2  # Corrected exponentiation operator
    aylana = {
        'Radius': r,
        'Diametr': d,
        'Perimetr': p,
        'Yuzi': s
    }
    return aylana

print(aylana_top(r))
def oraliq(min,max):
    tub_sonlar=[]
    """Berilgan oraliqdagi tub sonlarni topuvchi funksiya"""
    for n in range(min,max+1):
        tub = True
        if n==1:
            tub = False
        elif n==2:
            tub=True
        else:
            for x in range(2,n):
                if n%x==0:
                    tub=False
        if tub:
            tub_sonlar.append(n)
    return tub_sonlar
print(oraliq(5, 20))

def Fibonachchi():
    son=int(input('Son kiriting: '))
    sonlar=[0,1]
    for x in range(2,son+1):
        yangi_son=sonlar[x-1]+sonlar[x-2]
        sonlar.append(yangi_son)
    return sonlar
print(Fibonachchi())
def Fibonacci(n):
  
    sonlar = []  
    
    for x in range(n):
        if x==1 or x==0:
          sonlar.append(1)
        else: 

          yangi_son = sonlar[x - 1] + sonlar[x - 2]  
          sonlar.append(yangi_son)
    
    return sonlar

print(Fibonacci(10)) 




    
            
    
    
    




               

        
        

