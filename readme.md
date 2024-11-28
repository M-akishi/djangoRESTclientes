
# Django REST evaluando data

este proyecto necesita python 64 bit

descargar este repositorio e instalar con pip los requerimientos:

```
    pip -m venv venv_64
    pip install -r requirements.txt
    .\venv_64\Scripts\activate
```

las urls disponibles son:

```
/api/clientes (acepta json)
/clientes (listar clientes en formulario) GET
/clientes/eliminar/* (en * se ingresa el id del cliente a eliminar) POST
/clientes/editar/* (en * se ingresa el id del cliente a editar) POST
/estadistica (Resumen general de la data actual)
```
en /clientes se le pueden agregar filtros:

?edad_min=  (edad minima) \
?edad_max   (edad maxima) \
?satisfaccion= (nivel de satisfaccion 0 al 5) \
?genero= (genero M o F) \
?activo= (activo 1 Inactivo 0)

para iniciar el servidor es:

```
   python .\manage.py runserver 
```