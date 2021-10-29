
ascii_dict = dict()
ascii_range = range(32,128)
#for i in ascii_range:
#    ascii_dict[str(i)] = chr(i)
#Zeilen comprehension
ascii_dict = {str(i):chr(i) for i in ascii_range}

print(ascii_dict)    


# ascii_dict = {str(i):chr(i) for i in ascii_range}