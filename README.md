# Deploy de modelos.

Existen varias maneras de poner nuestros modelos en produccion, aca vamos a ver como hacerlo usando Streamlit y Heroku.
 

### Streamlit

Las apps de streamlit, son bastante sencillas, es un script de python normal y vamos insertando los widgets que necesitamos en el cuerpo del script. 

Un ejemplo basico, una pagina web que diga 'hola':

```python
import streamlit as st
st.write('hola!')
```
Lo guardamos en un archivo.py y para ejecutarlo:

```bash
streamlit run archivo.py
``` 
Luego desde nuestro navegador vemos nuestro mensaje, si bien esto es lo mas deprimente que vieron en la semana, streamlit tiene una lista larga de widgets disponibles [aca](https://docs.streamlit.io/api.html). De manera de que podemos en esta pagina web mostrar graficos que interactueen con widgets como: slides, multiplechoice, inputs de todo tipo. 

Con una syntasis muy sencilla generar una interfaz web para que nosotros o cualquier persona con un navegador pueda interactuar con nuestros complejos modelos de machine learning.

Hasta aca todo perfecto, pero hay un detalle... todo eso funciona de manera local, para poder tenerlo en funcionamiento online falta algo mas.



### Heroku 


Heroku es una plataforma que da servicio de hosting de maquinas virtuales, asi uno puede tener corriendo su modelo online y accesible desde cualquier navegador (incluso movil). 


1. Ir a [heroku.com](https://signup.heroku.com/) y registrarse.
2. Crear nueva app [aca](https://dashboard.heroku.com/new-app).
3. En el menu de la APP, ir a deploy method y seleccionar connect to Github.
4. Asociar heroku con su cuenta de github, buscar el repositorio donde tenemos nuestra app y conectar.
5. Seleccionaremos automatic deploys para que se actualice automáticamente las versiones de nuestra app, y por ultimo le damos a DEPLOY BRANCH.


Para crear la maquia virtual en heroku, tenemos que especificar la version de python y de las librerias presentes en nuestra app, esto lo hacemos en los archivos requirements y runtime que estan en el repositorio de github que asociamos a nuestra APP de heroku.

Ejemplo del contenido de estos archivos esta este repositorio:

https://github.com/carabedo/properatti

```bash
app.py
requirements.txt
runtime.txt
Procfile
create_config.sh
``` 

El archivo .py con la app de streamlit, la misma que probamos que funciona en nuestras compus:

[app.py](st3.py)

Un archivo con las librerias que va usar nuestra app, es la lista de librerias que se necesitan instalar en la maquina virtual 
para que todo ande bien

[requirements.txt](requirements.txt)



Esta app esta funcionando en:

[properatti.herokuapp.com](https://properatti.herokuapp.com/)
