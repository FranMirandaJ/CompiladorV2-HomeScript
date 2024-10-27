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
    programa : defConf defAuto bloqueLoop
    """
    #p[0] = ('programa', [p[1],p[2],p[3]])
    print('programa')

def p_defConf(p): 
    """
    defConf : DEF_CONF bloqueCodigoDefConf
    """
    #p[0] = ('defConf', p[2])
    print('defConf')

def p_bloqueCodigoDefConf(p): 
    """
    bloqueCodigoDefConf : LLAVE_IZQ listaDeclaracionesAsignaciones LLAVE_DER
    """
    print('bloqueCodigoDefConf')

def p_listaDeclaracionesAsignaciones(p): 
    """
    listaDeclaracionesAsignaciones : declaracionVariable listaDeclaracionesAsignaciones
                                   | declaracionAsignacionVariable listaDeclaracionesAsignaciones
                                   | sentAsignacion listaDeclaracionesAsignaciones
                                   | empty
    """
    print('listaDeclaracionesAsignaciones')

def p_defAuto(p):
    """
    defAuto : DEF_AUTO bloqueCodigoDefAuto
    """
    print('defAuto')

def  p_bloqueCodigoDefAuto(p):
    """
    bloqueCodigoDefAuto : LLAVE_IZQ listaFunciones LLAVE_DER
    """
    print('bloqueCodigoDefAuto')

def p_listaFunciones(p):
    """
    listaFunciones : declaracionFuncion listaFunciones
                   | empty
    """
    print('listaFunciones')

def p_bloqueLoop(p):
    """
    bloqueLoop : LOOP_PRINCIPAL bloqueCodigo
    """
    print('bloqueLoop')

def p_bloqueCodigo(p):
    """
    bloqueCodigo : LLAVE_IZQ listaSentencias LLAVE_DER
    """
    print('bloqueCodigo')

def p_listaSentencias(p):
    """
    listaSentencias : sentencia listaSentencias
                    | empty
    """
    print('listaSentencias')

def p_sentencia(p):
    """
    sentencia : declaracionVariable
              | declaracionAsignacionVariable
              | declaracionFuncion
              | sentAsignacion
              | sentSi
              | sentParaCada
              | llamarFuncion
              | imprimir
              | retornar
              | incremento
              | decremento
    """
    print('sentencia')

def p_declaracionVariable(p):
    """
    declaracionVariable : tipoDato ID PUNTOCOMA
                        | tipoDato CORCHETE_IZQ CORCHETE_DER ID PUNTOCOMA
    """
    print('declaracionVariable')

def p_declaracionAsignacionVariable(p):
    """
    declaracionAsignacionVariable : tipoDato ID ASIGNACION expresion PUNTOCOMA 
                                  | tipoDato ID ASIGNACION llamarFuncion PUNTOCOMA
                                  | tipoDato ID ASIGNACION instanciaObj PUNTOCOMA
                                  | tipoDato CORCHETE_IZQ CORCHETE_DER ID ASIGNACION bloqueArgumentos PUNTOCOMA
    """
    print('declaracionAsignacionVariable')

def p_sentAsignacion(p):
    """
    sentAsignacion : ID ASIGNACION expresion PUNTOCOMA
                   | accesoArreglo ASIGNACION expresion PUNTOCOMA
                   | ID ASIGNACION llamarFuncion PUNTOCOMA
    """
    print('sentAsignacion')

def p_instanciaObj(p):
    """
    instanciaObj : ID PARENTESIS_IZQ listaArgumentos PARENTESIS_DER PUNTOCOMA
    """
    print('instanciaObj')

def p_tipoDato(p):
    """
    tipoDato : TIPO_FECHA
             | TIPO_HORA
             | TIPO_BOOL
             | TIPO_ENTERO
             | TIPO_REAL
             | TIPO_CADENA
             | TIPO_SENSOR
             | TIPO_DISPOSITIVO
    """
    print('tipoDato')

def p_expresion(p):
    """
    expresion : expresionAritmetica
              | expresionLogica
              | expresionComparacion
              | PARENTESIS_IZQ expresion PARENTESIS_DER
              | valor
              | accesoArreglo
              | expresion expresion
    """
    print('expresion')

def p_valor(p):
    """
    valor : NUMERO 
          | REAL 
          | verdad 
          | falso 
          | CADENA
    """
    print('valor')

def p_expresionAritmetica(p):
    """
    expresionAritmetica : expresion SUMA expresion
                        | expresion RESTA expresion
                        | expresion MULTIPLICACION expresion
                        | expresion DIVISION expresion
    """
    print('expresionAritmetica')

def p_expresionLogica(p):
    """
    expresionLogica : expresion AND expresion
                    | expresion OR expresion
                    | NOT expresion
    """
    print('expresionLogica')

def p_expresionComparacion(p):
    """
    expresionComparacion : expresion MENORQUE expresion
                         | expresion MAYORQUE expresion
                         | expresion MENORIGUAL expresion
                         | expresion MAYORIGUAL expresion
                         | expresion IGUAL expresion
                         | expresion DIFERENTE expresion
    """
    print('expresionComparacion')

def p_accesoArreglo(p):
    """
    accesoArreglo : ID CORCHETE_IZQ expresion CORCHETE_DER
    """
    print('accesoArreglo')

def p_declaracionFuncion(p):
    """
    declaracionFuncion : FUNCION ID PARENTESIS_IZQ listaParametros PARENTESIS_DER RETORNO tipoDato bloqueCodigo
    """
    print('declaracionFuncion')

def p_listaParametros(p):
    """
    listaParametros : parametro
                    | parametro COMA listaParametros
                    | empty
    """
    print('listaParametros')

def p_parametro(p):
    """
    parametro : tipoDato ID
    """
    print('parametro')

def p_sentSi(p):
    """
    sentSi : SI PARENTESIS_IZQ expresion PARENTESIS_DER bloqueCodigo sentSiNo
    """
    print('sentSi')

def p_sentSiNo(p):
    """
    sentSiNo : SINO bloqueCodigo
             | SINO sentSi 
             | empty
    """
    print('sentSiNo')

def p_sentParaCada(p):
    """
    sentParaCada : PARACADA ID EN ID bloqueCodigo
    """
    print('sentParaCada')

def p_llamarFuncion(p):
    """
    llamarFuncion : instanciaObj
                  | SISTEMA PUNTO ID PARENTESIS_IZQ listaArgumentos PARENTESIS_DER PUNTOCOMA
                  | ID PUNTO ID PARENTESIS_IZQ listaArgumentos PARENTESIS_DER PUNTOCOMA
    """
    print('llamarFuncion')

def p_listaArgumentos(p):
    """
    listaArgumentos : expresion
                    | expresion COMA listaArgumentos
                    | bloqueArgumentos
                    | empty
    """
    print('listaArgumentos')

def p_bloqueArgumentos(p):
    """
    bloqueArgumentos : LLAVE_IZQ listaValores LLAVE_DER
    """
    print('bloqueArgumentos')

def p_listaValores(p):
    """
    listaValores : valor 
                 | valor COMA listaValores
    """
    print('listaValores')

def p_imprimir(p):
    """
    imprimir : IMPRIMIR PARENTESIS_IZQ CADENA PARENTESIS_DER PUNTOCOMA
    """
    print('imprimir')

def p_retornar(p):
    """
    retornar : RETORNAR expresion PUNTOCOMA
             | RETORNAR llamarFuncion PUNTOCOMA
    """
    print('retornar')

def p_incremento(p):
    """
    incremento : MASMAS ID PUNTOCOMA
               | ID MASMAS PUNTOCOMA
    """
    print('incremento')

def p_decremento(p):
    """
    decremento : MENOSMENOS ID PUNTOCOMA
               | ID MENOSMENOS PUNTOCOMA
    """
    print('decremento')

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, token={p.type}")
    else:
        print("Syntax error at EOF")


#CONSTRUIR ANALIZADOR
parser = yacc.yacc(debug=True)

def test_parser(codigo,lin):
    global linea
    linea = lin
    result = parser.parse(codigo)
    print(result)

codigo = """
         def_conf { }
         def_auto { }
         loop_principal { }
         """

test_parser(codigo,0)
#print(errores_Sinc_Desc)