#Amaliyot 08/25/2024
python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat"}

# one way
kalit=input("So'zni kiriting:")
tarjima=python_izohli_lugati.get(kalit,'Bunday lugat mavjud emas')
#print(tarjima)
# second way
print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))




  
  
  
  
  
  
  
  
  
  
  
  
  
  
  