
# Instalación y Uso de virtualenv

## Instalación de virtualenv

1. Abre tu terminal o línea de comandos.

2. Asegúrate de tener `pip` instalado. Si no lo tienes, instálalo primero. Dependiendo de tu sistema operativo, puedes usar `apt`, `brew` u otro gestor de paquetes.

3. Una vez que tengas `pip`, instala `virtualenv` ejecutando el siguiente comando:

```
pip install virtualenv

```

## Creación de un entorno virtual

4. Navega a la carpeta donde quieres crear tu entorno virtual.

5. Ejecuta el siguiente comando para crear un nuevo entorno virtual:

```
virtualenv nombre_de_tu_entorno

```

Reemplaza `nombre_de_tu_entorno` por el nombre que quieras darle a tu entorno virtual.

## Activación del entorno virtual

6. Dependiendo de tu sistema operativo, la forma de activar el entorno virtual varía:

- **En Windows:**

```
nombre_de_tu_entorno\Scripts\activate

```

- **En macOS y Linux:**

```
source nombre_de_tu_entorno/bin/activate

```

Después de ejecutar este comando, notarás que el nombre de tu entorno virtual aparece en el prefijo de tu línea de comandos, indicando que el entorno virtual está activo.

¡Y eso es todo! Ahora tienes `virtualenv` instalado, un nuevo entorno virtual creado y activado. Puedes instalar paquetes específicos en este entorno virtual sin afectar a tu sistema global. Recuerda desactivar el entorno virtual cuando hayas terminado trabajando en él con el comando `deactivate`.
