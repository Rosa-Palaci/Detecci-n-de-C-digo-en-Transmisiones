# Detección de Código en Transmisiones

## Descripción

Este programa tiene como propósito analizar y detectar posibles códigos maliciosos dentro de archivos de transmisión. Utiliza tres archivos que contienen secuencias maliciosas y dos archivos que simulan transmisiones de datos para verificar si las secuencias maliciosas están presentes. Además, busca palíndromos dentro de las transmisiones y analiza la similitud entre los archivos de transmisión.

## Funcionalidades

1. **Detección de Códigos Maliciosos**:
   - Verifica si las secuencias de los archivos `mcode1.txt`, `mcode2.txt`, y `mcode3.txt` están presentes en `transmission1.txt` y `transmission2.txt`.
   - Muestra `true` o `false` según si la secuencia está contenida en los archivos de transmisión.

2. **Búsqueda de Palíndromos**:
   - Detecta el palíndromo más largo en `transmission1.txt` y `transmission2.txt` y muestra las posiciones de inicio y fin de cada uno.

3. **Análisis de Similitud**:
   - Encuentra el substring más largo común entre `transmission1.txt` y `transmission2.txt` y muestra las posiciones de inicio y fin en `transmission1.txt`.

## Entrada

El programa no requiere interacción del usuario. Los archivos que deben existir en la misma ruta de ejecución son:

- `transmission1.txt`
- `transmission2.txt`
- `mcode1.txt`
- `mcode2.txt`
- `mcode3.txt`

Estos archivos contienen exclusivamente caracteres entre `0-9`, `A-F`, y saltos de línea.

## Salida

El programa mostrará en consola:

1. **Parte 1**: Para cada archivo de transmisión, indicará si contiene o no las secuencias de los archivos de código malicioso.
   - (true | false) para cada combinación de archivo de transmisión y archivo de código malicioso.
   
2. **Parte 2**: La posición de inicio y final del palíndromo más largo en cada archivo de transmisión.
   - Formato: `posiciónInicial posiciónFinal` para `transmission1.txt` y `transmission2.txt`.

3. **Parte 3**: La posición de inicio y final del substring común más largo entre ambos archivos de transmisión, mostrado respecto a `transmission1.txt`.
   - Formato: `posiciónInicial posiciónFinal`.

## Ejecución

Para ejecutar el programa, solo necesitas asegurarte de que los archivos mencionados existan en la misma carpeta de ejecución. Luego, ejecuta el archivo de Python con:

```bash
$ python nombre_del_programa.py
