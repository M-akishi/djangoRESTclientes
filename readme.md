
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

para iniciar el servidor es:

```
   python .\manage.py runserver 
```