#IMPORTAR MODULO LEX
import ply.lex as lex

#DEFINIR DOS VARIABLES PARA ERRORES
errores_Desc = []
lista_errores_lexicos = []

#DEFINIR METODO PARA VACIAR LISTAS
def limpiar_errores_lex():
    global errores_Desc
    global lista_errores_lexicos
    errores_Desc = []
    lista_errores_lexicos = []

reservadas = [
    'MOSTRAR', 'SI', 'SINO', 'PARACADA', 'EN', 'SISTEMA', 'FUNCION', 'RETORNO', 'RETORNAR',
    'LOOP_PRINCIPAL', 'ARREGLO', 'TIPO_FECHA', 'TIPO_HORA', 'TIPO_BOOL', 'TIPO_ENTERO', 'TIPO_REAL',
    'TIPO_CADENA', 'TIPO_SENSOR', 'TIPO_DISPOSITIVO', 'SISTEMA'
]

tokens = [
    'SUMA', 'RESTA', 'DIVISION', 'MULTIPLICACION',
    'ASIGNACION', 'IGUAL', 'DIFERENTE', 'MAYORQUE', 'MENORQUE', 
    'MENORIGUAL', 'MAYORIGUAL', 'PUNTO', 'COMA', 'PUNTOCOMA',
    'COMILLASIMPLE', 'COMILLADOBLE', 'PARENTESIS_IZQ', 'PARENTESIS_DER', 'LLAVE_IZQ',
    'LLAVE_DER', 'CORCHETE_IZQ', 'CORCHETE_DER', 'MASMAS', 'MENOSMENOS', 'AND', 'OR', 'NOT',
    'ID', 'ENTERO', 'REAL', 'verdad', 'falso', 'COMENTARIO'
    
]

tokens += reservadas;

#METODO PARA IDENTIFICADORES NO VALIDOS
def t_IDError(t):
    r'\d+[a-zA-ZñÑ][a-zA-Z0-9ñÑ]*'  #INICIA CON 1 O MAS DIGITOS, SEGUDO DE UNA LETRA, SEGUIDO DE 0 O MAS LETRAS Y DIGITOS
    global errores_Desc
    errores_Desc.append("Identificador no válido en la linea: " + str(t.lineno))

t_ignore = ' \t'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'\/'
t_ASIGNACION = r'\='
t_IGUAL = r'\=='
t_DIFERENTE = r'\!='
t_MAYORQUE = r'\>'
t_MENORQUE = r'\<'
t_MENORIGUAL = r'\<='
t_MAYORIGUAL = r'\>='
t_PUNTO = r'\.'
t_COMA = r'\,'
t_PUNTOCOMA = r'\;'
t_COMILLASIMPLE = r'\''
t_COMILLADOBLE = r'\"'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_MASMAS = r'\+{2}'
t_MENOSMENOS = r'\-{2}'
t_AND = r'\&{2}'
t_OR = r'\|{2}'
t_NOT = r'\!'

#METODO PARA IDENTIFICADORES
def t_IDENTIFICADOR(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value == 'BEGIN':
        t.type = 'BEGIN'
    elif t.value == 'END':
        t.type = 'END'
    elif t.value == 'FOR':
        t.type = 'FOR'
    elif t.value == 'WHILE':
        t.type = 'WHILE'
    elif t.value == 'IF':
        t.type = 'IF'
    elif t.value == 'ELSE':
        t.type = 'ELSE'
    elif t.value == 'int':
        t.type = 'int'
    elif t.value == 'real':
        t.type = 'real'
    elif t.value == 'bool':
        t.type = 'bool'
    elif t.value == 'stg':
        t.type = 'stg'
    elif t.value == 'FUN':
        t.type = 'FUN'
    elif t.value == 'True':
        t.type = 'True'
    elif t.value == 'False':
        t.type = 'False'
    else:
        t.type = 'ID'
    return t


def t_SALTOLINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_CADENA(t):
    r'\#.*?\#'  #(#:delimitador inicial y final de la cadena),(.:cualquier caracter),(*:0 o mas)(?:para que no sea codicioso)
    t.type = 'CADENA'
    return t

def t_COMENTARIO(t):
    r'\//(.*?)\//'  #(//:delimitador inicial y final del comentario),(():subexpresion),(.:cualquier caracter),(*:0 o mas),(?:transforma la busqueda en no codiciosa)
    pass

def t_REAL(t):
    r'(\d+\.\d+ | \.\d+)'   #(d+:1 o mas digitos),(\.\:punto literal),(|:or)
    t.value = float(t.value)
    return t

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    global errores_Desc
    errores_Desc.append(f"Simbolo '{t.value[0]}' en la linea {t.lineno}")
    t.lexer.skip(1)

#CONSTRUIR EL ANALIZADOR LEXICO
lexer = lex.lex()

def analisis(cadena):   #funcion recibe 'cadena'
    lexer.input(cadena)
    tokens = []
    # Inicia el número de línea en 1
    lexer.lineno = 1
    for tok in lexer:
        columna = tok.lexpos - cadena.rfind('\n', 0, tok.lexpos)
        tokens.append((tok.value, tok.type, tok.lineno, columna))
    return tokens

print(analisis('int a = 5;'))