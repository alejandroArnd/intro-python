import json
import urllib.request

def fetchJSON(url):
    fp = urllib.request.urlopen(url)
    archivoString = fp.read().decode("utf-8")
    fp.close()
    return json.loads(archivoString)


diccionario = fetchJSON("http://vps678826.ovh.net/ejemplo.json")
print("Diccionario completo:\n", diccionario)
print("Nombre:\n", diccionario["Name"])



