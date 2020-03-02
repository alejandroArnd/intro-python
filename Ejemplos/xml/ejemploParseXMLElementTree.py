import xml.etree.ElementTree as ET
from pprint import pprint

#Parsear el xml y coger el nodo raiz
tree = ET.parse('estudiantes.xml')
root = tree.getroot()

print("Nombre del nodo raiz: " + root.tag + "\n")

estudiantes = root.findall(".//*[@nivel = 'alto']/../..")

print("Estudiantes que tengan buenas habilidades en al menos un hobbie:")

listaEstudiantes = []
for estudiante in estudiantes:
    nombre = estudiante.find("nombre")
    apellido = estudiante.find("apellido")
    listaEstudiantes.append({"nombre": nombre.text, "apellido": apellido.text})

pprint(listaEstudiantes)

# Cambiar el valor de un atributo
ultimoEstudiante = root.find(".//estudiante[last()]")
hobbie = ultimoEstudiante.find("./hobbies/hobbie[1]")
print("\nHobbie:" + hobbie.text + "\nAtributos del hobbie:")
print(hobbie.attrib)
hobbie.attrib["nivel"] = "bajo---"
print("Atributo cambiado/mejorado: ")
print(hobbie.attrib)

# Guardar el xml
tree.write('output.xml', encoding="UTF-8")
