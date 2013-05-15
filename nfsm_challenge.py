def nfsmaccepts(current, edges, accepting, visited):
    if current in visited:
        return None
    
    elif current in accepting:
        return ""

    else:
        new_visited = visited + [current]
        for edge in edges.keys():
            if edge[0] ==  current:
                for newstate in edges[edge]:
                    foo = nfsmaccepts( newstate, edges, accepting, new_visited)
                    if foo != None:
                        return edge[1] + foo

        return None 

def nfsmtrim(edges, accepting):

    # gather up all states
    states = []

    for e in edges:
        states = states + [e[0]] + edges[e]
    # find live states, A state is live if there is some 
    # way to accept starting from it.

    live = []
    for s in states:
        if nfsmaccepts( s, edges, accepting, []) != None:
            live  = live + [s]
    # Build up the output

    new_edges = {}
    for e in edges:
         
        if e[0] in live:
            new_destinations = []
            for destination in edges[e]:
                if destination in live:
                    new_destinations = new_destinations + [destination]
            if new_destinations != []:
                new_edges[e] = new_destinations
    new_accepting = []
    for s in accepting:
        if s in live:
            new_accepting = new_accepting + [s]

    return (new_edges, new_accepting)

edges1 = { (1,'a') : [1] ,
           (1,'b') : [2] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (8,'z') : [9] , } 
accepting1 = [ 1 ] 
(new_edges1, new_accepting1) = nfsmtrim(edges1,accepting1) 
print new_edges1
print new_edges1 == {(1, 'a'): [1]}
print new_accepting1 == [1] 
