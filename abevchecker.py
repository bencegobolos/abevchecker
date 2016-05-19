import re
import sys

regex_fejadat = re.compile("^VF\|(.)+$")
regex_teteladat = re.compile("^VT\|(.)+$")
regex_check_fejadat = re.compile("^VF\|12\|[a-zA-Z0-9]{,8}\|[a-zA-Z0-9]{13}\|(.){1,70}\|[a-zA-Z0-9]{,20}\|[a-zA-Z0-9]{,10}\|(.){3,20}\|[0-9]{4}\|(.){3,20}\|(.){3,30}\|1\|\|\|[a-zA-Z0-9]{2,20}\|[0-9]{8}\|[0-9]{8}\s+$")
regex_check_teteladat = re.compile("^VT\|(.)+$")

def read_file(file_path):
    with open(file_path) as f:
        content = f.readlines()

    return content

def check_fejadat(line):
    return True

def check_teteladat(line):
    return True

def main():
    content = read_file(sys.argv[1])
    line_number = 0
    for line in content:
        line_number += 1

        if regex_fejadat.match(line) and not regex_check_fejadat.match(line):
            print("Error:Tetel:%d:%s" % (line_number, line))

        if regex_teteladat.match(line) and not regex_check_teteladat.match(line):
            print("Error:Fej:%d:%s" % (line_number, line))

    print("PROGRAM DONE")

if __name__ == "__main__":
    main()
