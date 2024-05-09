from typing import Dict, List, Set


def createMatrix(stringLength: int) -> List[List[Set]]:
    table = []

    # * stringLength rows are created
    for i in range(stringLength):
        row = []
        # * stringLength columns are created and a set is added
        for j in range(stringLength):
            row.append(set())
        table.append(row)

    return table


def cyk(grammar: Dict[str, List[List[str]]], string: str):

    stringLength = len(string)
    # Initialize the table
    table = createMatrix(stringLength)

    # Llenar la primera columna con producciones terminales
    for j in range(stringLength):
        character = string[j]  # Carácter actual
        for lhs, rhs_list in grammar.items():
            for rhs in rhs_list:
                # Si el lado derecho es un terminal y coincide con el carácter actual
                if len(rhs) == 1 and rhs == character:
                    table[j][0].add(lhs)  # Agrega el símbolo no terminal a la tabla
    # print(table)
    for row in table:
        print(row)
    print("--------------------------------------------------------------")
