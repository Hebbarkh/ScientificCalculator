import ply.yacc as yacc
import ply.lex as lex
import calc2
import sys
import math
tokens=calc2.tokens
names={}
precedence = (
        ('left', 'PLUS', 'MINUS'),
        ('left', 'TIMES', 'DIVIDE'))

def p_statement_assign(p):
	'''assign : NAME EQUALS expression
	| statement'''
	try:
	   names[p[1]] = p[3]
	   print "\n"
    	except:
    		pass
    		
def p_statement_expr(p):
        '''statement : expression
		| BREAK 
		| EXIT
		| QUIT
	'''
	if p[1]=="exit" or p[1]=="quit" or p[1]=="break":
        	sys.exit()
        print p[1],'\n'

        
def p_exprr(p):
	'''
	expression : SUM expression expression
	    |  DIFFERENCE expression expression
	    |  PRODUCT expression expression
	    |  QUOTIENT expression expression	
	'''    
	if p[1] == 'sum':
            p[0] = p[2] + p[3]
        elif p[1] == 'difference':
            p[0] = p[2] - p[3]
        elif p[1] == 'product':
            p[0] = p[2] * p[3]
        elif p[1] == 'quotient':
            p[0] = p[2] / p[3]
            
def p_expression_binop(p):
        """
        expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression OR expression
                  | expression AND expression
                  | expression XOR expression
        """
        if p[2] == '+' or p[2]=='plus':
            p[0] = p[1] + p[3]
        elif p[2] == '-' or p[2]=='minus':
            p[0] = p[1] - p[3]
        elif p[2] == '*' or p[2]=='times':
            p[0] = p[1] * p[3]
        elif p[2] == '/' or p[2]=='by':
            p[0] = p[1] / p[3]
        elif p[2] == 'logical or' or p[2]=='|' or p[2]=='OR':
        	try:
        		p[0] = p[1] | p[3]
        	except TypeError as e:print e
        elif p[2]=='logical and' or p[2]=='&' or p[2] == 'AND':
        	try:
        		p[0] = p[1] & p[3]
        	except TypeError as e:print e
        elif p[2] == 'xor' or p[2]=='XOR':
		try:
        		p[0]= p[1]^p[3]
        	except TypeError as e:print e
        	
def p_factor(p):
	'''expression : INT
		| FLOAT'''
	p[0]=p[1]

def p_paran(p):
	'''expression : OPAR expression CPAR'''
	p[0]=p[2]

def p_logical_not(p):
	'''expression : NOT expression'''
	p[0] = ~p[2]
	
def p_factorial_exp(p):
	'''expression : expression FACTORIAL
	| FACTORIAL expression
	'''
	try:
		p[0] = math.factorial(p[3])
	except IndexError:
		try:
			p[0] = math.factorial(p[1])
		except TypeError:
			try:p[0]=math.factorial(p[2])
			except ValueError as e:print e,'\n'
		except ValueError as e:print e,'\n'
	except ValueError as e:print e,'\n'
	
def p_logarithms(p):
	'''expression : LOG expression
	| LN expression
	'''
	try:
		if p[1]=='log':
			try:
				p[0] = math.log10(p[3])
			except IndexError:
				p[0] = math.log10(p[2])
		elif p[1] == 'ln':
			try:
				p[0] = math.log(p[3])
			except IndexError:
				p[0] = math.log(p[2])
	except ValueError:
		print "Math domain error\n"
			
def p_pival(p):
	'''expression : PI
	| NAME'''
	if p[1] == 'pi':
		p[0] = math.pi
	else:
		p[0] = names.get(p[1],0)
		
def p_uniminus(p):
	'''expression : MINUS expression'''
	p[0] = -p[2]

def p_square_fun(p):
	'''expression : expression SQUARE
	| SQUARE expression
	'''
	if p[1] == 'square':
		p[0] = p[2] ** 2
	else:
		p[0] = p[1] ** 2
		
def p_square_root(p):
	'''expression : SQROOT expression'''
	p[0] = math.sqrt(p[2])
		
def p_math_fun(p):
	'''expression : function1'''
	p[0] = p[1]
	
def p_math_pow(p):
	'''expression : POWER OPAR expression expression CPAR'''
	a1 = p[3]
	a2 = p[4]
	p[0] = a1**a2
		
def p_trig_func1(p):
	'''function1 : SIN expression
	| COS expression
	| TAN expression
	| COT expression
	| SEC expression
	| COSEC expression
	| COS expression RAD
	| TAN expression RAD
	| COT expression RAD
	| SEC expression RAD
	| COSEC expression RAD
	| SIN expression RAD
	'''
	if p[1] == 'sin':
		p[0] = math.sin(p[2])
	elif p[1] == 'cos':
		p[0] = math.cos(p[2])
	elif p[1] == 'tan':
		p[0] = math.tan(p[2])
	elif p[1] == 'cot':
		p[0] = 1.0/math.tan(p[2])
	elif p[1] == 'sec':
		p[0] = 1.0/math.cos(p[2])
	elif p[1] == 'cosec':
		p[0] = 1.0/math.sin(p[2])


		
def p_func1(p):
	'''function1 : SIN expression DEGREE
	| COS expression DEGREE
	| TAN expression DEGREE
	| COT expression DEGREE
	| SEC expression DEGREE
	| COSEC expression DEGREE
	'''
	if p[1] == 'sin':
		p[0] = math.sin(p[2]*math.pi/180)
	elif p[1] == 'cos':
		p[0] = math.cos(p[2]*math.pi/180)
	elif p[1] == 'tan':
		p[0] = math.tan(p[2]*math.pi/180)
	elif p[1] == 'cot':
		p[0] = 1.0/math.tan(p[2]*math.pi/180)
	elif p[1] == 'sec':
		p[0] = 1.0/math.cos(p[2]*math.pi/180)
	elif p[1] == 'cosec':
		p[0] = 1.0/math.sin(p[2]*math.pi/180)

def p_registers(p):
	'expression : REGISTERS'
	for x in ['A','B','C','D']:
		print x,'=',names.get(x,0)	
			
def p_error(p):
	print "Error!!!"
	
yacc.yacc()
print "Available registers are A,B,C,D"
while(True):
	data=raw_input("calc>")
	yacc.parse(data)
		
