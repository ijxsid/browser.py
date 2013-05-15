def reductions(chart, i, x, ab, cd, j):
    return [ (jstate[0], jstate[1] +[x], (jstate[2])[1:], jstate[3]) for jstate in chart[j] if cd== [] and jstate[2] != [] and jstate[2][0] == x ]
    
    
    
chart = {0: [('exp', ['exp'], ['+', 'exp'], 0), ('exp', [], ['num'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['exp', '+', 'exp'], 0)], 1: [('exp', ['exp', '+'], ['exp'], 0)], 2: [('exp', ['exp', '+', 'exp'], [], 0)]}

print reductions(chart,2,'exp',['exp','+','exp'],[],0) == [('exp', ['exp'], ['-', 'exp'], 0), ('exp', ['exp'], ['+', 'exp'], 0)]