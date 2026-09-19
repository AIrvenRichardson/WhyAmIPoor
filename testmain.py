# A simple script for calling functions in isolation.
import import_csv
import sys

def main():

    if len(sys.argv) != 2:
        raise IndexError("Dude, you just have to put in a file path it is not that hard.")

    import_csv.read_transactions(None, sys.argv[1], "Posted Date")
    print("??????")
    return

main()