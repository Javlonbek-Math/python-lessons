import random as r
print('Keling taxminni topish oyinini oynaymiz!')
def son_top():
    s=r.randint(1, 10)
    i=0
    while True:
      i+=1
      
      y=int(input('>>>'))
      if s>y:
            print('Xato, men oylagan son bundan kattaroq')        
      elif s<y:
            print('Xato, men oylagan son bundan kichikroq')
      else:
            break
    print(f"Tabriklayman siz {i}-taxminda topdinggiz!")
    return i
def son_top_pc():
    input("Siz 1 dan 10 gacha son o'ylang,son o'ylagan bo'lsanggiz istalgan tugmani bosing va men topishga harakat qilaman")
    j=0
    quyi=1
    yuqori=10
    while True:
        j+=1
        taxmin=r.randint(quyi, yuqori)
        javob=input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri (t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob=='+':
            quyi=taxmin+1
        elif javob=='-':
            yuqori=taxmin-1
        else: 
            break
    print(f"Tabriklaymiz siz {j}-urinishda topdinggiz!")
    return j
def play():
    yana=True
    while yana:
        taxminlar_user=son_top()
        taxminlar_pc=son_top_pc()
        if taxminlar_user>taxminlar_pc:
            print("Men yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdinggiz!")
        else:
            print("Durrang")
        yana=int(input("Yana davom etishni xoylaysizmi? Ha(1) yoki Yo'q(0):"))
play()

            
            
        
        
    
    


    

    
    
            
        

