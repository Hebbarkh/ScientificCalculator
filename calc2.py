import ply.lex as lex

tokens = [ 'NAME','INT','FLOAT','PLUS','MINUS','TIMES','DIVIDE','EQUALS','SIN','COS','TAN','COT','SEC','COSEC','OPAR','CPAR','AND','OR','XOR',
'NOT','QUIT','EXIT','BREAK','SUM','DIFFERENCE','PRODUCT','QUOTIENT','LOG','LN','FACTORIAL','PI','SQUARE','SQROOT','REGISTERS',
'RAD','POWER','DEGREE','WORD' ]

t_NAME = 'A|B|C|D'
t_ignore = ' \t'
t_PLUS = r'\+|plus'
t_MINUS = r'-|minus'
t_TIMES = r'\*|times'
t_DIVIDE = r'/|by'
t_EQUALS = r'='
t_SIN = r'sin'
t_COS = r'cosine|cos'
t_TAN = r'tan|tangent'
t_COT = r'cot|cotangent'
t_SEC = r'sec|secent'
t_COSEC = r'cosec|cosecent'
t_OPAR = r'\('
t_CPAR = r'\)'
t_AND = r'logical\ and|&|AND'
t_OR = r'logical\ or|\||OR'
t_NOT = r'NOT'
t_XOR = r'xor|XOR'
t_BREAK = r'break'
t_QUIT = r'quit'
t_EXIT = r'exit'
t_SUM = 'sum|add'
t_RAD = 'radian|radians'
t_DIFFERENCE = 'difference|subtract'
t_PRODUCT = 'product|multiply'
t_QUOTIENT = 'quotient|divide'
t_LOG = r'log'
t_LN = r'ln'
t_FACTORIAL = r'factorial'
t_PI = r'pi'
t_SQUARE = r'square'
t_POWER = r'power'
t_SQROOT = r'square\ root|root|squareroot'
t_REGISTERS = r'registers?'
t_DEGREE = r'degrees?'


def t_WORD(t):
	r'what|whats|is|the|find|me|of|calculate|tell|do\ you\ know|and|value|,|What|Whats|Find|Calculate|Tell|And|Value'
	pass

def t_FLOAT(t):
	r'[0-9]*\.[0-9]+'
	t.value = float(t.value)
	return t

def t_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print ' Undefined character ',t.value
	t.lexer.skip(len(t.value))

lex.lex()

