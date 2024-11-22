# RAPPTOR (test)
## _Generador de Reportes_

App diseñada para cargar archivos .csv y generar un reporte trimestral, anual y general
de las calificaciones otorgadas en las encuestas de satisfacción generadas para CATCH Consulting.

>Hecha por estudiantes de la carrera de IED  de la UPG para el concurso de datos 2024.

### Pre requisitos:
 - VSC
 - Python 
 - Git

### Instrucciones antes de ejecutar app.py por primera vez:

1.- Abrir Visual Studio Code.

Inicia VS Code y asegúrate de que tengas las extensiones de Git y Python instaladas.

2.- Clonar el repositorio desde GitHub.

 - Ve al menú View > Command Palette o usa Ctrl+Shift+P / Cmd+Shift+P.
 - Escribe Git: Clone y selecciona la opción.
 - Pega la URL del repositorio de GitHub que quieres clonar.
   ```sh
     https://github.com/Samuel-Emeus-Jun/prototipo_producto
   ```
 - Selecciona una carpeta en tu computadora para guardar el proyecto.

3.- Abrir el repositorio clonado.

Una vez clonado, VS Code te preguntará si quieres abrir la carpeta. Haz clic en Open.

4.- Crear un entorno virtual. 
_(Opcional, pero muy recomendable. Si decides no hacerlo, salta al paso 6)_

 - Abre la terminal integrada en VS Code con `Ctrl+ñ`.
 - Crea un entorno virtual dentro del proyecto con el siguiente comando
    ```sh
    python -m venv <nombre_entorno>
    ```

5.- Seleccionar el intérprete del entorno virtual.

 - Ve al menú View > Command Palette.
 - Escribe Python: Select Interpreter y selecciona la opción.
 - Busca el intérprete que tiene el prefijo (venv) en el nombre. Esto asegurará que VS Code use el entorno virtual para ejecutar y depurar.

6.- Instalar las dependencias.

 - Abre una nueva terminal PowerShell
 - Escribe en la terminal
     ```sh
     .\<nombre_entorno>\Scripts\Activate
    ```
 - Asegúrate de que la terminal activa sea del entorno virtual (debería decir algo como (venv) al principio de la linea).
 - Instala las dependencias listadas en requirements.txt:
    ```sh
    pip install -r requirements.txt
    ```
   - _Toma su tiempo, se paciente._
   
 #
**Una vez completados estos pasos, se puede ejecutar app.py**

7.- Ejecutar el script o aplicación
Abre el archivo app.py y presiona F5 para ejecutarlo desde el depurador de VS Code. Si no tienes configurado el depurador, VS Code te ayudará a crearlo automáticamente.

##
##
###
###
###
###
>DISCLAIMER: ESTA ES UNA APLICACIÓN DE PRUEBA HECHA PARA UN CONCURSO EN ESPECÍFICO. 
>SEGURO ESTARÁ LLENA DE BUGS ASÍ QUE NADIE DEBERÍA USARLA.
