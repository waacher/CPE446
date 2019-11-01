import sys
from collections import Counter

errors = []

def main():
    f = open(sys.argv[1], "r")
    lines = f.readlines()
    for line in lines:
        if ("finish" in line):
            errors.append((line.split()[2]))

    print(Counter(errors))

    f.close()            

if __name__ == '__main__':
    main()
