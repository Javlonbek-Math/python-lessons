from datetime import datetime as dt,timedelta
import re
today=dt.today()
bugun_date=today.date()
n=0
while n<10:
    print(bugun_date.strftime("%d/%m/%Y"))
    bugun_date+=timedelta(weeks=2)
    n+=1
def hisobla(yil,oy,kun):
  today=dt.today()
  yil=int(yil)
  oy=int(oy)
  kun=int(kun)
ramazon=dt(2025,2,20)
left_day=ramazon-today
left_day=int(left_day.days)
print(f"Ramazonga {left_day} kun qoldi")

  tugilgan_date=dt(yil,oy,kun)
  farq_kun=(today-tugilgan_date).days
  farq_oy=farq_kun//30
  farq_yil=farq_oy//12
  print(f"Tug'ilgan kuniggizga shuncha {farq_kun} kun bo'libdi")
  print(f"Tug'ilgan kuniggizga shuncha {farq_oy} oy bo'libdi")
  print(f"Tug'ilgan kuniggizga shuncha {farq_yil} yil bo'libdi")

hisobla(2002,7,24)

msg="Telefon raqaminggizni kiriting: "
andoza='^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
while True:
    t_raqam=input(msg)
    if re.match(andoza,t_raqam):
        print('Telefon raqam muvaffaqiyatli kiritildi')
        break
    else: print('Telefon raqam talabga javob bermadi')

matn="Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI"

matn+=" Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"

andoza=r'https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'
saytlar=re.findall(andoza,matn)
print(saytlar)

