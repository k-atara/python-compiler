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
LiteralInt = '[1-9]*|0'            #Int, Float, "Complex" (imaginarios (j)) (sin simbolos)
LiteralFloat= '\d*\.\d*'
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

RegexTokens='\+=|\+|\-=|\->|\-|<<=|<=|<<|<|>>=|>=|>>|>|\*=|\*\*=|\*\*|\*|//=|/=|//|/|%=|%|@=|@|&=|&|\|=|\||\^=|\^|~|:=|:|!=|==|=|\(|\)|\[|\]|{|}|,|\.|;|\'|\"|\$|\`|\?'
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

def operadores(t):
    for clave in Operadores:
        valor = Operadores[clave] 
        if valor == t :
            return True
    return False

def operadoresName(t):
    for clave in Operadores:
        valor = Operadores[clave] 
        if valor == t :
            return clave
    return False

def delimitadores(t):
    for clave in Delimitadores:
        valor = Delimitadores[clave] 
        if valor == t :
            return True
    return False

def delimitadoresName(t):
    for clave in Delimitadores:
        valor = Delimitadores[clave] 
        if valor == t :
            return clave
    return False

def delimitadoresEspeciales(t):
    for clave in DelimitadoresEspeciales:
        valor = DelimitadoresEspeciales[clave] 
        if valor == t :
            return True
    return False

def delimitadoresEspecialesName(t):
    for clave in DelimitadoresEspeciales:
        valor = DelimitadoresEspeciales[clave] 
        if valor == t :
            return clave
    return False

def delimitadoresErrores(t):
    for clave in DelimitadoresError:
        valor = DelimitadoresError[clave] 
        if valor == t :
            return True
    return False

def delimitadoresErroresName(t):
    for clave in DelimitadoresError:
        valor = DelimitadoresError[clave] 
        if valor == t :
            return clave
    return False

#---------------------------------------------------------------------Recursion

def tokenizador(t):
    posComment=t.find("#")
    posEnter=t.find("\n")
    posEspacio=t.find(" ")
    txtString=re.findall(LiteralString,t)
    #x=re.compile('\".*\"|\'.*\'')
    # k=re.findall('\W' ,t)
    simbs=re.findall(RegexTokens,t)

    #print("t="+t)
    #print(txtString)
    #print(len(txtString))

#Comentarios
    if(posComment!=-1):
        if(posComment==0):
            t=t.replace('\n', '')
            #print("Comentario"+t)
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
    elif(len(txtString)>0):
        #print("ENTRE")
        x=re.compile(LiteralString)
        p=x.findall(t) #STRING
        #print(p)
        pExtra=re.compile(LiteralString).split(t)
        #print(pExtra) #RESTO DE LA LINEA
        for i in range(len(p)):
            listaTokens.append("String Literal -> "+p[i])

        if(len(pExtra)>0):
            for i in range(len(pExtra)):
                #lineas.append(pExtra[i])
                tokenizador(pExtra[i])

#Espacios 
    elif(posEspacio!=-1):
        listaP = t.split(" ")
        #print(listaP)
        for i in range(len(listaP)):
            tokenizador(listaP[i])

#------------------------------------------------SIN COMENTARIOS, SIN ENTERS, SIN ESPACIOS, SIN STRINGS LITERALS

#Encontrar símbolos
    elif(len(simbs)>0):
        #print("ENTRE")
        x=re.compile(RegexTokens)
        p=x.findall(t) #STRING
        #print(p)
        pExtra=re.compile(RegexTokens).split(t)
        #print(pExtra) #RESTO DE LA LINEA
        for i in range(len(p)):
            if operadores(p[i]):
                listaTokens.append(operadoresName(p[i])+" -> "+p[i])
            elif delimitadores(p[i]):
                listaTokens.append(delimitadoresName(p[i])+" -> "+p[i])
            elif delimitadoresEspeciales(p[i]):
                listaTokens.append(delimitadoresEspecialesName(p[i])+" -> "+p[i])
            elif delimitadoresErrores(p[i]):
                listaTokens.append(delimitadoresErroresName(p[i])+" -> "+p[i])
        if(len(pExtra)>0):
            for i in range(len(pExtra)):
                #lineas.append(pExtra[i])
                tokenizador(pExtra[i])
#Encontrar palabras clave
    elif(palabrasClave(t)):
        listaTokens.append(palabrasClaveName(t)+" -> "+t)
#ID's
    elif(t!=''):
        listaTokens.append("ID -> "+t)

#Análisis de cada línea
for i in range(len(lineas)):
    tokenizador(lineas[i])

#Lista de tokens
for k in range(len(listaTokens)):
    print(listaTokens[k])





























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











