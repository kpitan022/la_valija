# la_valija

## compilar en un solo archivo:

```bash

pyinstaller --noconfirm --onefile --windowed --add-data "C:/mi_codigo/la_valija/credencial.jpeg;."  "C:/mi_codigo/la_valija/gui.py"

```

> agregar la imagen credencial.jpg en el mismo directorio que el archivo ejecutable

## compilar en una carpeta:

```bash

pyinstaller --noconfirm --onedir --windowed --add-data "C:/mi_codigo/la_valija/credencial.jpeg;."  "C:/mi_codigo/la_valija/gui.py"

```
