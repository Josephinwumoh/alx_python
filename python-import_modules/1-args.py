#!/usr/bin/env python3
import sys

def main():
    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 arguments.")
    else:
        if num_args == 1:
            print("1 argument:")
        else:
            print(f"{num_args} arguments:")

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"{i}: {arg}")

if __name__ == "__main__":
    main()
