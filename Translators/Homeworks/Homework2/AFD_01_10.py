delta = {
    ("q0", "0"): "q1",
    ("q0", "1"): "q2",
    ("q1", "0"): "q4",
    ("q1", "1"): "q3",
    ("q2", "0"): "q3",
    ("q2", "1"): "q4",
    ("q3", "0"): "q3",
    ("q3", "1"): "q3",
    ("q4", "0"): "q4",
    ("q4", "1"): "q4",
}


def test_string(string):
    final_state = "q3"
    state = "q0"

    for character in string:
        state = delta[state, character]

    if final_state == state:
        print(f"'{string}' \tSí es aceptada.")
    else:
        print(f"'{string}' \tNo es aceptada.")


strings = ["0011", "0111111", "001", "100000", "110000", "10","01"]

for string in strings:
    test_string(string)
