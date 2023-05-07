#include <iostream>
#include <cstring>
#include <stdlib.h>
#include <ctype.h>
#include <fstream>
#include <string>
using namespace std;

string arr[] = {"void", "using", "namespace", "int", "iostream", "std", "cin", "cout", "return", "float", "double", "string"};

string arr1[] = {"<iostream>", "<cstring>", "<stdlib.h>", "<ctype.h>", "<fstream>", "<string>"};

bool isKeyword(string a)
{
    for (int i = 0; i < 12; i++)
    {
        if (arr[i] == a)
        {
            return true;
        }
    }
    return false;
}

bool isheaderfile(string a)
{
    for (int i = 0; i < 6; i++)
    {
        if (arr1[i] == a)
        {
            return true;
        }
    }
    return false;
}

int main()
{

    std::ifstream file("prog.txt");
    std::string x;
    string code = "";
    while (std::getline(file, x))
    {
        code += x;
    }

    string s = "";
    
    for (int i = 0; i < code.size(); i++)
    {
        if (code[i] != ' ')
        {
            s += code[i];
//             cout << code << endl;
        }
        else
        {
            if (s == "#include")
            {
                cout << s << " is a preprocessor directive" << endl;
                s = "";
            }
            else if (isheaderfile(s))
            {
                cout << s << " is a Header File" << endl;
                s = "";
            }
            else if (s == "+" || s == "-" || s == "*" || s == "/" || s == "^" || s == "&&" || s == "||" ||
                     s == "=" || s == "==" || s == "&" || s == "|" || s == "%" || s == "++" || s == "--" || s == "+=" ||
                     s == "-=" || s == "/=" || s == "*=" || s == "%=")
            {
                cout << s << " is an operator" << endl;
                s = "";
            }

            else if (isKeyword(s))
            {
                cout << s << " is a keyword" << endl;
                s = "";
            }

            else if (s == "(" || s == "{" || s == "[" || s == ")" || s == "}" || s == "]" || s == "<" ||
                     s == ">" || s == "()" || s == ";" || s == "<<" || s == ">>" || s == "," || s == "#")
            {
                cout << s << " is a symbol" << endl;
                s = "";
            }

            else if (s == "\n" || s == "" || s == "")
            {
                s = "";
            }

            else if (isdigit(s[0]))
            {
                int x = 0;
                if (!isdigit(s[x++]))
                {
                    continue;
                }
                else if (s.find('.') != std::string::npos)
                {
                    cout << s << " is a float number" << endl;
                    s = "";
                }
                else{
                	cout << s << " is a number" << endl;
                    s = "";
				}
            }

            else
            {
                if (s.find('"') != std::string::npos)
                {
                    cout << s << " is a message" << endl;
                    s = "";
                }
                else if (s.find('/') != std::string::npos)
                {
                    cout << s << " these line is a comment" << endl;
                    s = "";
                }
                else
                {
                    cout << s << " is an identifier" << endl;
                    s = "";
                }
            }
        }
    }
}


// output 

// #include is a preprocessor directive
// <iostream> is a Header File
// void is a keyword
// main is an identifier
// ( is a symbol
// ) is a symbol
// { is a symbol
// int is a keyword
// a is an identifier
// = is an operator
// 3 is a number
// ; is a symbol
// int is a keyword
// b is an identifier
// = is an operator
// 6.5 is a float number
// ; is a symbol
// int is a keyword
// c is an identifier
// = is an operator
// 9 is a number
// ; is a symbol
// int is a keyword
// d is an identifier
// = is an operator
// a is an identifier
// + is an operator
// b is an identifier
// + is an operator
// c is an identifier
// ; is a symbol
// cout is a keyword
// << is a symbol
// d is an identifier
// ; is a symbol
// cout is a keyword
// << is a symbol
// "Nitesh" is a message
// << is a symbol
// endl is an identifier
// ; is a symbol
// //Helloworld these line is a comment
// } is a symbol