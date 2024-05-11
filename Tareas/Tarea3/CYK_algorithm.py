from typing import Dict, List, Set


def createMatrix(string_length: int) -> List[List[Set]]:
    table = []

    # * string_length rows are created
    for i in range(string_length):
        row = []
        # * stringLength columns are created and a set is added
        for j in range(string_length):
            row.append(set())
        table.append(row)

    return table


def fillFirstColumn(
    grammar: Dict[str, List[List[str]]], string: str, table: List[List[Set]]
):
    string_length = len(string)
    # * Fill first column
    for i in range(string_length):
        character = string[i]
        # * Extract non terminal symbol side and the production list
        for non_terminal_symbol, production_list in grammar.items():
            # * for loop to iterate between production list
            for terminal_symbol in production_list:
                # * if is terminal_symbol and match with the character add to the first column
                if len(terminal_symbol) == 1 and terminal_symbol == character:
                    table[i][0].add(non_terminal_symbol)

def printFormatedTable(table: List[List[set]]) -> None:
    for row in range(len(table)):
        print(table[row])
    print("")


def cyk(grammar: Dict[str, List[List[str]]], string: str):
    string_length = len(string)
    
    table = createMatrix(string_length)

    fillFirstColumn(grammar, string, table)

    # * loop to iterate between columns
    for j in range(1, string_length):
        # * loop to iterate between rows
        for i in range(string_length - 1):
            # * loop to iterate the number of cartesian product
            for k in range(j):
                if i + k + 1 < string_length:
                    first_set = table[i][k]
                    second_set = table[i + k + 1][j - k - 1]
                    for non_terminal_symbol, production_list in grammar.items():
                        for production in production_list:
                            if production[0] in first_set and production[1] in second_set:
                                table[i][j].add(non_terminal_symbol)  # Añadir el no terminal a la tabla

    start_symbol = list(grammar.keys())[0]
    status = start_symbol in table[0][string_length-1]

    printFormatedTable(table)

    if status:
        print(f"the string: {string} was accepted\n")
    else:
        print(f"the string: {string} was rejected\n")
    print("-----------------------------------------------------")