delta = {
    ("q0", "0"): "q1",
    ("q0", "1"): "q2",
    ("q1", "0"): "q0",
    ("q1", "1"): "q3",
    ("q2", "0"): "q3",
    ("q2", "1"): "q0",
    ("q3", "0"): "q2",
    ("q3", "1"): "q1",
}


def test_string(string):
    final_state = "q0"
    state = "q0"

    for character in string:
        state = delta[state, character]

    if final_state == state:
        print(f"'{string}' \tSí es aceptada.")
    else:
        print(f"'{string}' \tNo es aceptada.")


strings = ["0011", "00", "001", "00011", "000111", "000110","00110"]

for string in strings:
    test_string(string)
