Amaliyot 04/12/2024
*args and **kwargs
def mult(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma=son*kopaytma
    return kopaytma
print(mult(2,3,4))
def talabalar(ism,fam,**malumot):
    malumot['ismi']=ism
    malumot['familya']=fam
    return malumot
print(talabalar('ali','valiev', t_yili=2002))
        

