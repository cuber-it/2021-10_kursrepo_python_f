#!/usr/bin/env python3

for i in range(30, 130, 10):

   for characters in range(i, i+10):
      print('%5s'%chr(characters), end="")
   print()

   for decimal in range(i, i+10):
      print('%5s'%decimal, end="")
   print()




