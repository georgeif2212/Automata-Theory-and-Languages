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


