from math import *

menesis=int(input("Kura menesi pec kartas tev ir dzimsanas diena? - "))
print(" ")
cilveki=int(input("Kads bus viesu skaits? - "))
print(" ")
laiks=int(input("Cik stundas tu velies svinet savu dzimsanas dienu? - "))
print(" ")
vieta=int(input("Kur jus gribetu svinet savu dzimsanas dienu? Telpa (1) vai daba (2) raksti ciparu - ")) 
if vieta==1: vietaa=int(input("Var svinet kafeinica (1), izklaides centra (2) vai orendetaja maja (3). Raksti ciparu, kur tu velies svinet - "))  
elif vieta==2: vietaa=int(input("Var svinet telta (4), pie ezera (5) vai izklaides centra meza (6). Raksti ciparu, kur tu velies svinet - "))
print(" ")

if vietaa==1: Vietasmaksa=0
elif vietaa==2: Vietasmaksa=10*cilveki*laiks
elif vietaa==3: Vietasmaksa=60*laiks
elif vietaa==4: Vietasmaksa=20*laiks
elif vietaa==5: Vietasmaksa=60
elif vietaa==6: Vietasmaksa=15*laiks*cilveki

print(" ")
pirmamaksa=Vietasmaksa

dzerieni=input("Vai bus vajadzigi dzerieni? Ja vai Ne - ")

if dzerieni=="Ja": dzerienimaksa=3*cilveki
elif dzerieni==Ne: dzerienimaksa=0

otrmaksa=dzerienimaksa

print(" ")
deserti=input("Vai bus vajadzigi deserti?  Ja vai Ne - ")

if deserti=="Ja": desertimaksa=5*cilveki
elif deserti=="Ne": desertimaksa=0

tresimaksa=desertimaksa
print(" ")
kuka=int(input("Kada izmera kuku pirksim? Lielu (3), videjo (2) vai mazu (1) - "))
print(" ")
if kuka==1: kukasmaksa=20
elif kuka==2: kukasmaksa=30
elif kuka==3: kukasmaksa=50

cerurtamaksa=kukasmaksa

if vieta==1: edienkarte=int(input("Izvelies vienu no piedavatam edienkartem: fri kartupeli un hamburgeri (1) , dazadas uzkodas un augli (2) , picca (3) - "))
elif vieta==2: edienkarte=int(input("Izvelies vienu no piedavatam edienkartem: cepta gala un darzeni (4) , sviestmaizes un salati (5) , kokogles folijas kartupeli un svaigi darzeni (6) , picca (7) - "))

if edienkarte==1 : maksaparedieniem=cilveki*7
elif edienkarte==2 : maksaparedieniem=cilveki*5
elif edienkarte==3 : maksaparedieniem=cilveki*9
elif edienkarte==4 : maksaparedieniem=cilveki*11
elif edienkarte==5 : maksaparedieniem=cilveki*8
elif edienkarte==6 : maksaparedieniem=cilveki*5
elif edienkarte==7 : maksaparedieniem=cilveki*9

piektamaksa=maksaparedieniem
print(" ")
visasmaksas=(pirmamaksa+otrmaksa+tresimaksa+cerurtamaksa+piektamaksa)
print("Kopejas izmaksas eiro ir - ", visasmaksas)
print(" ")
if vietaa==1: print("Vieta svinesanai - kafeinica")
elif vietaa==2: print("Vieta svinesanai - izklaides centrs")
elif vietaa==3: print("Vieta svinesanai - orendetaja maja")
elif vietaa==4: print("Vieta svinesanai - telts")
elif vietaa==5: print("Vieta svinesanai - pie ezera")
elif vietaa==6: print("Vieta svinesanai - izklaides centrs meza")
print(" ")

if edienkarte==1 : print("Edienkartes sastava bus fri kartupeli un hamburgeri")
elif edienkarte==2 : print("Edienkartes sastava bus dazadas uzkodas un augli")
elif edienkarte==3 : print("Edienkartes sastava bus picca")
elif edienkarte==4 : print("Edienkartes sastava bus cepta gala un darzeni")
elif edienkarte==5 : print("Edienkartes sastava bus viestmaizes un salati")
elif edienkarte==6 : print("Edienkartes sastava bus kokogles folijas kartupeli un svaigi darzeni") 
elif edienkarte==7 : print("Edienkartes sastava bus picca")
print(" ")
