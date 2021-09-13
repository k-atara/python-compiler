import sys
import re

lineas = []
nom_archivo = sys.argv[1]

# Leer el archivo y separarlos por TABS
for line in open(nom_archivo, 'r'):
    for num in line.split("\t"):
        lineas.append(num)
print(lineas)

# for j in range(len(lineas)):
#     words = lineas[j].split(" ")
#     for k in range(len(words)): 
#         palabras.append(words[k])

#print(palabras)

#---------------------ESTRUCTURA DE LINEA
Indent=('   ')

#---------------------ID's Y PALABRAS CLAVE

#Palabras clave / KEYWORDS
PalabrasClave = {'FALSE':'False','NONE':'None','TRUE':'True','AND':'and','AS':'as','ASSERT':'assert','ASYNC':'async','AWAIT':'await','BREAK':'break',
                 'CLASS':'class','CONTINUE':'continue','DEF':'def','DEL':'del','ELIF':'elif','ELSE':'else','EXCEPT':'except','FINALLY':'finally',
                 'FOR':'for','FROM':'from','GLOBAL':'global','IF':'if','IMPORT':'import','IN':'in','IS':'is','LAMBDA':'lambda','NONLOCAL':'nonlocal',
                 'NOT':'not','OR':'or','PASS':'pass','RAISE':'raise','RETURN':'return','TRY':'try','WHILE':'while','WITH':'with','YIELD':'yield'}

#Identificadores
Identificadores = '[a-zA-Z_][a-zA-Z0-9_]*'
#las letras mayúsculas y minúsculas A hasta Z, el guión bajo _ y los dígitos 0 hasta 9, salvo el primer carácter. Case sensitive

#Literales
LiteralString = '\".*\"|\'.*\''             #Literales cerrados en comillas simples o dobles (hasta triples...)
LiteralNumerical = []            #Int, Float, "Complex" (imaginarios (j)) (sin simbolos)
LiteralBoolean = [PalabrasClave['TRUE'],PalabrasClave['FALSE']] #PalabrasClave [True,False]
LiteralSpecial = [PalabrasClave['NONE']] #PalabrasClave [None]
LiteralEscape = ['\n']                  #Enter


#Operadores
Operadores = {'PLUS':'+','MINUS':'-','STAR':'*','DOUBLESTAR':'**','SLASH':'/','LDOUBLESLASH':'//','PERCENT':'%','AT':'@','LEFTSHIFT':'<<',
              'RIGHTSHIFT':'>>','AMPER':'&','VBAR':'|','CIRCUMFLEX':'^','TILDE':'~','COLONEQUAL':':=','LESS':'<','GREATER':'>','LESSEQUAL':'<=',
              'GREATEREQUAL':'>=','EQEQUAL':'==','NOTEQUAL':'!='}

Delimitadores = {'LPAR':'(','RPAR':')','LSQB':'[','RSQB':']','LBRACE':'{','RBRACE':'}','COMMA':',','COLON':':','DOT':'.',
                 'SEMI':';','AT':'@','EQUAL':'=','RARROW':'->','PLUSEQUAL':'+=','MINEQUAL':'-=','STAREQUAL':'*=','SLASHEQUAL':'/=',
                'DOUBLESLASHEQUAL':'//=','PERCENTEQUAL':'%=','ATEQUAL':'@=','AMPEREQUAL':'&=','VBAREQUAL':'|=','CIRCUMFLEXEQUAL':'^=',
                'RIGHTSHIFTEQUAL':'>>=','LEFTSHIFTEQUAL':'<<=','DOUBLESTAREQUAL':'**='}

DelimitadoresEspeciales = {'CSIMPLE':'\'','CDOUBLE':'\"','HASHTAG':'#','RDOUBLESLASH':'\\','EMPTY':''} #EMPTY SE GENERA CUANDO HAY UN SALTO DE LINEA DE FORMA AUTOMATICA
#El simbolo de hashtag se usa de comentario
#El simbolo de comilla doble o simple se usa para hacer strings

