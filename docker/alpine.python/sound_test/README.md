# Descripción del proyecto

Este es un proyecto de prueba para crear un ambiente de desarrollo con Docker, que incluye un contenedor con Alpine, Python y PulseAudio, y un ejemplo simple de cómo usarlo para reproducir un archivo de audio generado a partir de texto.

## Requisitos

- Docker
- docker-compose

## Instrucciones

Para ejecutar este proyecto, sigue los siguientes pasos:

1. Clona este repositorio en tu máquina local ejecutando el siguiente comando:

```bin/bash
git clone https://github.com/codejach/public_skills.git
```


2. En la terminal, navega hasta la carpeta del proyecto y ejecuta el siguiente comando:
```bin/bash
make install
```
Esto construirá la imagen de Docker del servicio `install`, que instalará las dependencias de Python del proyecto.


3. Después de que la imagen se haya construido, ejecuta el siguiente comando:
```bin/bash
make run
```
Esto ejecutará el contenedor y permitirá que puedas usarlo para reproducir audio.


4. Para probar que el contenedor funciona correctamente, ejecuta el siguiente comando:
```bin/bash
make dev
```
Esto abrirá una sesión de shell en el contenedor, desde donde podrás ejecutar los scripts del proyecto.


5. Para detener el contenedor, ejecuta el siguiente comando:
```bin/bash
make stop
```


