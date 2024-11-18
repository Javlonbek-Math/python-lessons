#Amaliyot 18/11/2024
#Funksiya
def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
tyil = int(input("Tug'ilgan yilingizni kiriting: "))
yosh_hisobla(tyil)
def yosh_hisobla(tugilgan_yil, joriy_yil=2024):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

yosh_hisobla(1993)
def t_yil_ber(joriy_yil=2024):
    """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    ism=input("Isminggizni kiriting: ")
    yosh=int(input("Yoshiggizni kiriting: "))
    print(f" {ism}, siz {joriy_yil-yosh} da tug'ilgansiz! ")
t_yil_ber()
def kvadratini_hisobla(son):
    print(f"{son}ning kvadrati {son**2} ga teng")
kvadratini_hisobla(5)
def son_turi(son1,son2=2):
    """ Sonning darajaga ko'tarish """
    print(f"{son1**(son2)}")
son_turi(3)
def qoldiq_tekshir(x):
    for i in range(2,11):
      if not x%i:
          print(f"{x} {i} ga qoldiqsiz bo'linadi")
qoldiq_tekshir(70)

    



