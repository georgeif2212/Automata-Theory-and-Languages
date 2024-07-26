from CYK_algorithm import cyk

if __name__ == "__main__":

    grammar_1 = {
        "A": ["BC", "AB", "1"],
        "B": ["AA", "0"],
        "C": ["CB", "1", "0"]
    }
    grammar_2 = {
        "S": ["XY"],
        "X": ["SY", "ZZ", "0"],
        "Y": ["XX"],
        "Z": ["1"]
    }
    grammar_3 = {
        "S": ["AB"],
        "A": ["BB", "a"],
        "B": ["AB", "b"]
    }
    cyk(grammar_1, "110100")
    cyk(grammar_2, "00111")
    cyk(grammar_3, "aabbb")
