23/12/2024
# Fayllar bilan ishlash

# filename= 'Fayllar_bilan_ishlash.txt'
# with open(filename) as file:
#     file=file.read()
# print(file)

# filename='pi_million_digits.txt'
# with open(filename) as file:
    x=file.readlines()

def top(raqam):
    for a in x:
        a.replace('\n','')
        if str(raqam) in a:
          return 'yes'
    return 'no'

filename='pi_million_digits.txt'
with open(filename) as file:
    x=file.read()
x=x.replace('\n','')
x=x.rstrip()
x=x.replace(' ','')
x=float(x)
import pickle
with open('new_file0','wb') as file:
    x=pickle.dump(x,file)
with open('new_file0','rb') as file:
    x=pickle.load(file)
while True:
    book=input(f"Yaxshi ko'rgan kitobinggizni kiriting(to'xtatish uchun Enterni bosing): ")
    if not book:
        break
    filename='kitob.txt'
    with open(filename,'a') as file:
        file.write(book+'\n')
    with open(filename) as f:
        x=f.read()
    print(x)
print("\nOxirgi fayl mazmuni:")
with open(filename) as f:
    final_content = f.read()
print(final_content)
while True:
    x=input(f"(yes/no)")
    if x=='yes':
        book=input(f"Yaxshi ko'rgan kitobinggizni kiriting: ")
    else:
        break

    




