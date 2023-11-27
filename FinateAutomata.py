states = {'q0', 'q1'}
alphabet = {'0', '1'}
transitions = {
    'q0': {'0': 'q1', '1': 'q0'},
    'q1': {'0': 'q0', '1': 'q1'}
}
initial_state = 'q0'
accepting_states = {'q0'}
def process_input(input_string):
    current_state = initial_state
    for symbol in input_string:
        if symbol not in alphabet:
            raise ValueError(f"Invalid symbol '{symbol}' in input.")
        current_state = transitions[current_state][symbol]
    return current_state in accepting_states
if __name__ == "__main__":
    test_strings = ["0011", "0101", "1100", "101010", "1111"]
    for test_string in test_strings:
        result = process_input(test_string)
        print(f"Input: {test_string}, Result: {'Accepted' if result else 'Rejected'}")
