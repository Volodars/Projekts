#aprekinat visas izmaksas
#atrast labako vietu svinesanai 
#izveidot edienkarti

from math import *

menesis=int(input("Kura menesi pec kartas tev ir dzimsanas diena? - "))
cilveki=int(input("Kads bus viesu skaits? - "))
laiks=int(input("Cik stundas tu velies svinet savu dzimsanas dienu? - "))
vieta=int(input("Kur jus gribetu svinet savu dzimsanas dienu? Telpa (1) vai daba (2) raksti ciparu - ")) # ( Kafeinica, Izklaides_centrs, Orendeta_maja, Daba )

if vieta==1: vietaa=int(input("Var svinet kafeinica (1), izklaides centra (2) vai orendetaja maja (3). Raksti ciparu, kur tu velies svinet - ")) #edieni 
elif vieta==2: print("Var svinet telta (1), pie ezera (2) vai izklaides centra meza (3). Raksti ciparu, kur tu velies svinet - ")) ") #ieeja katram cilvekam 5 eiro

dzerieni=input("Vai bus vajadzigi dzerieni? Ja vai Ne ") #viens 3 eiro

deserti=input("Vai bus vajadzigi deserti?  Ja vai Ne ") #viens 5 eiro

kuka=input("Kada izmera kuku pirksim? Lielu, videjo vai mazu")

#vieta=="Kafeinica": ("Vietas maksa=laiks*30")
#vieta=="Izklaides_centrs": print("Vietas maksa=laiks*5*cilveki")
#vieta=="Orendeta_maja": print("Vietas maksa=laiks*60")
#vieta=="Daba: print ("Vietas maksa=0")




#if menesis>10 or menesis<4: print("Labak svinet telpa, jo ir auksti ")
#else: print("Var svinet vai telpa, vai uz dabas")



#print("Katram cilvekam bus 20 eiro, un vins pats sastada pusdienu edienkarti ")
