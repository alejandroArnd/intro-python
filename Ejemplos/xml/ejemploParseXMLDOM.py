# library                         time    space
# xml.dom.minidom (Python 2.1)    6.3 s   80000K
# gnosis.objectify                2.0 s   22000k
# xml.dom.minidom (Python 2.4)    1.4 s   53000k
# ElementTree 1.2                 1.6 s   14500k
# ElementTree 1.2.4/1.3           1.1 s   14500k
# cDomlette (C extension)         0.540 s 20500k
# PyRXPU (C extension)            0.175 s 10850k
# libxml2 (C extension)           0.098 s 16000k
# readlines (read as utf-8)       0.093 s 8850k
# cElementTree (C extension)  --> 0.047 s 4900K <--


from xml.dom import minidom
from lxml import etree

print('Parseo con minidom')
xmldoc = minidom.parse('ejemplo.xml')
neighborlist = xmldoc.getElementsByTagName('neighbor')
print(len(neighborlist))
print(neighborlist[0].attributes['name'].value)
for neighbor in neighborlist:
    print(neighbor.attributes['name'].value)

print('Parseo con lxml')
xml = etree.parse('ejemplo.xml')
yearsCountry= xml.xpath("/data/country/year/text()")
for year in yearsCountry:
    print(year)
