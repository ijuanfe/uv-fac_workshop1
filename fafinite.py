class Automaton(object):

    def __init__(self, accepting_states, transitions):

        self.accepting_states = accepting_states
        self.transitions = transitions
        self.result = True # False: Recognized language is infinite, True: Recognized language is finite

    def reverse_routing(self, current_state, visited_states):

        if current_state in visited_states:
            self.result = False # If at least one loop is found (infinite language) then stop searching in this path
        else:
            for transition in self.transitions:
                next_state = transition[2]
                if current_state == next_state: # Can we get to current_state from some state?
                    previous_state = transition[0]
                    new_visited_states = visited_states + (next_state,)
                    self.reverse_routing(previous_state, new_visited_states)

    def is_finite(self):

        for transition in self.transitions:
            next_state = transition[2]
            if next_state in self.accepting_states:
                previous_state = transition[0]
                visited_states = (next_state,)
                self.reverse_routing(previous_state, visited_states)
                if self.result == False:
                    break

        print("Recognized language is finite") if self.result == True else print("Recognized language is infinite")

if __name__ == "__main__":

    # Automaton definition example:

    # 1. A finite set of input symbols (alphabet sigma): ["a", "b"]
    # - It does not have to be defined due to the proposed implementation

    # 2. A finite set of states: ["q0", "q1", "q2", "q3"]
    # - It does not have to be defined due to the proposed implementation

    # 3. An initial state: ["q0"]
    # - It does not have to be defined due to the proposed implementation

    # 4. A finite set of accepting states:
    # It does support multiple accepting states (e.g. accepting_states = ["q1", "q2", "q3"])
    accepting_states = ["q3"]

    # 5. A transition function:
    # - Input transition format: ("current_state", "transition_symbol", "next_state")
    # - Order between transitions does not matter due to the proposed implementation
    # - It does support Deterministic Finite Automaton (DFA) and Nondeterministic Finite Automaton (NFA)
    transitions = [
        ("q0", "a", "q1"),
        ("q0", "b", "q2"),
        ("q1", "a", "q2"),
        ("q1", "b", "q3"),
        ("q2", "a", "q3"),
        ("q2", "b", "q3"),
        ("q3", "a", "q3"),
        ("q3", "b", "q2")
    ]

    # Recognized language of the example: a(a(a+b)(a+ba+bb)*+b(a+ba+bb)*) + b(a+b)(a+ba+bb)*
    automaton = Automaton(accepting_states, transitions)
    automaton.is_finite()
