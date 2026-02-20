"""
Converts infix notation to postfix notation.
"""

import sys


def prec(c):
    if c == '^':
        return 3
    elif c in ('/', '*'):
        return 2
    elif c in ('+', '-'):
        return 1
    return -1


def main():
    if len(sys.argv) < 2:
        print("Converts infix notation to postfix notation")
        print("    Usage: python in2post.py \"<infix_expression_with_no_spaces>\"")
        print("    e.g. python in2post.py \"a+b*c\"")
        return
    
    st = []
    res = ""

    for c in sys.argv[1]:
        if c.isalnum():
            res += c + ' '
        elif c == '(': 
            st.append('(')
        elif c == ')':
            while st and st[-1] != '(': 
                res += st.pop() + ' '
            st.pop()
        else:
            while st and prec(c) <= prec(st[-1]):
                res += st.pop() + ' '
            st.append(c)
    
    while st:
        res += st.pop() + ' '

    print(" ".join(res.split()))


if __name__ == "__main__":
    main()
