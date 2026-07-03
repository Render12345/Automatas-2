grammar Expr;

root : expr EOF;

//expr: expr MENOS expr | NUM;

expr: EOF;
IF:'if';
ID:[a-zA-Z_$][0-9a-zA-Z_$]*;
NUM:[0-9]+;
BIG:'>';
PareI:'(';
PareF:')';
WS: [ \t\r\n]+ -> skip;

