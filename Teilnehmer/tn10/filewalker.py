#!/usr/bin/env python3
import os
import re

class filewalker():

    def __init__(self, startdir, pattern):
        self.startdir = startdir
        self.pattern = pattern
        self.result = []

    def walk(self):
        pass

if __name__ == "__main__":
    f = filewalker("/","*.dir")