"""
Converts infix notation to prefix notation.
"""

import sys


def prec(op):
    if op == '^':
        return 3
    if op in ['*', '/']:
        return 2
    if op in ['+', '-']:
        return 1
    return -1


def in2post(s: str):
    st = []
    res = ""

    for i in range(len(s)):
        if s[i].isalnum():
            res += s[i] + ' '
        elif s[i] == '(':
            st.append(s[i])
        elif s[i] == ')':
            while st and st[-1] != '(':
                res += st.pop() + ' '
            st.pop()
        else:
            while st and prec(s[i]) <= prec(st[-1]):
                res += st.pop() + ' '
            st.append(s[i])

    while st:
        res += st.pop() + ' '
    
    return res


def main():
    if len(sys.argv) < 2:
        print("Converts infix notation to prefix notation")
        print("    Usage: python in2pre.py \"<infix_expression_with_no_spaces>\"")
        print("    e.g. python in2pre.py \"a+b*c\"")
        return
    
    infix = sys.argv[1][::-1]
    infix = ''.join(['(' if ch == ')' else ')' if ch == '(' else ch for ch in infix])
    
    print(in2post(infix)[::-1])


if __name__ == "__main__":
    main()
