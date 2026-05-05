class NFAState:
    def __init__(self, is_end=False):
        self.is_end = is_end
        self.transitions = {}  # char -> list of states
        self.epsilon_transitions = []

def create_basic_nfa(char):
    start = NFAState()
    end = NFAState(is_end=True)
    start.transitions[char] = [end]
    return start, end

def create_union_nfa(nfa1, nfa2):
    start = NFAState()
    end = NFAState(is_end=True)
    
    start.epsilon_transitions = [nfa1[0], nfa2[0]]
    nfa1[1].is_end = False
    nfa2[1].is_end = False
    nfa1[1].epsilon_transitions.append(end)
    nfa2[1].epsilon_transitions.append(end)
    
    return start, end

def create_star_nfa(nfa):
    start = NFAState()
    end = NFAState(is_end=True)
    
    start.epsilon_transitions = [nfa[0], end]
    nfa[1].is_end = False
    nfa[1].epsilon_transitions.extend([nfa[0], end])
    
    return start, end

def create_concat_nfa(nfa1, nfa2):
    nfa1[1].is_end = False
    nfa1[1].epsilon_transitions.append(nfa2[0])
    return nfa1[0], nfa2[1]
