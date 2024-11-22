# RAPPTOR (test)
## _Generador de Reportes_

App diseñada para cargar archivos .csv y generar un reporte trimestral, anual y general
de las calificaciones otorgadas en las encuestas de satisfacción generadas para CATCH Consulting.

>Hecha por estudiantes de la carrera de IED  de la UPG para el concurso de datos 2024.

### Pre requisitos:
 - VSC
 - Python 3.10
 - Git

### Instrucciones antes de ejecutar app.py por primera vez:

1.- Abrir Visual Studio Code

Inicia VS Code y asegúrate de que tengas las extensiones de Git y Python instaladas.

2.- Clonar el repositorio desde GitHub

 - Ve al menú View > Command Palette o usa Ctrl+Shift+P / Cmd+Shift+P.
 - Escribe Git: Clone y selecciona la opción.
 - Pega la URL del repositorio de GitHub que quieres clonar.
   ```sh
     https://github.com/
   ```
 - Selecciona una carpeta en tu computadora para guardar el proyecto.

3.- Abrir el repositorio clonado

Una vez clonado, VS Code te preguntará si quieres abrir la carpeta. Haz clic en Open.

4.- Crear un entorno virtual(Opcional. Si decides no hacerlo, salta al paso 6)

 - Abre la terminal integrada en VS Code con `Ctrl+```.
 - Crea un entorno virtual dentro del proyecto con el siguiente comando
    ```sh
    python -m venv <nombre_entorno>
    ```

5.- Seleccionar el intérprete del entorno virtual

 - Ve al menú View > Command Palette.
 - Escribe Python: Select Interpreter y selecciona la opción.
 - Busca el intérprete que tiene el prefijo (venv) en el nombre. Esto asegurará que VS Code use el entorno virtual para ejecutar y depurar.

6.- Instalar las dependencias

 - Asegúrate de que la terminal activa sea del entorno virtual (debería decir algo como (venv)).
 - Instala las dependencias listadas en requirements.txt:
    ```sh
    pip install requirements.txt
    ```

7.- Ejecutar el script o aplicación
Abre el archivo app.py y presiona F5 para ejecutarlo desde el depurador de VS Code. Si no tienes configurado el depurador, VS Code te ayudará a crearlo automáticamente.

**Una vez completados estos pasos, se puede ejecutar app.py**
##
##
### _Uso sin pre-requisitos - sólo para pruebas-_

1.- Haz el Fork del repositorio:

 - Ve a la página del repositorio principal en GitHub.
 - Haz clic en el botón Fork en la esquina superior derecha.
 - Esto creará una copia del repositorio en tu cuenta de GitHub.
 
 2.- Abre el Codespace desde tu Fork:

 - Ve al repositorio forkeado en tu cuenta de GitHub.
 - Haz clic en el botón Code (verde, junto al botón de Clonar).
 - Selecciona la pestaña Codespaces.
 - Si no hay un Codespace creado, haz clic en Create Codespace on Main para iniciar uno.
    - Esto abrirá un entorno de desarrollo integrado basado en la nube.
    
3.- Instala las dependencias necesarias:

 - Una vez que se cargue el Codespace, abre la terminal en la interfaz de Codespaces (normalmente está en la parte inferior).
 - Ejecuta el comando para instalar las dependencias del proyecto
    ```sh
    pip install requirements.txt
    ```

4.- Ejecuta app.py

**Una vez completados estos pasos, se puede ejecutar app.py**
###  
###
###
###
###
###
>DISCLAIMER: ESTA ES UNA APLICACIÓN DE PRUEBA HECHA PARA UN CONCURSO EN ESPECÍFICO. 
>SEGURO ESTARÁ LLENA DE BUGS ASÍ QUE NADIE DEBERÍA USARLA.
