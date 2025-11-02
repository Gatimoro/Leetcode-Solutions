# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacc = []
        for t in tokens:
            try:
                stacc.append(int(t))
            except:
                b, a = stacc.pop(), stacc.pop()
                # print(eval(str(a) + t + str(b)))
                stacc.append(int(eval(str(a) + t + str(b))))
        return stacc[0]
