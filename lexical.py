import re
directives = {"#include", "#define"}
headers = {"<iostream>", "<stdio.h>", "<conio.h>", "<stdio.h>", "<math.h>", "<float.h>", "<stdlib.h>", "<string.h>"}
keywords = {"void", "using", "namespace", "int", "iostream", "std", "main", "cin", "cout", "return", "float", "double", "string","printf"}
operators = {"+", "-", "*", "/", "^", "&&", "||", "=", "==", "&", "|", "%", "++", "--", "+=", "-=", "/=", "*=", "%="}
comments = {"//", "/*", "*/"}
symbols = {"(", "{", "[", ")", "}", "]", "<", ">", "()", ";", "<<", ">>", ",", "#"}

def is_directive(s):
    return s in directives

def is_header(s):
    return s in headers

def is_keyword(s):
    return s in keywords

def is_operator(s):
    return s in operators

def is_symbol(s):
    return s in symbols


def is_constant(s):
    return re.match("^[-+]?\d+(\.\d+)?$", s) is not None

def is_identifier(s):
    return re.match("^[a-zA-Z_]\w*$", s) is not None

def is_comment(s):
    return s in comments

def main():
    with open("prog.txt", "r") as file:
        code = file.read().replace("\n", " ")

    s = ""
    for i in range(len(code)):
        if code[i] != " ":
            s += code[i]
        else:
            if is_operator(s):
                print(s, "is an operator")
                s = ""
            elif is_keyword(s):
                print(s, "is a keyword")
                s = ""
            elif is_symbol(s):
                print(s, "is a symbol")
                s = ""
            elif is_constant(s):
                print(s, "is a constant")
                s = ""
            elif is_identifier(s):
                print(s, "is an identifier")
                s = ""
            elif is_directive(s):
                print(s, "is a directive")
                s = ""
            elif is_header(s):
                print(s, "is a header")
                s = ""
            elif is_comment(s):
                print(s, "is a comment")
                s = ""
            else:
                s = ""

if __name__ == "__main__":
    main()

''' Output
#include is a directive
<stdio.h> is a header
int is a keyword
main is a keyword
( is a symbol
) is a symbol
{ is a symbol
printf is a keyword
; is a symbol
// is a comment
adding is an identifier
two is an identifier
number is an identifier
int is a keyword
a is an identifier
= is an operator
10 is a constant
a is an identifier
+= is an operator
2 is a constant
return is a keyword
0 is a constant
; is a symbol
} is a symbol
'''
