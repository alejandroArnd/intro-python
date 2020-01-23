import json

# Leer JSON
#fp === File Pointer
with open("autores.json", "r") as fp:
    diccionario = json.load(fp)
    # diccionario[0]["Name"] = "Mauricio"
    print(json.dumps(diccionario, indent=4))

# Escribir JSON
modulos = [
    {
        "Nombre": "Cliente",
        "Duracion": "200"
     },
    {
        "Nombre": "Servidor",
        "Duracion": "200"
    }
]

with open("miArchivo.json", "w") as fp:
    json.dump(modulos, fp)