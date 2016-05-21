import re
import sys

regex_fejadat = re.compile("^VF\|(.)+$")
regex_teteladat = re.compile("^VT\|(.)+$")
regex_check_fejadat = re.compile(
    "^VF\|"
    "12\|"
    "[a-zA-Z0-9]{,8}\|"
    "[a-zA-Z0-9]{13}\|"
    "(.){1,70}\|"
    "[a-zA-Z0-9]{,20}\|"
    "[a-zA-Z0-9]{,10}\|"
    "(.){3,20}\|"
    "[0-9]{4}\|"
    "(.){3,20}\|"
    "(.){3,30}\|"
    "1\|"
    "\|"
    "\|"
    "[a-zA-Z0-9]{2,20}\|"
    "[0-9]{8}\|"
    "[0-9]{8}"
    "\s*$")
regex_check_teteladat = re.compile(
    "^VT\|"
    "[0-9a-zA-Z]{1,20}\|"
    "[0-9]{8}\|"
    "(.){2,50}\|"
    "([0-9]{1,12}\.[0-9]{2}|)\|"
    "[A-Za-z]{1,2}\|"
    "([0-9]{1,4}\.[0-9]{2,3}|)\|"
    "([0-9]{1,3}\.[0-9]{2}|)\|"
    "([0-9]{1,13}\.[0-9]{2}|)\|"
    "HUF"
    "\s*$")


def read_file(file_path):
    with open(file_path) as f:
        content = f.readlines()
    return content


def is_fejadat_true(line):
    return regex_check_fejadat.match(line)


def is_teteladat_true(line):
    return regex_check_teteladat.match(line)


def main():
    content = read_file(sys.argv[1])
    line_number = 0
    for line in content:
        line_number += 1

        if regex_fejadat.match(line) and not is_fejadat_true(line):
            sys.stdout.write("Error:Fej:%d:%s" % (line_number, line))

        if regex_teteladat.match(line) and not is_teteladat_true(line):
            sys.stdout.write("Error:Tetel:%d:%s" % (line_number, line))


if __name__ == "__main__":
    main()
