#Importa ANTLR4 para funciones
from antlr4 import *

from ExprLexer import ExprLexer

#Lo que obtiene es la entrada, analiza el texto y lo separa en tokens
lexer = ExprLexer(InputStream(input("? ")))

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