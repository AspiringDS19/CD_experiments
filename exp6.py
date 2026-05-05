def construct_ll1_table(grammar, first, follow):
    table = {}
    terminals = set()

    # Collect all terminals in the grammar
    for productions in grammar.values():
        for prod in productions:
            for char in prod:
                if char not in grammar and char != 'ε':
                    terminals.add(char)
    terminals.add('$')

    # Initialize the table
    for nt in grammar:
        table[nt] = {t: None for t in terminals}

    # Populate the table
    for nt, productions in grammar.items():
        for prod in productions:
            # 1. Find FIRST(prod)
            first_of_prod = set()
            if prod == 'ε':
                first_of_prod.add('ε')
            else:
                for char in prod:
                    if char not in grammar: # Terminal
                        first_of_prod.add(char)
                        break
                    first_of_prod.update(first[char] - {'ε'})
                    if 'ε' not in first[char]:
                        break
                else:
                    first_of_prod.add('ε')

            # 2. Apply rules to fill M[nt, terminal]
            for terminal in first_of_prod:
                if terminal != 'ε':
                    table[nt][terminal] = prod
            
            # 3. If ε is in FIRST(prod), use FOLLOW(nt)
            if 'ε' in first_of_prod:
                for terminal in follow[nt]:
                    table[nt][terminal] = prod

    return table, sorted(list(terminals))
