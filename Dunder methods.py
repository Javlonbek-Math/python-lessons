22/12/2024
# Amaliyot
# Dunder methods
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
    def __init__(self, ism, familiya, passport, tyil,idraqam,bosqich):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = bosqich
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
    def __repr__(self):
        return f"Samdu talabasi {self.ism} {self.familiya}"
    def __lt__(self,y):
        return self.bosqich<y.bosqich
class Fan:
    def __init__(self,name):
        self.name=name
        self.fanga_azolar=[]
    def add_student(self,*students):
     for student in students:
          if isinstance(student, Talaba):
                self.fanga_azolar.append(student)
    def __getitem__(self,index):
        return self.fanga_azolar[index]
    def __len__(self):
        return len(self.fanga_azolar)    
    def __add__(self,student):
            if isinstance(student,Talaba):
                self.add_student(student)
            return self

            
              
    
    def __repr__(self):
     result=f"Fan: {self.name}\nTalabalar:\n"   
     for x in self.fanga_azolar:
         result += f"  - {x}\n"
     return result
    def __sub__(self,student):
        if isinstance(student,Talaba):
            student_id=student.get_id()
            student_passport=student.passport
            for x in self.fanga_azolar:
                x.get_id()==student_id or x.passport==student_passport
                self.fanga_azolar.remove(x)
                return f"{x.ism} {x.familiya} removed from {self.name}"
    def __call__(self):
        return [x for x in self.fanga_azolar]
    def __call__(self,*students):
        if students:
            for student in students:
                self.add_student(student)
            else:
                return [student for student in self.fanga_azolar]
            
        
           
     
talaba1 = Talaba("Valijon","Aliyev","FA112299",2000,1,"0000012")
talaba2=Talaba('Komil','Berdiyev','FA2312312',2002,2,'0000013')
talaba3=Talaba('Asilbek','Ahadaov','FA2125332',2001,3,'0000014')
talaba4=Talaba('Bekmurod','Erkinov','FA2125345',2005,2,'0000015')
talaba5=Talaba('Ali','Boqiyev','FA2125356',2001,1,'0000016')
talaba6=Talaba('Karim','Ochilov','FA2125366',2001,4,'0000017')
matem=Fan('Matematika')
fizika=Fan('Fizika')
tarix=Fan('Tarix')
matem.add_student(talaba1,talaba2)
fizika.add_student(talaba3,talaba4)
tarix.add_student(talaba5,talaba6)
matem=matem+talaba3
result=matem-talaba1






