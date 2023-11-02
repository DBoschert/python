import sys
# python3 c2f_batch.py 100 0 -40

cstrs = sys.argv[1:]
for cstr in cstrs:
    c = float(cstr)
    f = float(c) * 9 / 5 + 32
    print(f"{c:.1f}C is {f:.1f}F")
