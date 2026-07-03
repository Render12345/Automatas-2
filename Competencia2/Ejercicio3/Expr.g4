grammar Expr;

root : expr EOF;

//expr: expr MENOS expr | NUM;

expr: EOF;
ID:[a-zA-Z]+;
NUM:[0-9]+;
ASIG:'=';
WS: [ \t\r\n]+ -> skip;