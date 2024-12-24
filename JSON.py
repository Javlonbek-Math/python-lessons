24/12/2024
# JSON
import json
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
# data_json=json.dumps(data)
# print(type(data_json))

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
talaba=json.loads(talaba_json)
# print(f"{talaba['ism']} {talaba['familiya']}" )
with open('new_file1.json','w') as file:
    json.dump(data,file)
with open('students.json') as file:
    students=json.load(file)
# print(students.values())
for y in students.values():
    for i in range(3):
      a=(y[i]['name'])
      b=(y[i]['year'])
      c=(y[i]['faculty'])
      i+=1
      # print( f"{a}, {b}-kurs, {c} fakultet talabasi")
for item in students['student']:
    print(item)

with open('api-result.json') as file:
    file=json.load(file)
print(file['query']['pages']['13801']['title'])
print(file['query']['pages']['13801']['extract'])

