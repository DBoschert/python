import sys
import logging
# python3 c2f_batch.py 100 0 -40

logging.basicConfig(
    filename='c2f_batch.log', 
    level=logging.WARNING
)

cstrs = sys.argv[1:]
for cstr in cstrs:
    try:
        c = float(cstr)
    except Exception:
        with open("c2f_batch.log", "w") as log_out:
            logging.exception("Exception:")
        print("ONLY ENTER NUMBERS")
        print("number was automatically entered as 1")
        c = 1

    f = float(c) * 9 / 5 + 32
    print(f"{c:.1f}C is {f:.1f}F")