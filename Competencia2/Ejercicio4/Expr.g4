grammar Expr;

root : expr EOF;

//expr: expr MENOS expr | NUM;

expr: EOF;
IF:'if';
ID:[a-zA-Z]+;
COMP:'>';
NUM:[0-9]+; 
WS: [ \t\r\n]+ -> skip;