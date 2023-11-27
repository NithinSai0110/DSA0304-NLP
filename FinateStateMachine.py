import re

# Define the states of the finite-state machine
states = {'q0', 'q1', 'q2', 'q3', 'q4'}

# Define the alphabet (input symbols)
alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Define the transition function
transitions = {
    'q0': {'e': 'q1'},
    'q1': {'d': 'q2'},
    'q2': {' ': 'q3'},
    'q3': {'v': 'q4'},
    'q4': {'e': 'q0'}
}

# Define the initial state
initial_state = 'q0'

# Define the set of accepting states
accepting_states = {'q2'}

# Function to check if a word is a regular verb
def is_regular_verb(word):
    current_state = initial_state

    for symbol in word:
        if symbol not in alphabet:
            raise ValueError(f"Invalid symbol '{symbol}' in input.")

        current_state = transitions.get(current_state, {}).get(symbol, current_state)

    return current_state in accepting_states

# Function to generate the past tense form of a regular verb
def generate_past_tense(word):
    return word + 'ed'

# Test sentences
sentences = ["She walked to the park yesterday", "He walks to the park every morning."]

for sentence in sentences:
    # Tokenize sentence into words
    words = re.findall(r'\b\w+\b', sentence)

    # Process each word
    for word in words:
        # Check if the word is a regular verb
        if is_regular_verb(word):
            # Generate the past tense form
            past_tense_form = generate_past_tense(word)
            print(f"Original: {word}, Past Tense: {past_tense_form}")
        else:
            print(f"Original: {word}, Past Tense: {word}")
