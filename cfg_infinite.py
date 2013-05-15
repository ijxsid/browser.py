#Infinite Grammers

#Important Assumption: For this problem, you may assume that for every
# non-terminal in the grammar, that non-terminal derives at least one
# non-empty finite string.  (You could just call cfgempty() from before to
# determine this, so we'll assume it.)  

def cfginfinite(grammer):
    for Q in [ rule[0] for rule in grammer ]:
        #See if Q can be written as x Q y, where |x+y| > 0

        def helper(current, visited, sizexy):
            """ Local function inside a function, can be used only inside this
                function.

                Returns true if :

            """

            if current in visited:
                return sizexy > 0
            else:
                new_visited   = visited + [current]

                for rhs in [rule[1] for rule in grammer if rule[0] == current]:
                    
                    for symbol in rhs:
                        # 3rd argument to the helper  => sizexy + len(rhs) -1 
                        # coz 1 is length of the symbol which is being checked. 

                        if helper( symbol, new_visited, sizexy + len(rhs) - 1 ):
                            return True
                return False

        if helper(Q, [], 0):
            return True
    return False

# Test Cases

grammar1 = [ 
      ("S", [ "S", "a" ]), # S -> S a
      ("S", [ "b", ]) , # S -> b 
      ] 
print cfginfinite(grammar1) == True

grammar2 = [ 
      ("S", [ "S", ]), # S -> S 
      ("S", [ "b", ]) , # S -> b 
      ] 

print cfginfinite(grammar2) == False

grammar3 = [ 
      ("S", [ "Q", ]), # S -> Q
      ("Q", [ "b", ]) , # Q -> b
      ("Q", [ "R", "a" ]), # Q -> R a 
      ("R", [ "Q"]), # R -> Q
      ] 

print cfginfinite(grammar3) == True

grammar4 = [  # Nobel Peace Prizes, 1990-1993
      ("S", [ "Q", ]),
      ("Q", [ "Mikhail Gorbachev", ]) ,
      ("Q", [ "P", "Aung San Suu Kyi" ]),
      ("R", [ "Q"]),
      ("R", [ "Rigoberta Tum"]),
      ("P", [ "Mandela and de Klerk"]),
      ] 

print cfginfinite(grammar4) == False
