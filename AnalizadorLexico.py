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
    'IMPRIMIR', 'SI', 'SINO', 'PARACADA', 'EN', 'SISTEMA', 'FUNCION', 'RETORNO', 'RETORNAR',
    'LOOP_PRINCIPAL', 'ARREGLO', 'TIPO_FECHA', 'TIPO_HORA', 'TIPO_BOOL', 'TIPO_ENTERO', 'TIPO_REAL',
    'TIPO_CADENA', 'TIPO_SENSOR', 'TIPO_DISPOSITIVO'
]

tokens = [
    'SUMA', 'RESTA', 'DIVISION', 'MULTIPLICACION',
    'ASIGNACION', 'IGUAL', 'DIFERENTE', 'MAYORQUE', 'MENORQUE', 
    'MENORIGUAL', 'MAYORIGUAL', 'PUNTO', 'COMA', 'PUNTOCOMA',
    'COMILLASIMPLE', 'COMILLADOBLE', 'PARENTESIS_IZQ', 'PARENTESIS_DER', 'LLAVE_IZQ',
    'LLAVE_DER', 'CORCHETE_IZQ', 'CORCHETE_DER', 'MASMAS', 'MENOSMENOS', 'AND', 'OR', 'NOT',
    'ID', 'NUMERO', 'REAL', 'verdad', 'falso', 'COMENTARIO', 'BLOQUE_COMENTARIOS'
    
]

tokens += reservadas;

#metodo para identificadores no validos
def t_IDError(t):
    r'\d+[a-zA-ZñÑ][a-zA-Z0-9ñÑ]*'
    global errores_Desc
    errores_Desc.append("Identificador no valido en la linea "+str(t.lineno))


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
    r'[a-zA-Z][a-zA-Z0-9_]*'
    
    if t.value == 'si':
        t.type = 'SI'
    elif t.value == 'si-no':
        t.type = 'SINO'
    elif t.value == 'para_cada':
        t.type = 'PARACADA'
    elif t.value == 'en':
        t.type = 'EN'
    elif t.value == 'funcion':
        t.type = 'FUNCION'
    elif t.value == 'retornar':
        t.type = 'RETORNAR'
    elif t.value == 'retorno':
        t.type = 'RETORNO'
    elif t.value == 'Sistema':
        t.type = 'SISTEMA'
    elif t.value == 'entero':
        t.type = 'TIPO_ENTERO'
    elif t.value == 'real':
        t.type = 'TIPO_REAL'
    elif t.value == 'cadena':
        t.type = 'TIPO_CADENA'
    elif t.value == 'Dispositivo':
        t.type = 'TIPO_DISPOSITIVO'
    elif t.value == 'Sensor':
        t.type = 'TIPO_SENSOR'
    elif t.value == 'fecha':
        t.type = 'TIPO_FECHA'
    elif t.value == 'hora':
        t.type = 'TIPO_HORA'
    elif t.value == 'bool':
        t.type = 'TIPO_BOOL'
    elif t.value == 'arreglo':
        t.type = 'ARREGLO'
    elif t.value == 'loop_principal':
        t.type = 'LOOP_PRINCIPAL'
    elif t.value == 'imprimir':
        t.type = 'IMPRIMIR'
    elif t.value == 'verdad':
        t.type = 'verdad'
    elif t.value == 'falso':
        t.type = 'falso'
    else:
        t.type = 'ID'
    return t

def t_SALTOLINEA(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_CADENA(t):
    r'\".*?\"'  #(":delimitador inicial y final de la cadena),(.:cualquier caracter),(*:0 o mas)(?:para que no sea codicioso)
    t.type = 'CADENA'
    return t

def t_COMENTARIO(t):
    r'\/\/.*'
    pass

def t_BLOQUE_COMENTARIOS(t):
    r'\/\*(.|\n)*?\*\/'
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
    errores_Desc.append(f"Símbolo no válido '{t.value[0]}' en la linea {t.lineno}, columna {find_column(t.lexer.lexdata, t)}")
    t.lexer.skip(1)

def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = -1
    return token.lexpos - last_cr

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

if __name__ == '__main__':
    codigo = """
        Dispositivo disp = Luz("asd"); Sensor sensor
         """

    print(analisis(codigo))

    if errores_Desc:
        print("Errores encontrados:")
        for error in errores_Desc:
            print(error)
