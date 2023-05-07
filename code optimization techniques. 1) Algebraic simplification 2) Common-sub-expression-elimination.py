# Method 1
# 1. Algebraic Simplification:
import sympy
x, y ,a = sympy.symbols('x y a')   # define the input expression
expr = a + x*2 -0 + 2*x*y * 1 + y*2 + 0 - a
simplified_expr = sympy.simplify(expr)  # simplify the expression
#output - 2*x*y + 2*x + 2*y

# Method 2
# 1. Algebraic Simplification:
def simplify(expr): 
    expr = expr.replace('1*', '')
    expr = expr.replace('*1', '')
    expr = expr.replace('0*', '0')
    expr = expr.replace('*0', '0')
    expr = expr.replace('+0', '')
    expr = expr.replace('-0', '')
    expr = expr.replace('x-x', '')
    expr = expr.replace('y-y', '')
    expr = expr.replace('x+-x', '0')
    expr = expr.replace('x*1-', 'x-')
    expr = expr.replace('+1-1', '')
    expr = expr.replace('-1*x', '-x')
    expr = expr.replace('x*0', '0') 
    return expr

expr = 'x-x - x*1 + x*x + 2*x*y +1-1'
simplified_expr = simplify(expr)
print(simplified_expr)
#output =  - x + x*x + 2*x*y


# 2. Common Subexpression Elimination:
a, b, c = 2, 3, 4  # define the input expression
expr = a*b*c + a*b*c + a*b*c + a*b
temp = a*b*c  # eliminate common subexpressions
simplified_expr = temp*3 + a*b
print(simplified_expr)
#output - 78



# import sympy
# x, y ,a = sympy.symbols('x y a')

# def Algebraic_simplicaation(expr):
#     return sympy.simplify(expr)

# print(Algebraic_simplicaation('x-x - x*1 + x*x + 2*x*y +1-1'))
