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


def fillFirstColumn(
    grammar: Dict[str, List[List[str]]], string: str, table: List[List[Set]]
):
    stringLength = len(string)
    # * Fill first column
    for i in range(stringLength):
        character = string[i]

        # * Extract non terminal symbol side and the production list
        for nonTerminalSymbol, production_list in grammar.items():

            # * for loop to iterate between production list
            for terminalSymbol in production_list:

                # * if is terminalSymbol and match with the character add to the first column
                if len(terminalSymbol) == 1 and terminalSymbol == character:
                    table[i][0].add(nonTerminalSymbol)


def cyk(grammar: Dict[str, List[List[str]]], string: str):

    stringLength = len(string)
    # Initialize the table
    table = createMatrix(stringLength)

    fillFirstColumn(grammar, string, table)

    for row in table:
        print(row)

    for i in range(stringLength - 1):
        for j in range(1, stringLength):
            for k in range(j - 1):
                # Hacer producto cartesiano para obtener opciones
                # opciones = Vik X Vi + k, j-k
                return

    # print(table)

    print("--------------------------------------------------------------")
