import sys
import re

lineas = []
nom_archivo = sys.argv[1]
palabras=[]
rPrueba='\+=|\+|\-=|\->|\-|<<=|<=|<<|<|>>=|>=|>>|>|\*=|\*\*=|\*\*|\*|//=|/=|//|/|%=|%|@=|@|&=|&|\|=|\||\^=|\^|~|:=|:|!=|==|=|\(|\)|\[|\]|{|}|,|\.|;|\$|\`|\?|\n'
LiteralString = '\"[^[\"]+\"|\'[^[\']+\''             #Literales cerrados en comillas simples o dobles (hasta triples...)
LiteralInt = '^[1-9]+[0-9]*$|^[0]*0$'            #Int, Float, "Complex" (imaginarios (j)) (sin simbolos)
LiteralFloat= '\d+\.\d+|\.\d+|\d+\.'
Octal = '0o[0-7]+'
Hexa = '0x[0-9A-F]+'
Bi = '0b[0-1]+'
Identificadores = '[a-zA-Z_][a-zA-Z0-9_]*'

rFinal='#.*|\+=|\+|\-=|\->|\-|<<=|<=|<<|<|>>=|>=|>>|>|\*=|\*\*=|\*\*|\*|//=|/=|//|/|%=|%|@=|@|&=|&|\|=|\||\^=|\^|~|:=|:|!=|==|=|\(|\)|\[|\]|{|}|,|\.|;|\$|\`|\?|\n|\"[^[\"]+\"|\'[^[\']+\'|^[1-9]+[0-9]*$|^[0]*0$ |\d+\.\d+|\.\d+|\d+\. |[a-zA-Z_][a-zA-Z0-9_]*|0b[0-1]+ |0x[0-9A-F]+|0o[0-7]+'

# Leer el archivo y separarlos por TABS
for line in open(nom_archivo, 'r'):
    for num in line.split("\t"):
        lineas.append(num)

for i in range(len(lineas)):
    lista=re.findall(rFinal,lineas[i])
    print(lista)



    # lista=re.findall(rPrueba,lineas[i])
    # print(lista)
    # x=re.compile(rPrueba)
    # p=x.findall(lineas[i]) #STRING
    # pExtra=re.compile(rPrueba).split(lineas[i])

    # print(p)
    # print(pExtra)

    # for i in range(len(p)):
    #     listaTokens.append(p[i]+" -> String Literal")

    # if(len(pExtra)>0):
    #     for i in range(len(pExtra)):
    #         if(pExtra!=''):
    #             tokenizador(pExtra[i])