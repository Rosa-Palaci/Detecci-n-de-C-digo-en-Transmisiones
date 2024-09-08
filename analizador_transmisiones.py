def read_file(file_path: str) -> str:
    """
    Lee el contenido de un archivo de texto y lo devuelve como una cadena.
    
    Parámetros:
    - file_path: La ruta del archivo a leer.
    
    Retorna:
    - Una cadena que contiene el contenido del archivo.
    """
    with open(file_path, 'r') as file:
        return file.read()

def compute_lps(pat: str) -> list[int]:
    """
    Calcula la tabla LPS (Longest Prefix Suffix) para el patrón.
    
    Parámetros:
    - pat: El patrón para el cual se calculará la tabla LPS.
    
    Retorna:
    - Una lista que contiene los valores de la tabla LPS.
    """
    length = 0  # Longitud del prefijo más largo que también es sufijo
    lps = [0] * len(pat)
    i = 1

    while i < len(pat):
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def kmp_search(txt: str, pat: str) -> bool:
    """
    Implementa el algoritmo KMP para buscar un patrón en un texto.
    
    Parámetros:
    - txt: El texto en el cual se buscará el patrón.
    - pat: El patrón que se desea buscar en el texto.
    
    Retorna:
    - True si el patrón está contenido en el texto, False en caso contrario.
    """
    m = len(pat)
    n = len(txt)

    # Calcular la tabla LPS
    lps = compute_lps(pat)

    i = 0  # Índice para txt
    j = 0  # Índice para pat
    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == m:
            # Se encontró el patrón
            return True
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False

def contains_code(transmission: str, code: str) -> bool:
    """
    Verifica si el código malicioso está contenido en la transmisión usando el algoritmo KMP.
    
    Parámetros:
    - transmission: La cadena que representa el contenido de la transmisión.
    - code: La cadena que representa el código malicioso.
    
    Retorna:
    - True si el código malicioso está contenido en la transmisión, False en caso contrario.
    """
    return kmp_search(transmission, code)

def manacher(s: str) -> tuple[int, int]:
    """
    Implementa el algoritmo de Manacher para encontrar el palíndromo más largo en una cadena.
    
    Parámetros:
    - s: Cadena de caracteres para analizar el palíndromo.
    
    Retorna:
    - Una tupla con las posiciones inicial y final (1-indexed) del palíndromo más largo.
    """
    if not s:
        return 0, 0

    # Convertimos la cadena para manejar palíndromos pares e impares
    modified_s = '#' + '#'.join(s) + '#'
    N = len(modified_s)
    L = [0] * N
    C = R = 0  # Centro y radio del palíndromo actual
    max_len = 0
    center_index = 0

    for i in range(N):
        mirror = 2 * C - i  # Índice espejo

        if i < R:
            L[i] = min(R - i, L[mirror])

        # Expande el palíndromo centrado en 'i'
        while i + L[i] + 1 < N and i - L[i] - 1 >= 0 and modified_s[i + L[i] + 1] == modified_s[i - L[i] - 1]:
            L[i] += 1

        # Si el palíndromo centrado en 'i' se expande más allá de 'R'
        if i + L[i] > R:
            C = i
            R = i + L[i]

        # Guardar la longitud máxima y el centro del palíndromo más largo
        if L[i] > max_len:
            max_len = L[i]
            center_index = i

    # Calcular el inicio y el fin en la cadena original
    start = (center_index - max_len) // 2  # Ajustar para convertir desde la cadena modificada a la original
    end = start + max_len - 1

    # Retornar las posiciones 1-indexed
    return start + 1, end + 1

def longest_common_substring(s1: str, s2: str) -> tuple[int, int]:
    """
    Encuentra el substring común más largo entre dos cadenas.

    Parámetros:
    - s1: Primera cadena de texto.
    - s2: Segunda cadena de texto.

    Retorna:
    - Una tupla con la posición inicial y final (1-indexed) del substring más largo en s1.
    """
    len_s1, len_s2 = len(s1), len(s2)
    lcs = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]
    max_len = 0
    max_pos = 0

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
                if lcs[i][j] > max_len:
                    max_len = lcs[i][j]
                    max_pos = i

    if max_len == 0:
        return (0, 0)

    start = max_pos - max_len
    end = max_pos - 1
    return start + 1, end + 1  # 1-indexed

def analyze_transmissions() -> None:
    """
    Analiza los archivos de transmisión y códigos maliciosos.

    Parte 1: Verifica si los códigos maliciosos están contenidos en las transmisiones.
    Parte 2: Encuentra el palíndromo más largo en cada archivo de transmisión.
    Parte 3: Encuentra el substring común más largo entre las dos transmisiones.

    No tiene parámetros ni retorna valores. Imprime los resultados directamente.
    """
    # Leer los archivos de transmisión y código malicioso
    transmission1 = read_file("transmission1.txt")
    transmission2 = read_file("transmission2.txt")
    mcode1 = read_file("mcode1.txt")
    mcode2 = read_file("mcode2.txt")
    mcode3 = read_file("mcode3.txt")

    # Parte 1: Verificar si el código malicioso está en las transmisiones usando KMP
    print(contains_code(transmission1, mcode1))
    print(contains_code(transmission1, mcode2))
    print(contains_code(transmission1, mcode3))
    print(contains_code(transmission2, mcode1))
    print(contains_code(transmission2, mcode2))
    print(contains_code(transmission2, mcode3))

    # Parte 2: Encontrar el palíndromo más largo en las transmisiones
    start1, end1 = manacher(transmission1)
    start2, end2 = manacher(transmission2)
    print(f"{start1} {end1}")
    print(f"{start2} {end2}")

    # Parte 3: Encontrar el substring común más largo entre las transmisiones
    start_common, end_common = longest_common_substring(transmission1, transmission2)
    print(f"{start_common} {end_common}")

if __name__ == "__main__":
    analyze_transmissions()
