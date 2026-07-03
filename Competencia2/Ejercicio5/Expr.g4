grammar Expr;

root : expr EOF;

//expr: expr MENOS expr | NUM;

expr: EOF;
PRINT:'print';
CADENA: '"'~[" \t\r\n]*'"';
WS: [ \t\r\n]+ -> skip;