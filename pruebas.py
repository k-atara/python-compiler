import re

# LiteralFloat= '^\d*\.\d*'
# LiteralInt = '^[1-9][0-9]*$'            #Int, Float, "Complex" (imaginarios (j)) (sin simbolos)
# t="v2v=2"

# numero = re.findall(LiteralInt,t)
# print(numero)

# x=re.compile(LiteralInt)

# p=x.findall(t) #STRING
# #print(p)
# pExtra=re.compile(LiteralInt).split(t)
# #print(pExtra) #RESTO DE LA LINEA

# print(p)
# print(pExtra)

# v2v=2

#47 simbolos
# r='\+=|\+|\-=|\->|\-|<<=|<=|<<|<|>>=|>=|>>|>|\*=|\*\*=|\*\*|\*|//=|/=|//|/|%=|%|@=|@|&=|&|\|=|\||\^=|\^|~|:=|:|!=|==|=|\(|\)|\[|\]|{|}|,|\.|;|\'|\"|\$|\`|\?'
# k=re.compile(r)
# t="+ += - -= < < <= <=+ +-= ** * // /%@ << >>&|^1~:=> > >===()[]{},::=.;===->>***=///=//=%=%@=&=|=^=>>=<<=**=***'\" \$ \`"

# Delimitadores = {'LPAR':'(','RPAR':')','LSQB':'[','RSQB':']','LBRACE':'{','RBRACE':'}','COMMA':',','COLON':':','DOT':'.',
#                  'SEMI':';','AT':'@','EQUAL':'=','RARROW':'->','PLUSEQUAL':'+=','MINEQUAL':'-=','STAREQUAL':'*=','SLASHEQUAL':'/=',
#                 'DOUBLESLASHEQUAL':'//=','PERCENTEQUAL':'%=','ATEQUAL':'@=','AMPEREQUAL':'&=','VBAREQUAL':'|=','CIRCUMFLEXEQUAL':'^=',
#                 'RIGHTSHIFTEQUAL':'>>=','LEFTSHIFTEQUAL':'<<=','DOUBLESTAREQUAL':'**='}

# Operadores = {'PLUS':'+','MINUS':'-','STAR':'*','DOUBLESTAR':'**','SLASH':'/','LDOUBLESLASH':'//','PERCENT':'%','AT':'@','LEFTSHIFT':'<<',
#               'RIGHTSHIFT':'>>','AMPER':'&','VBAR':'|','CIRCUMFLEX':'^','TILDE':'~','COLONEQUAL':':=','LESS':'<','GREATER':'>','LESSEQUAL':'<=',
#               'GREATEREQUAL':'>=','EQEQUAL':'==','NOTEQUAL':'!='}

# DelimitadoresEspeciales = {'CSIMPLE':'\'','CDOUBLE':'\"','HASHTAG':'#','RDOUBLESLASH':'\\','EMPTY':''}

# DelimitadoresError= {'ERRORA':'$','ERRORB':'?','ERRORC':'`'} 


# numero = re.findall(r,t)
# #print(numero)

# x=re.compile(r)

# p=x.findall(t) #STRING
# #print(p)
# pExtra=re.compile(r).split(t)
# #print(pExtra) #RESTO DE LA LINEA
# for i in range(len(p)):
#     for key in Delimitadores:
#         if(p[i]==Delimitadores[key]):
#             print("Caracter especial: Delimitador " + key + " -> "+ Delimitadores[key])
        
#     for key2 in Operadores:
#         if(p[i]==Operadores[key2]):
#             print("Caracter especial: Operador " + key2 + " -> "+ Operadores[key2])

#     for key3 in DelimitadoresEspeciales:
#         if(p[i]==DelimitadoresEspeciales[key3]):
#             print("Caracter especial: Delimitador especial " + key3 + " -> "+ DelimitadoresEspeciales[key3])

#     for key4 in DelimitadoresError:
#         if(p[i]==DelimitadoresError[key4]):
#             print("Caracter especial: Delimitador error " + key4 + " -> "+ DelimitadoresError[key4])




#print(p)
#print(pExtra)


LiteralInt = '[1-9]+0?|0'            
LiteralFloat= '\d*\.\d*'
t="12 45 963 03"
lista=[]

numeroI=re.findall(LiteralInt,t)

if(len(numeroI)>0):
    print(t)
    x=re.compile(LiteralInt)
    p=x.findall(t) #STRING
    # for i in range(len(p)):
    lista.append("INT -> "+p[i])



#
#
#
#
#
#
#
#
