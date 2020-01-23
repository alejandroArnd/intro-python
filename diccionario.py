# Ejemplo de como usar un diccionario

dictionary = {
    "Name": "Alex",
    "Age": 20,
    "Profession": "Airplane Destroyer",
    "hobbies": "Strolling"
}

print(dictionary["Profession"])
dictionary["Profession"] = "Programmer"
print(dictionary["Profession"])
dictionary.clear()
print(dictionary)
