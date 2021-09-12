PalabrasClave = {'FALSE':'False','NONE':'None','TRUE':'True','AND':'and','AS':'as','ASSERT':'assert','ASYNC':'async','AWAIT':'await','BREAK':'break',
                 'CLASS':'class','CONTINUE':'continue','DEF':'def','DEL':'del','ELIF':'elif','ELSE':'else','EXCEPT':'except','FINALLY':'finally',
                 'FOR':'for','FROM':'from','GLOBAL':'global','IF':'if','IMPORT':'import','IN':'in','IS':'is','LAMBDA':'lambda','NONLOCAL':'nonlocal',
                 'NOT':'not','OR':'or','PASS':'pass','RAISE':'raise','RETURN':'return','TRY':'try','WHILE':'while','WITH':'with','YIELD':'yield'}

for clave in PalabrasClave:
    valor = PalabrasClave[clave] 
    print(clave+" "+valor)
