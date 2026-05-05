import re

# Define token categories using Regular Expressions
TOKEN_PATTERNS = [
    ('KEYWORD',    r'\b(if|else|while|for|int|float|return|print)\b'),
    ('ID',         r'[a-zA-Z_][a-zA-Z0-9_]*'),      # Identifiers
    ('NUMBER',     r'\d+(\.\d+)?'),                 # Integer or Decimal
    ('ASSIGN',     r'='),                           # Assignment
    ('OP',         r'[+\-*/]'),                     # Arithmetic Operators
    ('COMP',       r'==|!=|<=|>=|<|>'),             # Comparison Operators
    ('SEP',        r'[;,\(\){}]'),                  # Separators
    ('WHITESPACE', r'\s+'),                         # Skip spaces/tabs
]
def lexical_analyzer(code):
    tokens = []
    master_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_PATTERNS)
    
    for match in re.finditer(master_pattern, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'WHITESPACE':
            tokens.append((token_type, token_value))
            
    return tokens
