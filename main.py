import math

print("Linoleja ieklāšanas aprēķinu programma")

linoleja_cena = float(input("Ievadi linoleja cenu EUR/m2 ")) #ievadīt linoleju cenu
linoleja_platums = float(input("Ievadi linoleja platumu "))
telpas_platums = float(input("Cik plata ir telpa? " )) #telpas platums
telpas_garums = float(input("Cik gara ir telpa? ")) #telpas garums

def gridas_izmaksa(linoleja_cena, linoleja_platums, telpas_platums, telpas_garums):
  telpas_laukums = math.ceil(telpas_garums) * math.ceil(telpas_platums) #aprēķina telpas lielumu
  linojeja_izmaksas = float(telpas_laukums * linoleja_cena) #aprēķina linoleja izmaksas
  return linojeja_izmaksas


print("grīdas izmaksas ir " + str(gridas_izmaksa(linoleja_cena, linoleja_platums, telpas_platums, telpas_garums)) + "eiro.")
