import ply.lex as lex
import ply.yacc as yacc

tokens = ('STAR', 'EQUALS', 'ID')

# Tokens
t_STAR = r'\*'
t_EQUALS = r'='
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_error(t):
  print(f"Illegal character {t.value[0]!r}")
  t.lexer.skip(1)

# Criando o analisador lexico
lex.lex()

def p_s(p):
  '''s : l EQUALS r
       | r'''

def p_l(p):
  '''l : STAR r
      | ID'''

def p_r(p):
  'r : l'

def p_error(p):
  print(f"Syntax error at {p.value!r}")

# Criando o analisador sintatico
yacc.yacc(debug=True, method="LALR")
# yacc.yacc(debug=True, method="SLR")

while True:
  try:
    s = input('Entrada: ')
  except EOFError:
    break

  yacc.parse(s)