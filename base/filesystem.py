#! /usr/bin/python
import os, glob

path = os.getcwd()

os.chdir( path )
for file in glob.glob("*.py"):
    print(file)
