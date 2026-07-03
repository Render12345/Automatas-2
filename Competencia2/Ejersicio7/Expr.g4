grammar Expr;

root : expr EOF;

//expr: expr MENOS expr | NUM;

expr: EOF;
INT:'int';
ID:[a-zA-Z_$][0-9a-zA-Z_$]*;
NUM:[0-9]+;
ASIG:'=';
WS: [ \t\r\n]+ -> skip;