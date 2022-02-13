from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}

def test_buscar():
    response = client.get("/consulta?string=camion")
    assert response.status_code == 200
    assert response.json() == {"number": 0}

def test_add():
    response = client.post("/almacena?string=avion")
    assert response.status_code == 200
    assert response.json() == {"msg" :  "Sentence added succesfully"}

def test_buscar_avion():
    response = client.get("/consulta?string=avion")
    assert response.status_code == 200
    assert response.json() == {"number": 1}

def test_insertar_acento():
    response = client.post("/almacena?string=lápiz")
    assert response.status_code == 200
    assert response.json() == {"msg" : "Sentence added succesfully"}

#DEBERIA DAR 0
def test_buscar_acento():
    response = client.get("/consulta?string=lápiz")
    assert response.status_code == 200
    assert response.json() == {"number" : 0}

def test_insertar_mayusculas():
    response = client.post("/almacena?string=CORRE")
    assert response.status_code == 200
    assert response.json() == {"msg" :  "Sentence added succesfully"}

#DEBERIA DAR 0
def test_buscar_mayusculas():
    response = client.get("/consulta?string=CORRE")
    assert response.status_code == 200
    assert response.json() == {"number" : 0}
