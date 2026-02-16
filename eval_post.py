"""
Evaluates a postfix expression, assuming that there are no custom operators.
"""

import operator
import sys


def main():
    if len(sys.argv) < 2:
        print("Evaluates a postfix expression, assuming that there are no custom operators")
        print("    Usage: python eval_post.py \"<expression_split_by_whitespaces>\"")
        print("    e.g. python eval_post.py \"3 4 * 8 2 / + 7 5 - ^\"")
        return

    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '^': operator.pow
    }
    
    stack = []
    for token in sys.argv[1].split():
        if token not in ops:
            stack.append(float(token))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            result = ops[token](op1, op2)
            stack.append(result)
    
    print(stack[0])


if __name__ == "__main__":
    main()
