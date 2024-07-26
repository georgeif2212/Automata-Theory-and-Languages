# importamos la librería de expresiones regulares
import re

# importamos la función urlopen
from urllib.request import urlopen

url_programa = "https://raw.githubusercontent.com/iarobles-cursos/automatas-archivos/main/programa.py"
# obtiene el programa de la url dada en forma de texto (cadena) en encoding utf-8
programa = urlopen(url_programa).read().decode("utf-8")

########################################################
# tokens y sus expresiones regulares que los definen
tokens = {
    "comentario": "#[a-zA-Z0-9 ]*",
    "espacios": "[ \t\n]+",
    "for": "for",
    "equal": "=",
    "if": "if",
    "in": "in",
    "len": "len",
    "print": "print",
    "comillas":"\"|\"",
    "string":"\"[_a-zA-Z0-9]*\"",
    "enteros": "[0-9]+",
    "simbolosEspeciales": "\[|\]|\(|\)|,|:",
    "identificador": "[_a-zA-Z][_a-zA-Z0-9]*",
}
########################################################

# crea un mapa con las expresiones regulares compiladas
exp_regs = dict(
    (nombre_token, re.compile(exp_reg)) for (nombre_token, exp_reg) in tokens.items()
)

# comienza a recorrer el programa buscando tokens
indice = 0
continuar_programa = True
while indice < len(programa) and continuar_programa:
    # Probar si la cadena puede ser reconocida por alguna expresión regular
    se_encontro = False
    for nombre_token, exp_comp in exp_regs.items():
        res = exp_comp.search(programa, indice)
        if res and res.start() == indice:
            valor_token = res.group(0)
            print("Token encontrado:{}, Valor:{}".format(nombre_token, valor_token))
            indice = indice + len(valor_token)
            se_encontro = True
            break

    if not se_encontro:
        print("\nNo se pudo reconocer lo siguiente:")
        print(programa[indice:])
        continuar_programa = False

if indice == len(programa):
    print("\n¡Programa reconocido exitosamente!")
