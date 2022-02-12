# -*- coding: utf-8 -*-

# main.py
from fastapi import FastAPI
from pathlib import Path


app = FastAPI()

@app.post("/almacena")
def add(string):
    dataBase = open("data.txt", "a")
    dataBase.write(string + "\n")
    dataBase.close()
    return {"msg" : "Sentence added succesfully"}

@app.get("/consulta")
def buscar(string):
    #si el fichero no existe, la creamos
    file = Path('data.txt')
    file.touch(exist_ok=True)
    #abrimos y troceamos el contenido
    dataBase = open("data.txt", "r").read().splitlines()
    i = 0
    #quitamos los tildes con el metodo maketrans (traduccion)
    a,b = 'áéíóú','aeiou'

    trans = str.maketrans(a,b)
    for line in dataBase:
	    new_line = line.lower() #no tomamos en cuenta minusculas
	    new_line = new_line.translate(trans)
	    if (string in new_line):
		    i += 1 
    print(i)	
    return {"number" : i}

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=12345)
