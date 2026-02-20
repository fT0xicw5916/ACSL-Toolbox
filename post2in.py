"""
Converts postfix notation to infix notation.
"""

import sys


def main():
    if len(sys.argv) < 2:
        print("Converts postfix notation to infix notation")
        print("    Usage: python post2in.py \"<postfix_expression_separated_by_spaces>\"")
        print("    e.g. python post2in.py \"2 4 8 2 - * 5 2 ^ / - 8 4 / 2 / 8 * +\"")
        return
    
    st = []
    ops = set(['+', '-', '*', '/', '^'])

    for token in sys.argv[1].split():
        if token not in ops:
            st.append(token)
        else:
            op2 = st.pop()
            op1 = st.pop()
            new_expr = f"({op1} {token} {op2})"
            st.append(new_expr)
    
    print(st[0] if st else "")


if __name__ == "__main__":
    main()
