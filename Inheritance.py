15/12/2024
# Amaliyot
# Vorislik va Polimorfizm
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism,familiya,passport,tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.shaxslar=[]
    def add_shaxs(self,shaxs):
        self.shaxslar.append(shaxs)
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-yilda tug`ilgan"
        return info
        
    def get_age(self,yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.fanlar=[]
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    def fanga_yozil(self,nomi):
        self.fanlar.append(nomi)
        return self.fanlar
    def get_info(self):
        fanlar_str=[]
        for x in self.get_fanlar():
            fanlar_str.append(x)
        return f"{self.ism} quyidagi fanlarda o'qiydi: {fanlar_str}"
    def remove_fan(self,del_fan):
        """Biror fanni o'chirib tashlash"""
        self.del_fan=del_fan
        for fan in self.fanlar:
            if del_fan==fan.nomi:
             self.fanlar.remove(fan)
             return (f"{del_fan} ro'yxatdan o'chirildi")
         
             
        return (f"Siz {del_fan}ga yozilmagansiz.")
        
        
    def get_fanlar(self):
        return [fan.nomi for fan in self.fanlar]
    def get_ism(self,user):
        self.user=user
        self.shaxslar.append(user)
        return self.shaxslar
class Fan:
    def __init__(self,nomi):
        self.nomi=nomi
kimyo=Fan('Kimyo')
matem=Fan('Oliy Matematika')  
fizika=Fan('Fizika') 
talaba1 = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")
talaba2=Talaba('Komil','Berdiyev','FA2312312',2002,'0000013')
talaba3=Talaba('Asilbek','Ahadaov','FA2125332',2001,'0000014')

talaba1.fanga_yozil(kimyo)
talaba1.fanga_yozil(fizika)
talaba2.fanga_yozil(matem)
talaba2.fanga_yozil(kimyo)
talaba3.fanga_yozil(kimyo)
talaba3.fanga_yozil(fizika)
class Foydalanuvchi(Shaxs):
    def __init__(self,ism,familiya,passport,tyil):        
        super().__init__(ism,familiya,passport,tyil)
    def yoshi(self,yil):
        self.yil=yil
        return yil-self.tyil
class Admin(Foydalanuvchi):
    def __init__(self,ism,familiya,passport,tyil):
        super().__init__(ism,familiya,passport,tyil)
        self.shaxslar=[]
    def ban_user(self,yil,max_age):
        banned_users=[]
        for shaxs in self.shaxslar:
            age=shaxs.get_age(yil)
            if age>max_age:
                banned_users.append(shaxs)
        if banned_users:
          for banned in banned_users:
             print(f"{banned.ism} banned (Age: {banned.get_age(yil)})!")
             self.shaxslar.remove(banned)
        else:
            print("No users were banned")
admin=Admin('Javlonbek','Shukurov','AA1234567',2002)
admin.add_shaxs(talaba1)
admin.add_shaxs(talaba2)
admin.add_shaxs(talaba3)
# print(admin.ban_user(2024, 22))
print(admin.yoshi(2024))

            

        
        
         
        




    

