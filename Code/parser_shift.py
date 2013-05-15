def shift (tokens, i, x, ab, cd, j):
    if cd != [] and tokens[i] == cd[0]:
        return (x, ab + [cd[0]], cd[1:] ,j)
    return None
    # Insert code here

    
print shift(["exp","+","exp"],2,"exp",["exp","+"],["exp"],0)
print shift(["exp","+","exp"],2,"exp",["exp","+"],["exp"],0) == ('exp', ['exp', '+', 'exp'], [], 0)
print shift(["exp","+","exp"],0,"exp",[],["exp","+","exp"],0) == ('exp', ['exp'], ['+', 'exp'], 0)
print shift(["exp","+","exp"],3,"exp",["exp","+","exp"],[],0) == None
print shift(["exp","+","ANDY LOVES COOKIES"],2,"exp",["exp","+"],["exp"],0) == None