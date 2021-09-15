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

r='\+=|\+|\-=|\->|\-|<<=|<=|<<|<|>>=|>=|>>|>|\*=|\*\*=|\*\*|\*|//=|/=|//|/|%=|%|@=|@|&=|&|\|=|\||\^=|\^|~|:=|:|!=|==|=|\(|\)|\[|\]|{|}|,|\.|;|\'|\"'
k=re.compile(r)
t="+ += - -= < < <= <=+ +-= ** * // /%@ << >>&|^1~:=> > >===()[]{},::=.;===->>***=///=//=%=%@=&=|=^=>>=<<=**=***'\""

"""
+
+=
-
-=
<
<
<=
+
+
-=
"""

numero = re.findall(r,t)
#print(numero)

x=re.compile(r)

p=x.findall(t) #STRING
#print(p)
pExtra=re.compile(r).split(t)
#print(pExtra) #RESTO DE LA LINEA

print(p)
print(pExtra)



