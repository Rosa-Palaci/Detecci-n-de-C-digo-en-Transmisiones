import pytest
from analizador_transmisiones import contains_code, manacher, longest_common_substring

# Pruebas para la función contains_code usando KMP
def test_contains_code():
    # Casos en los que el código está contenido
    assert contains_code("123ABCDEF987", "ABCDEF") == True
    assert contains_code("A1B2C3D4E5", "C3D4") == True
    
    # Casos en los que el código no está contenido
    assert contains_code("123ABCDEF987", "XYZ") == False
    assert contains_code("ABCDEF", "FEDCBA") == False

# Pruebas para la función manacher (encontrar el palíndromo más largo)
def test_manacher():
    assert manacher("ABC12321CBA") == (1, 11)  # Palíndromo: "12321"
    assert manacher("ABCDE") == (1, 1)  # No hay palíndromo más largo que un solo carácter
    assert manacher("1234554321") == (1, 10)  # Palíndromo: "1234554321"
    assert manacher("BAABBA") == (1, 4)  # Palíndromo: "BAAB"

# Pruebas para la función longest_common_substring (substring común más largo)
def test_longest_common_substring():
    assert longest_common_substring("ABCDEF", "ZBCDF") == (2, 4)  # Substring común: "BCD"
    assert longest_common_substring("123456789", "34567") == (3, 7)  # Substring común: "34567"
    assert longest_common_substring("ABCDEFGH", "XYZABCD") == (1, 4)  # Substring común: "ABCD"
    assert longest_common_substring("ABCDE", "FGHIJ") == (0, 0)  # No hay substring común
