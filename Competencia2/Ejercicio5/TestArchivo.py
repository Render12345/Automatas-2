#Importa ANTLR4 para funciones
from antlr4 import *

from ExprLexer import ExprLexer

import sys 

#Lo que obtiene es la entrada, analiza el texto y lo separa en tokens
input_stream = FileStream(sys.argv[1])

lexer = ExprLexer(input_stream)

tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for token in tokens.tokens:
    print("Texto ",token.text)
    print("Tipo ",token.type)
    print("Linea ",token.line)
    print("Columna ",token.column)
    nombre_token = lexer.symbolicNames[token.type]

    print("Nombre del token: ", nombre_token)

    print("--------------------")