from uzwords1 import words
import random
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
    print(f"I thought {len(word)}-letters word, try to find it!")
    while word_letters:
        print(display(user_letters, word))
        if user_letters:
            print(f"You guessed words so far: {user_letters}")
        letter=input("Guess a letter to find word!:  ")
        if letter in user_letters:
            print("You already used this word, guess another word!")
            continue
        elif letter in word_letters:
            word_letters.remove(letter)
            print('You found! Continue!')
        else:
            print('Uncorrect')
        user_letters+=letter
    print(f"Congratulation! You found ' {word} ' in a {len(user_letters)}-attemt.")
play()
    