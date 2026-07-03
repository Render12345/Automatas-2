grammar Expr;

root : expr EOF;

//expr: expr MENOS expr | NUM;

expr: EOF;
NUM:[0-9]+;
ADD:'+';
MUL:'*';
WS: [ \t\r\n]+ -> skip;