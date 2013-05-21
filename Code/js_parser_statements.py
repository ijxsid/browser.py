# JavaScript Statements parser

#       js -> element js
#       js -> 
#
# An element is either a function declaration: 
#
#       element -> FUNCTION IDENTIFIER ( optparams ) compoundstmt
#
# or a statement following by a semi-colon: 
#
#       element -> stmt ; 
#       
# The parse tree for the former is the tuple ("function",name,args,body),
# the parse tree for the latter is the tuple ("stmt",stmt). 
#
#       optparams ->
#       optparams -> params
#       params -> IDENTIFIER , params
#       params -> IDENTIFIER
#
# optparams is a comma-separated list of zero or more identifiers. The
# parse tree for optparams is the list of all of the identifiers. 
#
#       compoundstmt -> { statements } 
#       statements -> stmt ; statements
#       statements -> 
#
# A compound statement is a list of zero or more statements, each of which
# is followed by a semicolon. (In real JavaScript, some statements do not
# need to be followed by a semicolon. For simplicity, we will assume that
# they all have to.) The parse tree for a compound statement is just the
# list of all of the statements. 
#
# We will consider six kinds of possible statements: 
#
#       stmt -> IF exp compoundstmt     
#       stmt -> IF exp compoundstmt ELSE compoundstmt
#       stmt -> IDENTIFIER = exp 
#       stmt -> RETURN exp 
#
# The "if", "assignment" and "return" statements should be familiar. It is
# also possible to use "var" statements in JavaScript to introduce new
# local variables (this is not necessary in Python): 
#
#       stmt -> VAR IDENTIFIER = exp 
#
# And it is also possible to treat an expression as a statement. This is
#
#       stmt -> exp 
#
# The parse trees for statements are all tuples:
#       ("if-then", conditional, then_branch)
#       ("if-then-else", conditional, then_branch, else_branch)
#       ("assign", identifier, new_value) 
#       ("return", expression)
#       ("var", identifier, initial_value) 
#       ("exp", expression)
#
#names of our tokens: 
#
# 'ANDAND',       # &&          | 'LT',           # <
# 'COMMA',        # ,           | 'MINUS',        # -
# 'DIVIDE',       # /           | 'NOT',          # !
# 'ELSE',         # else        | 'NUMBER',       # 1234 
# 'EQUAL',        # =           | 'OROR',         # ||
# 'EQUALEQUAL',   # ==          | 'PLUS',         # +
# 'FALSE',        # FALSE       | 'RBRACE',       # }
# 'FUNCTION',     # function    | 'RETURN',       # return
# 'GE',           # >=          | 'RPAREN',       # )
# 'GT',           # >           | 'SEMICOLON',    # ;
# 'IDENTIFIER',   # factorial   | 'STRING',       # "hello"
# 'IF',           # if          | 'TIMES',        # *
# 'LBRACE',       # {           | 'TRUE',         # TRUE
# 'LE',           # <=          | 'VAR',          # var 
# 'LPAREN',       # (           |
import ply.yacc as yacc
import ply.lex as lex
import jstokens                
from jstokens import tokens      

start = 'js'     
def p_js(p): 
        'js : element js'
        p[0] = [p[1]] + p[2]
def p_js_empty(p):
        'js : '
        p[0] = [ ]



#       element -> FUNCTION IDENTIFIER (optparams) compoundstmt
def p_element_function(p):
        'element : FUNCTION IDENTIFIER LPAREN optparams RPAREN compoundstmt'
        p[0] =  ("function", p[2],p[4],p[6])


#       element -> stmt ;

def p_element_stmt(p):
        'element : stmt SEMICOLON'
        p[0] = ("stmt", p[1])

#       optparams ->

def p_optparams_empty(p):
        'optparams : '
        p[0] = []

#       optparams -> params

def p_optparams(p):
        'optparams : params'
        p[0] = p[1]


#       params -> IDENTIFIER , params

def p_params(p):
        'params : IDENTIFIER COMMA params'
        p[0] = [p[1]] + p[3]

#       params -> IDENTIFIER

def p_params_one(p):
        'params : IDENTIFIER'
        p[0] = [p[1] ]


#       compoundstmt -> { statements }

def p_compound_stmt(p):
        'compoundstmt : LBRACE stmts RBRACE'
        p[0] = p[2]

#       statements -> stmt ; statements

def p_stmts(p):
        'stmts : stmt SEMICOLON stmts'
        p[0] = [p[1]] + p[3]

#       statements -> 

def p_stmts_empty(p):
        'stmts : '
        p[0] = [ ]

#       stmt -> IF exp compoundstmt

def p_stmt_if(p):
        'stmt : IF exp compoundstmt'
        p[0] = ("if-then", p[2], p[3])

#       stmt -> IF exp compoundstmt ELSE compoundstmt

def p_stmt_if_else(p):
        'stmt : IF exp compoundstmt ELSE compoundstmt'
        p[0] = ("if-then-else", p[2], p[3], p[5])

#       stmt -> IDENTIFIER = exp

def p_stmt_assignment(p):
        'stmt : IDENTIFIER EQUAL exp'
        p[0] = ("assign", p[1], p[3])

#       stmt -> RETURN exp

def p_stmt_return(p):
        'stmt :  RETURN exp'
        p[0] = ("return", p[2])

#       stmt -> VAR IDENTIFIER = exp 

def p_stmt_var(p):
        'stmt : VAR IDENTIFIER EQUAL exp'
        p[0] = ("var", p[2], p[4])

#       stmt -> exp 

def p_stmt_exp(p):
        'stmt : exp'
        p[0] =("exp", p[1])   





def p_exp_identifier(p): 
        'exp : IDENTIFIER'
        p[0] = ("identifier",p[1]) 

 