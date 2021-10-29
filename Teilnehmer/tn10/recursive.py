#!/usr/bin/env python3

_ = lambda x: x

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return n + recursive_sum(n-1)
print(recursive_sum(100))

help = _("Hallo")
print(help)