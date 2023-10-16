"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    
    import csv
    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])
        
    lines = data.split('\n')
    suma_total = 0
    for line in lines:
        if line.strip():
            parts = line.split('\t')
            num = int(parts[1])
            suma_total += num
    return suma_total


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import csv
    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])
    letter_counts = {}
    
    lines = data.strip().split('\n')
    for line in lines:
        parts = line.split('\t')
        letter = parts[0]
        
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    
    cantidad= sorted(letter_counts.items())
    return cantidad

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import csv
    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])
    letter_sums = {}
    lines = data.strip().split('\n')
    for line in lines:
        parts = line.split('\t')
        letter = parts[0]
        value = int(parts[1])
        if letter in letter_sums:
            letter_sums[letter] += value
        else:
            letter_sums[letter] = value
    suma = sorted(letter_sums.items())       
    
    return suma

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    import csv
    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])
    
    meses = {}
    lineas = data.strip().split('\n')
    for linea in lineas:
        campos = linea.split('\t')
        fecha = campos[2]
        mes = fecha.split('-')[1]
        if mes in meses:
            meses[mes] += 1
        else:
            meses[mes] = 1
    respuesta = list(meses.items())
    respuesta.sort(key=lambda x: int(x[0]))
    return respuesta


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    import csv
    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])
    
    max_values = {}
    min_values = {}

    rows = data.strip().split('\n')

    for row in rows:
        columns = row.split('\t')
        letra = columns[0]
        valor_columna_2 = int(columns[1])
        if letra in max_values:
            max_values[letra] = max(max_values[letra], valor_columna_2)
        else:
            max_values[letra] = valor_columna_2
        if letra in min_values:
            min_values[letra] = min(min_values[letra], valor_columna_2)
        else:
            min_values[letra] = valor_columna_2
        
        result = [(letra, max_values[letra], min_values[letra]) for letra in sorted(max_values)]

    return result


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    clave_valores_min = {}
    clave_valores_max = {}
    import csv
    with open('data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            if row:
                _, _, _, _, columna5 = row
                entries = columna5.split(',')

                for entry in entries:
                    key, value = entry.split(':')
                    value = int(value)

                    if key in clave_valores_min:
                        if value < clave_valores_min[key]:
                            clave_valores_min[key] = value
                        if value > clave_valores_max[key]:
                            clave_valores_max[key] = value
                    else:
                        clave_valores_min[key] = value
                        clave_valores_max[key] = value

    resultado = []
    for key in sorted(clave_valores_min.keys()):
        resultado.append((key, clave_valores_min[key], clave_valores_max[key]))

    return resultado


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import csv

    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        data = "\n".join(["\t".join(row) for row in csv_reader])

    values_dict = {}

    rows = data.strip().split('\n')

    for row in rows:
        columns = row.split('\t')
        valor_columna_2 = int(columns[1])
        letra_columna_1 = columns[0]

        if valor_columna_2 in values_dict:
            values_dict[valor_columna_2].append(letra_columna_1)
        else:
            values_dict[valor_columna_2] = [letra_columna_1]

    respuesta = [(valor, letras) for valor, letras in values_dict.items()]

    respuesta.sort()

    return respuesta


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    import csv

    values_dict = {}

    with open("data.csv", mode='r', newline='') as file:
        csv_reader = csv.reader(file, delimiter='\t')
        next(csv_reader)  

        for row in csv_reader:
            valor_columna_2 = int(row[1])
            letra_columna_1 = row[0]

            if valor_columna_2 in values_dict:
                values_dict[valor_columna_2].add(letra_columna_1)
            else:
                values_dict[valor_columna_2] = {letra_columna_1}

    respuesta = [(key, sorted(list(value))) for key, value in sorted(values_dict.items())]

    return respuesta


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import csv

    nombre_archivo = "data.csv"
    # Inicializa un diccionario para almacenar las claves y valores decodificados
    conteo_claves  = {}

    # Abrir el archivo CSV en modo lectura
    with open(nombre_archivo, 'r', newline='') as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter='\t') # Utiliza '\t' como delimitador

    # Recorrer las filas del archivo CSV
        for fila in lector_csv:
            #if len(fila) >= 5: #columna 1
                claves_col5 = fila[4].split(',')  # Las claves están en la columna 5

            # Iteramos sobre cada clave en la columna 5
                for clave in claves_col5:
                    # Extraer la clave y el conteo
                        clave, conteo = clave.split(':')
                        conteo = int(conteo)

                        # Incrementamos el conteo para esta clave
                        conteo_claves[clave] = conteo_claves.get(clave, 0) + 1

    # Ordenar el diccionario por las claves
    conteo_claves_ordenado = {k: conteo_claves[k] for k in sorted(conteo_claves)}
                   
    return conteo_claves_ordenado


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    respuesta = []
    import csv
    with open('data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')

        for row in csvreader:
            letra_columna_1 = row[0]
            column_4 = row[3].split(',')
            column_5 = row[4].split(',')

            cantidad_columna_4 = len(column_4)
            cantidad_columna_5 = len(column_5)

            respuesta.append((letra_columna_1, cantidad_columna_4, cantidad_columna_5))

    return respuesta


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_letras = {}
    import csv
    with open('data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')

        for row in csvreader:
            columna_2 = int(row[1])
            letras_columna_4 = row[3].split(',')

            for letra in letras_columna_4:
                letra = letra.strip()  
                letra = letra.strip('\ufeff')  
                if letra in suma_letras:
                    suma_letras[letra] += columna_2
                else:
                    suma_letras[letra] = columna_2

    respuesta = {k: v for k, v in sorted(suma_letras.items())}

    return respuesta

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    
    import csv
    with open('data.csv', newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')

    suma_columna_5 = {}

    for row in csvreader:
            letra_columna_1 = row[0]
            column_5 = row[4].split(',')

            for entry in column_5:
                _, valor = entry.split(':')
                valor = int(valor)

                if letra_columna_1 in suma_columna_5:
                    suma_columna_5[letra_columna_1] += valor
                else:
                    suma_columna_5[letra_columna_1] = valor

    # Ordenar el diccionario
    respuesta = dict(sorted(suma_columna_5.items()))

    return respuesta
