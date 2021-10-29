#for i in ascii_range:
#    ascii_dict[str(i)] = chr(i)
#print(ascii_dict)
ascii_dict = { str(i):chr(i) for i in range(32,128)}
print(ascii_dict)