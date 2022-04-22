import csv

#Decir si en la favorable es la respuesta mas comun y sensata, decir si lo mas normal
polarized_fav = {
    'Completamente de acuerdo': 0.5,
    'De acuerdo': 0.25,
    'Neutral': 0,
    'Desacuerdo': -0.75,
    'Completamente desacuerdo': -1
}

#Decir si en la desfavorable es la respuesta mas radical, decir que si extrano
polarized_unfav = {
    'Completamente de acuerdo': 1,
    'De acuerdo': 0.75,
    'Neutral': 0,   
    'Desacuerdo': -0.25,
    'Completamente desacuerdo': -0.5
}

neutral = {
    'Completamente de acuerdo': 0.75,
    'De acuerdo': 0.5,
    'Neutral': 0,
    'Desacuerdo': -0.5,
    'Completamente desacuerdo':-0.75
}
#Positive v negative
# positive are capitalist, diplomatic, democratic and progressive
# negative are socialist, nationalistic, authocratic and traditional
# If in favour is positive, then (+1), if not (-1)
questiondict = {
    #Economic
    '5. Es necesario que el gobierno intervenga en la economia para proteger a los consumidores.': ('neutral', '-1'),
    '6. Cuanta mas apertura economica haya, mas libre sera la poblacion.': ('neutral', '+1'),
    '7. Es mejor mantener un presupuesto equilibrado que garantizar el bienestar de todos los ciudadanos.': ('neutral', '+1'),
    '8. Los impuestos sobre el comercio internacional son importantes para fomentar la produccion local.': ('neutral', '-1'),
    '9. Seria mejor si se abolieran los programas sociales en favor de la caridad privada':  ('neutral', '+1'),
    "10. Deberian aumentarse los impuestos a los ricos para mantener a los pobres.": ('neutral', '-1'), ##
    "11. Los servicios basicos como agua y electricidad deben ser de propiedad publica.": ('neutral', '-1'),
    "12. La intervencion y regulacion del gobierno en la economia es una amenaza para esta.": ('neutral', '+1'),
    "13. Los medios de produccion deben pertenecer a los trabajadores que los utilizan.": ('neutral', '-1'), ##
    #Diplomatic
    "14. Las Naciones Unidas no dan suficientes resultados con respecto a los recursos que tienen": ('neutral', '-1'),
    "15. Apoyo las uniones regionales, como la Union Europea.": ('neutral', '+1'),
    "16. Un unico gobierno mundial seria beneficioso para la humanidad.": ('polarized_unfav', '-1'),
    "17. Para una nacion, es mas importante mantener relaciones pacificas que fortalecer su fuerza militar.": ('neutral', '+1'),
    "18. Las guerras no necesitan justificarse ante otros paises.": ('polarized_unfav', '-1'),
    "19. El gasto militar es una perdida de dinero": ('neutral', '+1'), ##
    "20. La ayuda internacional es una perdida de dinero.": ('neutral', '-1'),
    "21. Los gobiernos deberian ser responsabilizados por sus acciones en la comunidad internacional.": ('polarized_fav', '+1'),
    "22. La accion militar de una nacion a menudo es necesaria para protegerla.": ('polarized_unfav', '-1'),
    #Social
    "23. Incluso cuando se protesta contra un gobierno autoritario, la violencia no es aceptable.": ('polarized_fav', '-1'),
    "24. Es muy importante mantener la ley y el orden.": ('polarized_fav', '-1'),
    "25. La poblacion en general toma malas decisiones.": ('neutral', '-1'),
    "26. Es importante que el gobierno siga la opinion de la mayoria, incluso si esta equivocada.": ('neutral', '+1'),
    "27. Cuanto mas fuerte sea el liderazgo, mejor.": ('neutral', '-1'),
    "28. La mera existencia del estado es una amenaza para nuestra libertad.": ('polarized_unfav', '+1'),
    "29. Mis valores religiosos deberian difundirse tanto como sea posible.": ('neutral', '-1'),
    "30. La vigilancia gubernamental es necesaria en el mundo moderno.": ('neutral', '-1'),
    #Civil
    "31. Las regulaciones ambientales son esenciales.": ('neutral', '+1'),
    "32. Un mundo mejor vendra de la automatizacion, la ciencia y la tecnologia.": ('polarized_fav', '+1'),
    "33. Los ninos deben ser educados en valores religiosos.": ('neutral', '-1'),
    "34. La religion deberia desempenar un papel en el gobierno.": ('neutral', '-1'),
    "35. El consumo de drogas debe legalizarse o despenalizarse.": ('neutral', '+1'),
    "36. El matrimonio entre personas del mismo sexo deberia ser legal.": ('neutral', '+1'),
    "37. El aborto deberia prohibirse en la mayoria o en todos los casos.": ('neutral', '-1'),
    "38. Debe prohibirse la posesion de armas de fuego a quienes no tengan una razon valida.": ('neutral', '+1'),
    
}

def getavrgvalue(count, type):
    values = []
    total = len(data_list[0])-1
    if type[0] == 'neutral':
        for pair in count:
            values.append(pair[1] * neutral[pair[0]] * int(type[1]))
        return round(sum(values)/total, 2)
    elif type[0] == 'polarized_unfav':
        for pair in count:
            values.append(pair[1] * polarized_unfav[pair[0]] * int(type[1]))
        return round(sum(values)/total, 2)
    elif type[0] == 'polarized_fav':
        for pair in count:
            values.append(pair[1] * polarized_fav[pair[0]] * int(type[1]))
        return round(sum(values)/total, 2)
    else: return f'ERROR OF INPUT, NO TYPE {type[0]}'

def countanswers(answerlist):
    canswerlist = answerlist.copy()
    canswerlist.pop(0)
    answercount = [
        ('Completamente de acuerdo', canswerlist.count('Completamente de acuerdo')),
        ('De acuerdo', canswerlist.count('De acuerdo')), 
        ('Neutral', canswerlist.count('Neutral')), 
        ('Desacuerdo', canswerlist.count('Desacuerdo')), 
        ('Completamente desacuerdo', canswerlist.count('Completamente desacuerdo'))]
    return answercount

def demographycount(datalist):
    demography = datalist[0]
    demography.pop(0)
    totaldem = len(demography)
    dem5 = demography.count('5to ano')
    dem4 = totaldem - dem5
    dem5percent = round((dem5/totaldem)*100, 2)
    dem4percent = 100 - dem5percent
    return [dem5, dem4, dem5percent, dem4percent]


with open('respuestas-tesisv2.csv') as csv_file:
    csv_list = list(csv.reader(csv_file, delimiter=','))
    header_list = csv_list[0]
    data_list = [[] for x in range(len(header_list))]
    for position, answers in enumerate(data_list):
        answers.extend([row[position] for row in csv_list])

    result_list = data_list[5:]
    avrgvalues = []
    print(list(countanswers(column) for column in result_list[18:26]))
    for column in result_list:
        avrgvalues.append(getavrgvalue(countanswers(column), questiondict[list(column)[0]]))
    econ_values = avrgvalues[:9]
    diplom_values = avrgvalues[9:18]
    social_values = avrgvalues[18:26]
    civil_values = avrgvalues[26:]
    print(econ_values, diplom_values, social_values, civil_values)
    total_econ = round(sum(econ_values), 2)
    total_diplom = round(sum(diplom_values), 2)
    total_social = round(sum(social_values), 2)
    total_civil = round(sum(civil_values), 2)
    print(total_econ, total_diplom, total_social, total_civil)
