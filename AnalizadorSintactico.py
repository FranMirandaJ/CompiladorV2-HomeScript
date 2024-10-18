#IMPORTAR LIBRERIAS
import ply.yacc as yacc
#IMPORTAR TOKENS
from AnalizadorLexico import tokens

errores_Sinc_Desc = []

def limpiar_errores():
    global errores_Sinc_Desc
    errores_Sinc_Desc = []

linea = 0

precedence = (
    ('left', 'IGUAL', 'DIFERENTE'),
    ('left', 'MENORQUE', 'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION')
)

#GRAMATICA INICIAL
def p_programa(p):
    """
    programa : BEGIN bloque_codigo END
    """
    p[0] = ('programa',p[2])

def p_bloque_codigo(p):
    """
    bloque_codigo : LLAVE_A lista_declaraciones LLAVE_C
    """
    p[0] = ('bloque_codigo',p[2])

def p_lista_declaraciones(p):
    """
    lista_declaraciones : declaracion
                        | si
                        | mientras
                        | lista_declaraciones lista_declaraciones
    """
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_declaracion(p):
    """
    declaracion : tipo ID ASIGNACION expresion PUNTOCOMA
    """
    p[0] = ('declaracion',p[1],p[2],p[4])

def p_declaracion_error1(p):
    """
    declaracion : tipo ID ASIGNACION expresion
    """
    errores_Sinc_Desc.append("ERROR 1: Falta punto y coma en la linea: " + str(p.lineno(2)-linea))

def p_declaracion_error2(p):
    """
    declaracion : tipo ID ASIGNACION PUNTOCOMA
    """
    errores_Sinc_Desc.append("ERROR 2: Falta la expresion a asignar en la linea: " + str(p.lineno(2)-linea))

def p_tipo(p):
    """
    tipo : int
         | bool
         | stg
         | real
    """
    p[0] = p[1]

# EXPRESIONES
def p_expresion_suma(p):
    'expresion : expresion SUMA expresion'
    p[0] = p[1] + p[3]

def p_expresion_resta(p):
    'expresion : expresion RESTA expresion'
    p[0] = p[1] - p[3]

def p_expresion_mult(p):
    'expresion : expresion MULTIPLICACION expresion'
    p[0] = p[1] * p[3]

def p_expresion_div(p):
    'expresion : expresion DIVISION expresion'
    if p[3] != 0:
        p[0] = p[1] / p[3]
        if(p[0]%1 == 0):
            p[0] = int(p[0])
        

def p_expresion_comparacion(p):
    '''
    expresion : expresion MENORQUE expresion
              | expresion MENORIGUAL expresion
              | expresion MAYORQUE expresion
              | expresion MAYORIGUAL expresion
    '''
    if p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]

def p_expresion_comparacion2(p):
    '''
    expresion : expresion IGUAL expresion
              | expresion DIFERENTE expresion
    '''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]

def p_expresion(p):
    """
    expresion : PARENTESIS_A expresion PARENTESIS_B
              | NUMERO
              | REAL
              | CADENA
              | True
              | False
    """
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_si(p):
    """
    si : IF PARENTESIS_A expresion PARENTESIS_B bloque_codigo
       | IF PARENTESIS_A expresion PARENTESIS_B bloque_codigo ELSE bloque_codigo
    """
    if len(p) == 8:
        p[0] = ('IF',p[3],p[5],'ELSE',p[7])
    else:
        p[0] = ('IF',p[3],p[5])

def p_mientras(p):
    """
    mientras : WHILE PARENTESIS_A expresion PARENTESIS_B bloque_codigo
    """
    p[0] = ('WHILE',p[3],p[5])

def p_for_loop(p):
    """
    for_loop : FOR PARENTESIS_A for_init PUNTOCOMA for_condicion PUNTOCOMA for_actualizacion PARENTESIS_B bloque_codigo
    """
    p[0] = ('for_loop', {'init': p[3], 'condition': p[5], 'update': p[7], 'body': p[9]})

def p_for_init(p):
    """
    for_init : tipo ID ASIGNACION expresion
             | ID ASIGNACION expresion
    """
    if len(p) == 5:
        p[0] = ('init', {'tipo': p[1], 'id': p[2], 'valor': p[4]})
    else:
        p[0] = ('init', {'id': p[1], 'valor': p[3]})

def p_for_condicion(p):
    """
    for_condicion : expresion
    """
    p[0] = ('condicion', p[1])

def p_for_actualizacion(p):
    """
    for_actualizacion : ID ASIGNACION expresion
                      | ID MASMAS
                      | ID MENOSMENOS
    """

#CONSTRUIR ANALIZADOR
parser = yacc.yacc()

def test_parser(codigo,lin):
    global linea
    linea = lin
    result = parser.parse(codigo)
    print(result)

codigo = """
         BEGIN {
            IF (8>5) {
                WHILE (12 == 2) {
                    int variable = 2 ;
                }
            }
         } END
         """

test_parser(codigo,0)
print(errores_Sinc_Desc)