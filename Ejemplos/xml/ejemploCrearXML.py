from lxml import etree, objectify


# ----------------------------------------------------------------------
def crearEstudiante(data):
    """
    Crear elemento estudiante
    """
    estudiante = objectify.Element("estudiante")
    estudiante.uid = data["uid"]
    estudiante.nombre = data["nombre"]
    estudiante.apellido = data["apellido"]
    estudiante.pais = data["pais"]
    estudiante.ciudad = data["ciudad"]
    return estudiante


# ----------------------------------------------------------------------
def create_xml():
    """
    Crear fichero xml
    """

    xml = '''<?xml version="1.0"?><clase></clase>'''

    root = objectify.fromstring(xml)
    root.set("nombre", "S21AW")

    estudiante1 = crearEstudiante({
        "uid": "604f4792-eb89-478b-a14f-dd34d3cc6c21-1234355555",
        "nombre": "Alex",
        "apellido": "Aranda",
        "pais": "España",
        "ciudad": "Málaga"
    }
    )
    root.append(estudiante1)

    uid = "604f4792-eb89-478b-a14f-dd34d3cc6c21-1234360800"
    estudiante2 = crearEstudiante({
        "uid": uid,
        "nombre": "Roberto",
        "apellido": "Muñoz de León",
        "pais": "España",
        "ciudad": "Málaga"
    }
    )
    root.append(estudiante2)

    # Quitar anotaciones lxml

    objectify.deannotate(root)
    etree.cleanup_namespaces(root)

    # Crear xml string
    obj_xml = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding='UTF-8')

    try:
        with open("example.xml", "wb") as xml_writer:
            xml_writer.write(obj_xml)
    except IOError:
        pass


# ----------------------------------------------------------------------
create_xml()
