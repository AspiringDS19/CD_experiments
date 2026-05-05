import collections

class NFAtoDFA:
    def __init__(self, nfa_states, alphabet, transitions, start_state, accept_states):
        self.nfa_states = nfa_states
        self.alphabet = alphabet
        self.transitions = transitions  # Format: {(state, char): [next_states]}
        self.start_state = start_state
        self.accept_states = accept_states

    def get_epsilon_closure(self, states):
        stack = list(states)
        closure = set(states)
        while stack:
            u = stack.pop()
            # Assuming 'ε' represents epsilon transition
            for v in self.transitions.get((u, 'ε'), []):
                if v not in closure:
                    closure.add(v)
                    stack.append(v)
        return tuple(sorted(list(closure)))

    def move(self, states, char):
        next_states = set()
        for s in states:
            for ns in self.transitions.get((s, char), []):
                next_states.add(ns)
        return next_states

    def convert(self):
        start_closure = self.get_epsilon_closure([self.start_state])
        dfa_states = [start_closure]
        dfa_transitions = {}
        unprocessed = collections.deque([start_closure])
        
        dfa_accept_states = []

        while unprocessed:
            current_dfa_state = unprocessed.popleft()
            
            # Check if this set contains an NFA accept state
            if any(s in self.accept_states for s in current_dfa_state):
                dfa_accept_states.append(current_dfa_state)

            for char in self.alphabet:
                # 1. Move
                move_result = self.move(current_dfa_state, char)
                # 2. Closure
                closure_result = self.get_epsilon_closure(move_result)
                
                if not closure_result:
                    continue
                
                if closure_result not in dfa_states:
                    dfa_states.append(closure_result)
                    unprocessed.append(closure_result)
                
                dfa_transitions[(current_dfa_state, char)] = closure_result

        return dfa_states, dfa_transitions, dfa_accept_states
