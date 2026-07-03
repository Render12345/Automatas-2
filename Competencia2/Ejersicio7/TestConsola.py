#Importa ANTLR4 para funciones
from antlr4 import *

from ExprLexer import ExprLexer

#Lo que obtiene es la entrada, analiza el texto y lo separa en tokens
lexer = ExprLexer(InputStream(input("? ")))

tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

print(
    f"{'Texto':<15}"
    f"{'Tipo':<15}"
    f"{'Linea':<15}"
    f"{'Columna':<15}"
    f"{'Nombre del token':<15}"
    )
   
print("-"*75)
for token in tokens.tokens:
    nombre_token = lexer.symbolicNames[token.type]
    print(
        f"{token.text:<15}"
        f"{token.type:<15}"
        f"{token.line:<15}"
        f"{token.column:<15}"
        f"{nombre_token:<15}"
        )

    
    print("-"*75)