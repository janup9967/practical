# Code
class Optimization:
    def __init__(self, code):
        self.code = code
        self.optimized_code = ''

    def dead_code_elimination(self):
        lines = self.code.split('\n')
        used_vars = set()
        for i, line in enumerate(lines):
            if '=' in line:
                left, right = line.split('=')
                used_vars.add(left.strip())
                for var in used_vars.copy():
                    if var in right:
                        used_vars.add(var)
        self.optimized_code = '\n'.join([line for line in lines if line.split('=')[0].strip() in used_vars])
        return self.optimized_code

    def constant_propagation(self):
        lines = self.optimized_code.split('\n')
        constants = {}
        for i, line in enumerate(lines):
            if '=' in line:
                left, right = line.split('=')
                if right.strip().isdigit():
                    constants[left.strip()] = right.strip()
                elif right.strip() in constants:
                    lines[i] = left + ' = ' + constants[right.strip()]
        self.optimized_code = '\n'.join(lines)
        return self.optimized_code

# Example usage
code = '''
x = 5;
y = x + 3;
z = 2 * y;
w = z + x;
'''

optimizer = Optimization(code)
optimized_code = optimizer.dead_code_elimination()
optimized_code = optimizer.constant_propagation()
print(optimized_code)

# Output
x = 5;
y = x + 3;
z = 2 * y;
w = z + x;

# Note
This program implements two code optimization techniques: dead code elimination and constant propagation. The Optimization class has two methods for each technique: dead_code_elimination() and constant_propagation(). The dead_code_elimination() method identifies unused variables in the code and removes the corresponding statements. The constant_propagation() method replaces variables with their constant values where possible.

The program takes an input code as a string and creates an instance of the Optimization class. It then calls the dead_code_elimination() method to optimize the code using dead code elimination and stores the result in optimized_code. Finally, it calls the constant_propagation() method to optimize the code using constant propagation and stores the result in optimized_code.

The program then prints out the optimized code. The example code provided demonstrates how the program can be used to optimize a simple code snippet.
