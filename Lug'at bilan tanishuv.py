#Amaliyot 08/25/2024
otam={'Ismi':'Muhammad','t_yili':1976,'t_joyi':'Samarqand viloyati'}
#print(f"Otamning ismi {otam['Ismi']}, {otam['t_yili']}-yilda, {otam['t_joyi']}da tug'ilgan")
taomlar={'ali':'uzum','vali':'gilos','hasan':'olma','husan':'anor','olim':'shaftoli'}  
taom=taomlar['ali']
#print(f"Alining sevimli taomi {taom}")
python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}
#print(python_izohli_lugati['tuple'])
kalit=input("Sizga kerab bo'lgan  so'zni kiriting: ").lower()
#print(f"Ma'nosi {python_izohli_lugati[kalit]}" 
tarjima=python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else: print("ma'nosi",' ',tarjima)



  
  
  
  
  
  
  
  
  
  
  
  
  
  
  