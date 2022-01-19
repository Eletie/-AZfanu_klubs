#Danils
print("kā iesākt")

linoleja_cena = int(input("Ievadi linoleja cenu ")) #ievadīt linoleju cenu
telpas_platums = int(input("Cik plata ir telpa? " )) #telpas platums
telpas_garums = int(input("Cik gara ir telpa? ")) #telpas garums

def gridas_izmaksas():
  telpas_lielums = telpas_garums * telpas_platums #aprēķina telpas lielumu
  linoleja_izmaksas = telpas_lielums * linoleja_cena #aprēķina linoleja izmaksas
  print("Linoleja izmaksas ir ", str(linoleja_izmaksas), "eiro.")

gridas_izmaksas() #ja c