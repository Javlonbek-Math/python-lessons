from uzwords import words
import random  
# def get_word():
#     word=r.choice(words)
#     print(f"Men {len(word)}-xonali so'z o'yladim, topa olasizmi?")
#     harf=input("Harf kiriting: ")
#     return word
# soz=get_word()
# print(soz)
def get_word():
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word
def display(user_letters,word):
    display_letter=''
    for letter in word:
        if letter in user_letters:
            display_letter+=letter
        else:
            display_letter+='-'
    return display_letter
def play():
    word=get_word()
    word_letters=set(word)
    user_letters=''
    print(f"Men {len(word)}-xonali so'z o'yladim, topa olasizmi?")
    while len(word_letters)>0:
        print(display(user_letters, word))
        if len(user_letters)>0:
            print(f"Shu vaqtgacha kiritgan harflaringgiz:  {user_letters}")
        letter=input('Harf kiriting: ').upper()
        if letter in user_letters:
            print('Bu harfni oldin kiritgansiz, boshqa harf kiriting!')
            continue
        elif letter in word:
            word_letters.remove(letter)
        else:
            print('Bunday harf yo\'q')
    print(f"Табриклайман! {word} сўзини {len(user_letters)} та уринишда топдингиз.")
play()
        

        


    

            
            
        
        
    
    


    

    
    
            
        

