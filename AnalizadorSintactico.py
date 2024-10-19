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