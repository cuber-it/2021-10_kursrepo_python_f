#!/usr/bin/env python3
import os
import fnmatch

class filewalker:
    def __init__(self):
        for root,dir files in os.walk(".") :
            print root
            print ""
            for items in fnmatch.filter(files,"*"):
                print "... "+ items
                print ""
