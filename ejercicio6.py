# -*- coding: utf-8 -*-
#!/usr/bin/env python

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import json

with open("peliculas.json") as fichero:
	doc=json.load(fichero)
fi=open("Peliculas.html","w")
for l in doc["peliculas"]["pelicula"]:
	
	fi.write("<h1>"+str(l["titulo"])+"</h1>"+"\n")
	fi.write("<p>"+str(l["sinopsis"])+"</p>"+"\n")
	fi.write("<a href="+str(l["url"])+">"+"Enlace"+"</a>"+"\n")


fi.close()
	
	