# Ejemplo de como usar un diccionario

dictionary = {
    "Nombre": "Alex",
    "Edad": 20,
    "Profesion": "Destructor de aviones",
    "hobbies": "Pasear"
}

print(dictionary["Profesion"])
dictionary["Profesion"] = "Programador fraudulento"
print(dictionary["Profesion"])
dictionary.clear()
print(dictionary)
