person = {
    "first_name": "jurgen",
    "last_name": "Vander",
    "birth_year": 2005,
    "location": "Saaremaa",
    "favorite_dessert": "Fandant",
}

print(person.get("location"))
print(person["location"])

person["favorite_dessert"] = "jäätis"

for key in person:
    print(key)

for value in person.values():
    print(value)

if "isikukood" in person:
    print("Isikukood on leitud ja olemas!")
else:
    print("Isikukoodi ei eksisteeri.")

print(len(person))

person["height"] = "180cm"
del person["birth_year"]

person.clear()
