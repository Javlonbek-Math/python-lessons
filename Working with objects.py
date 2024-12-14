14/12/2024
# Amaliyot
# Objects
class Avto:
    def __init__(self,model,rang,korobka,narh):
        self.model=model
        self.rang=rang
        self.korobka=korobka
        self.narh=narh
        self.km=0
    def get_info(self):
        return f"{self.rang} {self.korobka} {self.model} yurgan kilometri : {self.km}, narhi: {self.narh}"
    def update_model(self,new_km):
        """Avtomobilning yurgan kmini yangilash"""
        self.km=new_km
        
        
avto1=Avto('chevrolet malibu','oq','avtomat',25000)
avto2=Avto('chevrolet nexia','qora','mexanika',35000)
avto3=Avto('chevrolet onix','qizil','mexanika',45000)
avto4=Avto('chevrolet captiva','yashil','avtomat',55000)

print(avto1.update_model(10000))
print(avto1.get_info())
class Avtosalon:
    def __init__(self,salon_nomi,manzili):
        self.salon_nomi=salon_nomi
        self.manzili=manzili
        self.sotuvdagi_avtomobillar=[]
        self.avtomobillar_soni=0
    def add_avto(self,avto):
        self.sotuvdagi_avtomobillar.append(avto)
        self.avtomobillar_soni+=1
    def get_salon(self):
        return self.salon_nomi
    def s_avtolar(self):
        return [avto.get_info() for avto in self.sotuvdagi_avtomobillar]
    

        
sam=Avtosalon("Samarkand GM",'Samarkand')
tosh=Avtosalon("Tashkent GM",'Tashkent')
sam.add_avto(avto1)
sam.add_avto(avto2)
sam.add_avto(avto3)
sam.add_avto(avto4)
tosh.add_avto(avto1)
tosh.add_avto(avto2)
tosh.add_avto(avto3)
tosh.add_avto(avto4)


def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False ]
print(see_methods(Avto))








