import xml.etree.ElementTree as ET
from pprint import pprint

#Parsear el xml y coger el nodo raiz
tree = ET.parse('students.xml')
root = tree.getroot()

print("Nombre del nodo raiz: " + root.tag + "\n")

estudiantes = root.findall(".//*[@skillLevel = 'high']/../..")

print("Estudiantes que tengan buenas habilidades en al menos un hobbie:")

listaEstudiantes = []
for estudiante in estudiantes:
    nombre = estudiante.find("name")
    apellido = estudiante.find("lastName")
    listaEstudiantes.append({"name": nombre.text, "lastName": apellido.text})

pprint(listaEstudiantes)

# Cambiar el valor de un atributo
ultimoEstudiante = root.find(".//student[last()]")
hobbie = ultimoEstudiante.find("./hobbies/hobbie[1]")
print("\nHobbie:" + hobbie.text + "\nAtributos del hobbie:")
print(hobbie.attrib)
hobbie.attrib["skillLevel"] = "low---"
print("Atributo cambiado/mejorado: ")
print(hobbie.attrib)

# Guardar el xml
tree.write('output.xml')
