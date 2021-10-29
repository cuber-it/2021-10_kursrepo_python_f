#!/usr/bin/env python3

# importing required library
import sys
import string

def print_table():
    for i in range(0,128):
        ascii_value = chr(i)
        if ascii_value.isprintable():
            print(i,ascii_value)
        else:
            print(i, ".")

if __name__ == "__main__":
    print_table()
    sys.exit(0)