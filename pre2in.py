"""
Converts prefix notation to infix notation.
"""

import sys


def ops(c):
    if c in ['^', '*', '/', '+', '-', '(', ')']:
        return True
    return False


def main():
    if len(sys.argv) < 2:
        print("Converts prefix notation to infix notation")
        print("    Usage: python pre2in.py \"<prefix_expression_separated_by_spaces>\"")
        print("    e.g. python pre2in.py \"* + a b c\"")
        return
    
    prefix = sys.argv[1].split()
    st = []
    
    i = len(prefix) - 1
    while i >= 0:
        if not ops(prefix[i]):
            st.append(prefix[i])
            i -= 1
        else:
            str = "(" + st.pop() + prefix[i] + st.pop() + ")"
            st.append(str)
            i -= 1
    
    print(st.pop())


if __name__ == "__main__":
    main()
