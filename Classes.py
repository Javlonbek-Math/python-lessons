#Amaliyot 13/12/2024
#class



class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")
#     def __init__(self,ism,familiya,tyil):
#         """Talabaning xususiyatlari"""
#         self.name = ism
#         self.surname = familiya
#         self.birthyear = tyil
# talaba1 = Talaba("Alijon","Valiyev",2000)
talaba2 = Talaba("Olim","Olimov",1995)
talaba3 = Talaba("Husan","Akbarov",2004)
talaba4 = Talaba("Hasan","Akbarov",2004)
talaba2.tanishtir()
class User:
    def __init__(self,ism,foydalanuvchi_ismi,email):
        self.name=ism
        self.username=foydalanuvchi_ismi
        self.email=email
    def get_info(self):
        return f"(Foydalanuvchi: {self.username}, ismi: {self.name}, email: {self.email})"
foydalanuvchi1=User('Azimjon','Azimchik001','Azimjon20@gmail.com')
print(foydalanuvchi1.get_info())



