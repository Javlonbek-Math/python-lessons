# Amaliyot: 11/11/2024
#buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           #'tyil':810,
           #'vyil':870,
           #'tjoy':'Buxoro'
#           }

#qodiriy = {'ism':'Abdulla Qodiriy',
#           'tyil':1894,
#           'vyil':1938,
#           'tjoy':'Toshkent'
#           }

#vohidov = {'ism':'Erkin Vohidov',
 #          'tyil':1936,
  #         'vyil':2016,
  #         'tjoy':"Farg'ona"
  #         }

#navoiy = {'ism':'Alisher Navoiy',
  #         'tyil':1441,
   #        'vyil':1501,
  #         'tjoy':"Xirot"
  #         }
#shaxslar=[buxoriy,qodiriy,vohidov,navoiy]
#for shaxs in shaxslar:
#    age=shaxs['vyil']-shaxs['tyil']
    #print(f"{shaxs['ism']} {shaxs['tyil']}-da {shaxs['tjoy']}da tavallud topgan."
   #       f"{age} yil umr ko'rgan")
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }
# shaxslar=[buxoriy,qodiriy,vohidov,navoiy]
# # for shaxs in shaxslar:
# #     print(f"{shaxs['ism']} ning mashxur asarlari")
# #     for asar in shaxs['asarlar']:
# #      print(asar)
# # kinolar = {
# #     'ali':['Terminator','Rambo','Titanic'],
# #     'vali':['Tenet','Inception','Interstellar'],
# #     'hasan':['Abdullajon','Bomba','Shaytanat'],
# #     'husan':['Mahallada duv-duv gap','John Wick']
# #     }
# # for k,v in kinolar.items():
# #     print(f"{k}ning sevimli kinolar:")
# #     for x in v:
# #         print(x)
davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }
# for x,y in davlatlar.items():
#     print(f"{x}ning poytaxti: {y['poytaxt']}")
#     print(f"Hududi: {y['maydon']}")
#     print(f"Aholisi: {y['aholi']}")
#     print(f"Pul birligi: {y['pul birligi']}")
x=input('Davlat nomini kiriting: ')
if x in davlatlar:
 y=davlatlar[x]
 print(f"{y['poytaxt']}")
else: print('bizda bunday davlat mavjud emas')
   

          
    
    
