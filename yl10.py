name = input("Sisesta oma nimi: ")
print("Tere", name)
location = input("Elukoht: ")
if "saaremaa" in location.lower():
    print("Miks sa elad siin , Hiiumaa parem.")
if "hiiumaa" in location.lower():
    print("Väga õige koht parem , kui Saaremaa.")
age = input("Vanus: ")
age = int(age)    
if age < 18:
    print("Sa oled veel alakas ning  sa ei tohi minna ärtu klubisse.")
elif age == 18:
    print("Väga õige oled 18 võid autoga sõita ja minna ärtu klubisse.")
else:
    print("Oppa vanna härra mis autoga te liigute.")