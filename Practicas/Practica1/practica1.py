# importar módulo de expresiones regulares
import re


# definir función de python


# Cuando se reconoce la cadena: <re.Match object; span=(0, 0), match=''>
# Cuando no se reconoce la cadena: None
def ev_exp_reg(exp_reg, string):
    result = re.fullmatch(exp_reg, string)
    if result:  # Si result contiene algo (es diferente de none)
        print(result, ": accepted")
    else:
        print(result, ": rejected")


# ? Reconocer cadenas vacías

string = ""
exp_reg = ""
ev_exp_reg(exp_reg, string)

# ? expresión regular como un solo símbolo
exp_reg = "a"
string = "hola"
ev_exp_reg(
    exp_reg, string
)  # no reconoce la cadena string porque no cumple con la expresión regular, en este caso solo un símbolo "a"

# ? expresión regular concatenación
exp_reg = "ab"  # se reconoce ab
string = "ab"
string2 = "abc"
ev_exp_reg(
    exp_reg, string
)  # reconoce la cadena string porque cumple con la expresión regular "ab"
ev_exp_reg(
    exp_reg, string2
)  # no reconoce la cadena string porque no cumple con la expresión regular, solo reconoce "ab"

# ? cerradura de klein
exp_reg = "a*"  # se reconoce 0 más veces la letra "a"
string = "aa"
string2 = ""
string3 = "aaab"
ev_exp_reg(exp_reg, string)  # reconoce la cadena
ev_exp_reg(exp_reg, string2)  # reconoce la cadena string
ev_exp_reg(exp_reg, string3)  # no reconoce la cadena string
exp_reg = "a+b"  # se reconoce 0 más veces la letra "a"
ev_exp_reg(exp_reg, string3)  # reconoce la cadena string

# ? Agrupación

exp_reg = "(ab)*"  # se reconoce 0 más veces la letra "a"
string = "ab"
string2 = "(ab)"
string3 = "ababab"
ev_exp_reg(exp_reg, string)  # reconoce la cadena
ev_exp_reg(
    exp_reg, string2
)  # no reconoce la cadena porque los parentesis son metacaracter
ev_exp_reg(exp_reg, string3)  # reconoce porque el patrón "ab" se repite 0 o más veces

# ? Disyunción

exp_reg = "a|b"  # se reconoce 0 más veces la letra "a"
string = "a"
string2 = "b"
string3 = "ab"
ev_exp_reg(exp_reg, string)  # reconoce la cadena a
ev_exp_reg(exp_reg, string2)  # reconoce la cadena b
ev_exp_reg(exp_reg, string3)  # no  reconoce 
