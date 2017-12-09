#!/usr/bin/env python3

import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="the directory to look for photos in")
args = parser.parse_args()

print("Scanning: %s" % args.directory)
print()

try:
    if not os.path.isdir(args.directory):
        raise OSError
except OSError:
    print("The specified directory does not exist")
    sys.exit(1)

for file in os.listdir(args.directory):
    if os.path.isfile(file):
        print(file)

