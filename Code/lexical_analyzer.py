import ply.lex as lex
tokens = ( #tokens we care about
    'LANGLE', # <
    'LANGLESLASH', #</
    'RANGLE', # >
    'EQUAL', # =
    'STRING',# "hello"
    'WORD', # Welcome
    'NUMBER' # 4556
    )

states   = (
    ('htmlcomment', 'exclusive'),
)

t_ignore = ' ' # shortcut for whitespace

def t_htmlcomment(token):
    r'<!--'
    token.lexer.begin('htmlcomment') # enter the commenting world

def t_htmlcomment_end(token):
    r'-->'
    
    # count the no. of newlines in the commenting section 
    # for line no. tracking purpose               
    token.lexer.lineno += token.value.count('\n')
    
    # return what we were doing before
    token.lexer.begin('INITIAL') 

def t_htmlcomment_error(token):
    # lot more like passing
    token.lexer.skip(1)

def t_newline(token):
    r'\n'
    token.lexer.lineno += 1
    pass

def t_LANGLESLASH(token):
    r'</'
    return token

def t_LANGLE(token):
    r'<'
    return token

def t_RANGLE(token):
    r'>'
    return token

def t_EQUAL(token):
    r'='
    return token

def t_STRING(token):
    r'"[^"\n]*"'
    token.value = token.value[1:-1]
    return token

def t_NUMBER(token):
    r'[0-9]+'
    token.value = int(token.value)
    return token

def t_WORD(token):
    r'[^ <>\n]+'
    return token



webpage = """This is <b>my </b> webpage <!-- It does<b>not suck </b> -->.
""" 
htmllexer = lex.lex()
htmllexer.input(webpage)
while True:
    tok = htmllexer.token()
    if not tok:break
    print tok
