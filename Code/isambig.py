# Ambiguity :-> If two rewrite rules in a grammer arrive at the same string :>

def expand(tokens_and_derivation, grammer):
    (tokens, derivation) = tokens_and_derivation

    for token_pos in range(len(grammer)): # for each token
        for rule_index in range(len(grammer)): # for each rule
            rule = grammer[rule_index]
            if tokens[token_pos] == rule[0]:
                yield ((tokens[0:token_pos] + rule[1] + tokens[token_pos + 1]), derivation + [rule_index])

def isambig(grammer, start, utterance):
    enumerated = [([start], [])]
    
    while True:
        new_enumerated = enumerated

        for u in enumerated:
            for i in expand(u, grammer):

                # if anything new is found, which is not emunerated
                if not i in new_enumerated:
                    new_enumerated = new_enumerated + [i]

        # update the emunerated if new things were found in last cycle of expansion
        if new_enumerated != enumerated:
            enumerated = new_enumerated
        else:
            break

    # len of the list with same utterance will be > 1 if grammer is ambigious 
    return len([x for x in enumerated if x[0] == utterance]) > 1

# Test Cases

grammar1 = [ 
       ("S", [ "P", ]),
       ("S", [ "a", "Q", ]) ,
       ("P", [ "a", "T"]),
       ("P", [ "c" ]),
       ("Q", [ "b" ]),
       ("T", [ "b" ]),
       ] 
print isambig(grammar1, "S", ["a", "b"]) == True
print isambig(grammar1, "S", ["c"]) == False

grammar2 = [ 
       ("A", [ "B", ]),
       ("B", [ "C", ]),
       ("C", [ "D", ]),
       ("D", [ "E", ]),
       ("E", [ "F", ]),
       ("E", [ "G", ]),
       ("E", [ "x", "H", ]),
       ("F", [ "x", "H"]),
       ("G", [ "x", "H"]),
       ("H", [ "y", ]),
       ] 
print isambig(grammar2, "A", ["x", "y"]) == True
print isambig(grammar2, "E", ["y"]) == False

grammar3 = [ # Rivers in Kenya
       ("A", [ "B", "C"]),
       ("A", [ "D", ]),
       ("B", [ "Dawa", ]),
       ("C", [ "Gucha", ]),
       ("D", [ "B", "Gucha"]),
       ("A", [ "E", "Mbagathi"]),
       ("A", [ "F", "Nairobi"]),
       ("E", [ "Tsavo" ]),
       ("F", [ "Dawa", "Gucha" ])
       ] 
print isambig(grammar3, "A", ["Dawa", "Gucha"]) == True
print isambig(grammar3, "A", ["Dawa", "Gucha", "Nairobi"]) == False
print isambig(grammar3, "A", ["Tsavo"]) == False


