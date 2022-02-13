## DevOps A2 - Unit Testing 🚀
_Esta actividad consiste en ampliar la aplicación web de la [Actividad 1](https://github.com/lapuya/DevOps_1_WebService)._

### Requisitos 📋
* Test Unitarios
* Script que facilite la provisión del servicio, cuya invocación permita comenzar a hacer peticiones

### Pre-requisitos ✅
* [Actividad 1](https://github.com/lapuya/DevOps_1_WebService)
* Python 3+
* pytest
* request 
* Coverage


### Pasos e instalación 🔧
Instalación de _pytest_:
```
pip install pytest
```
Después, instalaremos _requests_:
```
pip3 install requests
```
Tendremos listo el programa.
### Pruebas ⚙️
Ejecutamos el script localizado en el _run.sh_: 
```
./run.sh
```
Esto lanzará la herramienta de medición que realizará los test unitarios, abrirá un html con los resultados, instalará fastapi y lanzará el servicio.

## Importante :exclamation:
En el run.sh, la sentencia:
```
python main.py
```
No se ejecutará porque aparecerá que "uvicorn is not defined", por lo tanto no se levantará el servidor. *NO SE HA ENCONTRADO SOLUCIÓN A PESAR DE VARIOS INTENTOS*
En el archivo main.py habrá que descomentar el import para que se levante el servicio, pero a cambio no se ejecutará los tests porque aparecerá que no se encuentra el modulo llamado 'uvicorn'.
### Referencias 🛠️
* [pytest](https://docs.pytest.org/en/7.0.x/)
* [requests](https://www.w3schools.com/python/module_requests.asp)
* [coverage](https://coverage.readthedocs.io/en/6.3.1/)
* [FastAPI](https://fastapi.tiangolo.com)
* [Testing con FastApi](https://fastapi.tiangolo.com/tutorial/testing/)

