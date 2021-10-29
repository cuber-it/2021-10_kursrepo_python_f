for v in range(33,127):
    if v <= 42:
        print(chr(v), end = ' ')
    elif v >= 43 and v <= 52:
        print(chr(v), end = ' ')
    elif v >= 53 and v <= 62:
        print(chr(v), end = ' ')
    elif v >= 63 and v <= 72:
        print(chr(v), end = ' ')
    elif v >= 73 and v <= 82:
        print(chr(v), end = ' ')
    elif v >= 83 and v <= 92:
        print(chr(v), end = ' ')
    elif v >= 93 and v <= 102:
        print(chr(v), end = ' ')
    elif v >= 103  and v <= 112:
        print(chr(v), end = ' ')
    elif v >= 113  and v <= 122:
        print(chr(v), end = ' ')
    elif v >= 123 and v <= 127:
        print(chr(v), end = ' ')
    else:
        break

    start = 33
end = 127
for v in range(start, end):
    if (start - v) % 10 == 0: # check if (start - v) is a multiple of 10
        print("")
    print(chr(v), end=' ')

    import termtables as tt

tt.print(
    [[1, 2, 3], [613.23236243236, 613.23236243236, 613.23236243236]],
    header=["a", "bb", "ccc"],
    style=tt.styles.ascii_thin_double,
    padding=(0, 1),
    alignment="lcr"
)