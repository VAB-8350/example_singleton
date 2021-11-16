1-Implementar el Patrón Singleton mediante un ejemplo en el lenguaje que habitualmente utiliza.
2-Explicar el ejemplo y hacer una captura del código del Patrón.

Realizamos un patron Singleton en python, el ejemplo refiere a una consulta del dolar que puede
ser instanciada en cualquier momento pero siempre devolvera el primer valor con el que se instancio.


En el archivo singleton.py encontrara el corazon del codigo, en este caso esta realizado con decoradores, podra 
observarlos mejor cuando se utiliza el decorador en el archivo dolar_singelton.py. En el archivo consulta podra 
realizar consultas del dolar reciviendo un valor aleatorio entre 200 y 230.

-test unitarios
para los test unitarios fue utilizada la libreria de pytest y puede comprobar el funsionamiento de singleton
ingresando 'pytest' en consola ubicado en la raiz de este repositorio.