#---------------------------------------------------------------------------------------------------------------------------------------------
DelimitadoresError= {'ERRORA':'$','ERRORB':'?','ERRORC':'`'} #Son errores si están afuera de un string

#------------------------------------------------------------------------------ARREGLO DE TOKENS
listaTokens=[]
#------------------------------------------------------------------------------

def palabrasClave(t):
    for clave in PalabrasClave:
        valor = PalabrasClave[clave] 
        if valor == t :
            return True
    return False

def palabrasClaveName(t):
    for clave in PalabrasClave:
        valor = PalabrasClave[clave] 
        if valor == t :
            return clave
    return False

def delimitadoresEspecialesName(t):
    for clave in DelimitadoresEspeciales:
        valor = DelimitadoresEspeciales[clave] 
        if valor == t :
            return clave
    return False

#---------------------------------------------------------------------Recursion


def tokenizador(t):
    posComment=t.find("#")
    posEnter=t.find("\n")
    posEspacio=t.find(" ")
    txtString=re.fullmatch(LiteralString,t)
    #print("t="+t)
#Comentarios
    if(posComment!=-1):
        if(posComment==0):
            t=t.replace('\n', '')
            print("Comentario"+t)
            listaTokens.append("Comentario -> "+t)
        else:
            l,r=t[:posComment],t[posComment:]
            r=r.replace('\n', '')
            listaTokens.append("Comentario -> "+r)
            tokenizador(l)
#Enters
    elif(posEnter!=-1):
        l,r=t[:posEnter],t[posEnter:]
        listaTokens.append("Enter -> \\n")
        tokenizador(l)
#Strings 
    elif(bool(txtString)): 
        listaTokens.append(delimitadoresEspecialesName(t[0])+" -> "+t[0])
        listaTokens.append("String -> "+t[1:len(t)-1])
        listaTokens.append(delimitadoresEspecialesName(t[len(t)-1])+" -> "+t[len(t)-1])
#Espacios 
    elif(posEspacio!=-1):
        listaP = t.split(" ")
        #print(listaP)
        for i in range(len(listaP)):
            tokenizador(listaP[i])
#Encontrar palabras clave
    elif(palabrasClave(t)):
        listaTokens.append(palabrasClaveName(t)+" -> "+t)
    elif(t!=''):
        listaTokens.append("ID -> "+t)
#Encontrar símbolos
    #for j in range(len(PalabrasClave)):

for i in range(len(lineas)):
    tokenizador(lineas[i])

print(listaTokens)

for k in range(len(listaTokens)):
    print(listaTokens[k])

#Análisis de cada token



"""
#Paso 0: Remove Comentarios #
palabrasFinalesSinComent=[]
for j in range(len(lineas)):
    c1= palabras[j].find(DelimitadoresEspeciales['HASHTAG'])
    print(c1)


#Paso 1: Enters
for linea in lineas:
    if(LiteralEscape[0] in linea):
        #print("Encontro Enter")
        pos=linea.find('\n')
        palabras.append(linea[0:pos])
        palabras.append(linea[pos:len(linea)])
    else:
        palabras.append(linea)

print(palabras)

#Paso 2: Remove TABS y espacios
for j in range(len(palabras)):
    #print("Encontro tab/espacio")
    palabra=palabras[j].replace('   ',' ')
    palabras[j]=palabra

palabrasFinales=[]
for j in range(len(palabras)):
    words = palabras[j].split(" ")
    for k in range(len(words)): 
        palabrasFinales.append(words[k])

print(palabrasFinales)

#----------------------------------------------------------------

#PASO 3: EMPIEZA EL ANALISIS

def tokenId(t):
    verId=re.fullmatch(Identificadores,t)   
    #print(verId)
    if verId:
        return True
    else:
        return False

def comment(t):
    verId=re.fullmatch(Identificadores,t)
    #print(verId)
    if verId:
        return True
    else:
        return False       


for i in range(len(palabrasFinales)):
    if(tokenId(palabrasFinales[i])==True):
        print(palabrasFinales[i])
        print(palabrasFinales[i]+": IDENTIFICADOR")

"""











