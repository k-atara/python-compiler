import sys
import re

lineas = []
nom_archivo = sys.argv[1]
palabras=[]

# Leer el archivo y separarlos por TABS
for line in open(nom_archivo, 'r'):
    for num in line.split("\t"):
        lineas.append(num)

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
LiteralString = '\"[^[\"]+\"|\'[^[\']+\''             #Literales cerrados en comillas simples o dobles (hasta triples...)
LiteralInt = '^[1-9]+[0-9]*|0$'            #Int, Float, "Complex" (imaginarios (j)) (sin simbolos)
LiteralFloat= '\d+\.\d+|\.\d+|\d+\.'
LiteralEscape = ['\n']                  #Enter 
Octal = '0o[0-7]+'
Hexa = '0x[0-9A-F]+'
Bi = '0b[0-1]+'

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
    simbs=re.findall(RegexTokens,t)
    numeroI=re.findall(LiteralInt,t)
    numeroF=re.findall(LiteralFloat,t)
    id=re.fullmatch(Identificadores,t)
    
#Espacios 
    if(posEspacio!=-1 and len(txtString)<=0 and posComment==-1):
        listaP = t.split(" ")
        for i in range(len(listaP)):
            if(listaP[i]!=''):
                tokenizador(listaP[i])
#Comentarios
    elif(posComment!=-1):
        if(posComment==0):
            t=t.replace('\n', '')
            listaTokens.append(t+" -> Comentario")
        else:
            l,r=t[:posComment],t[posComment:]
            r=r.replace('\n', '')
            listaTokens.append(r+" -> Comentario")
            if(l!=''):
                tokenizador(l)
#Enters
    elif(posEnter!=-1):
        l,r=t[:posEnter],t[posEnter:]
        listaTokens.append("\\n -> Enter")
        if(l!=''):
            tokenizador(l)
#Strings 
    elif(len(txtString)>0):
        x=re.compile(LiteralString)
        p=x.findall(t) #STRING
        pExtra=re.compile(LiteralString).split(t)
        for i in range(len(p)):
            listaTokens.append(p[i]+" -> String Literal")

        if(len(pExtra)>0):
            for i in range(len(pExtra)):
                if(pExtra!=''):
                    tokenizador(pExtra[i])

#------------------------------------------------SIN COMENTARIOS, SIN ENTERS, SIN ESPACIOS, SIN STRINGS LITERALS
#Float
    elif(len(numeroF)>0):
        x=re.compile(LiteralFloat)
        p=x.findall(t) #STRING

        pExtra=re.compile(LiteralFloat).split(t)

        for i in range(len(p)):
            listaTokens.append(p[i]+" -> Literal Float")
        if(len(pExtra)>0):
            for i in range(len(pExtra)):
                if(pExtra!=''):
                    tokenizador(pExtra[i])
#Int
    elif(len(numeroI)>0):
        x=re.compile(LiteralInt)
        p=x.findall(t) #STRING

        pExtra=re.compile(LiteralInt).split(t)

        for i in range(len(p)):
            listaTokens.append(p[i]+" -> Literal Int")

        if(len(pExtra)>0):
            for i in range(len(pExtra)):
                if(pExtra!=''):
                    tokenizador(pExtra[i])    
#Encontrar símbolos
    elif(len(simbs)>0):
        x=re.compile(RegexTokens)
        p=x.findall(t) #STRING
        pExtra=re.compile(RegexTokens).split(t)
        for i in range(len(p)):
            if operadores(p[i]):
                listaTokens.append(p[i]+" -> "+operadoresName(p[i]))
            elif delimitadores(p[i]):
                listaTokens.append(p[i]+" -> "+delimitadoresName(p[i]))
            elif delimitadoresEspeciales(p[i]):
                listaTokens.append(p[i]+" -> "+delimitadoresEspecialesName(p[i]))
            elif delimitadoresErrores(p[i]):
                listaTokens.append(p[i]+" -> "+delimitadoresErroresName(p[i]))
        
        if(len(pExtra)>0):
            for i in range(len(pExtra)):
                if(pExtra!=''):
                    tokenizador(pExtra[i])
#Encontrar palabras clave
    elif(palabrasClave(t)):
        listaTokens.append(t+" -> "+palabrasClaveName(t))
    elif(re.fullmatch(Octal,t)):
        listaTokens.append(t+" -> Octal number")
    elif(re.fullmatch(Hexa,t)):
        listaTokens.append(t+" -> Hexadecimal number")
    elif(re.fullmatch(Bi,t)):
        listaTokens.append(t+" -> Binary number")
#ID's
    elif(t!='' and bool(id)):
        listaTokens.append(t+" -> ID")
#ID's
    elif(t!=''):
        listaTokens.append(t+" -> No identificado como parte de la gramática")

#---------------------------------------------------------------------Fin recursion

#Análisis de cada línea
for i in range(len(lineas)):
    tokenizador(lineas[i])
    
#----------------------------------------------------------------------Impresión de la lista de tokens
for k in range(len(listaTokens)):
    print(listaTokens[k])