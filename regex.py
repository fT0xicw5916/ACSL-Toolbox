"""
Checks for regex matches.
"""

import re
import sys


def main():
    if len(sys.argv) < 3:
        print("Checks for regex matches")
        print("    Usage: python regex.py \"<regex_rule>\" \"<query1>\" \"<query2>\" \"<query3>\" ...")
        print("    e.g. python regex.py \"00*1*1|11*0*0\" \"0000001111111\" \"1010101010\" \"1111111\" \"0110\" \"10\"")
        return
    
    for i in sys.argv[2:]:
        x = re.findall(sys.argv[1], i)
        if len(x) > 0:
            print(x[0] == i)
        else:
            print(False)


if __name__ == "__main__":
    main()
