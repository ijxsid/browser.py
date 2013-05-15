# Empty Grammer


def cfgempty(grammer, symbol, visited):
    """ Function to check whether a context-free grammer is Empty
        
        grammer format is 
        grammer = [
        (lhs_of_rule, (symbols in rhs_of_rule))
        ....more rules]
        
        symbols is non-terminal if it exists in lhs of atleast 1 rule.

        visited contains the list of already visited non-terminal symbols.

        Returns None if context-free grammer is Empty, otherwise 
        returns a string proving that context-free grammer is non-empty..

    """

    if symbol in visited:
        #Saving us from infinite loops
        return None

    elif not any([rule[0] == symbol for rule in grammer]):
        # return symbols if it is terminal
        return [symbol]

    else:

        #update visited
        new_visited = visited + [symbol]

        #consider every rewrite rule "Symbol -> RHS"
        for rhs in [r[1] for r in grammer if r[0] == symbol]:

            #check if every part of RHS is non-empty
            if all([None!= cfgempty(grammer, r, new_visited) for r in rhs]):

                #gather up all results
                result = []
                for r in rhs:
                    result = result + cfgempty(grammer, r, new_visited)
                return result 
    return None 
