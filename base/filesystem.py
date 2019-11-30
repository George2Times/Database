#! /usr/bin/python
import os
import glob


def main():
    path = os.getcwd()

    os.chdir(path)
    for file in glob.glob("*.py"):
        print(file)


if __name__ == '__main__':
    main()