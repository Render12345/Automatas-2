grammar Expr;

root : expr EOF;

//expr: expr MENOS expr | NUM;

expr: EOF;
Print:'print';
CADENA: '"' (~["\r\n])* '"';
PareI:'(';
PareF:')';
FinSent: ';';
WS: [ \t\r\n]+ -> skip;