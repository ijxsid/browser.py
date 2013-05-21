# Javascript Expression parser
# 
#       exp -> IDENTIFIER       # ("identifier",this_identifier_value)
#       exp -> NUMBER           # ("number",this_number_value)
#       exp -> STRING           # ("string",this_string_value) 
#       exp -> TRUE             # ("true","true") 
#       exp -> FALSE            # ("false","false") 
#
#
#       exp -> NOT exp          # ("not", child_parse_tree)
#       exp -> ( exp )          # child_parse_tree
#
#      exp ->   exp || exp        # lowest precedence, left associative
#           | exp && exp        # higher precedence, left associative 
#           | exp == exp        # higher precedence, left associative
#           | exp < exp         # /---
#           | exp > exp         # | higher precedence, 
#           | exp <= exp        # | left associative
#           | exp >= exp        # \---
#           | exp + exp         # /--- higher precedence,
#           | exp - exp         # \--- left associative
#           | exp * exp         # /--- higher precedence,
#           | exp / exp         # \--- left associative
#
# In each case, the parse tree is the tuple:
# 
#       ("binop", left_child, operator_token, right_child) 
#
# it is possible to have a function call as an expression:
#
#       exp -> IDENTIFIER ( optargs ) 
#
# The parse tree is the tuple ("call", function_name, arguments). 
#
#       optargs -> 
#       optargs -> args
#       args -> exp , args
#       args -> exp 
#
# It is also possible to have anonymous functions (sometimes called
# lambda expressions) in JavaScript. 
#
#       exp -> function ( optparams ) compoundstmt
#
# The names of our tokens: 
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

start = 'exp'   

precedence = (
         
        ('left', 'OROR'),
        ('left', 'ANDAND'),
        ('left', 'EQUALEQUAL'),
        ('left', 'LT', 'LE', 'GT', 'GE'),
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE','MOD')
        ('left', 'NOT')

) 

def p_exp_identifier(p): 
    'exp : IDENTIFIER'
    p[0] = ("identifier",p[1]) 
        
def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ('number',p[1])

def p_exp_string(p):
    'exp : STRING'
    p[0] = ('string',p[1])
    
def p_exp_true(p):
    'exp : TRUE'
    p[0] = ('true','true')
    
def p_exp_false(p):
    'exp : FALSE'
    p[0] = ('false','false')
    
def p_exp_not(p):
    'exp : NOT exp'
    p[0] = ('not', p[2])
    
def p_exp_parens(p):
    'exp : LPAREN exp RPAREN'
    p[0] = p[2]


def p_exp_lambda(p):
    'exp : FUNCTION LPAREN optparams RPAREN compoundstmt'  
    p[0] = ("function",p[3],p[5])

def p_exp_binop(p):
    '''exp : exp PLUS exp
            | exp MINUS exp
            | exp TIMES exp
            | exp MOD exp
            | exp DIVIDE exp
            | exp EQUALEQUAL exp
            | exp LE exp
            | exp LT exp
            | exp GE exp
            | exp GT exp
            | exp ANDAND exp
            | exp OROR exp '''

    p[0] = ("binop", p[1], p[2], p[3])

def p_exp_func_call(p):
    'exp : IDENTIFIER LPAREN optargs RPAREN'
    p[0] = ("func_call", p[1], p[3])

def p_optargs(p):
    'optargs : args'
    p[0] = p[1]

def p_optargs_empty(p):
    'optargs : '
    p[0] = []

def p_args(p):
    'args : exp COMMA args'
    p[0] = [p[1]] + p[3]

def p_args_one(p):
    'arg : exp'
    p[0] = [p[1]]













