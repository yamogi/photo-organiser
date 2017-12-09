#!/usr/bin/env python3

import argparse
import os
import sys

def check_dir_exists(directory):
    try:
        if not os.path.isdir(directory):
            raise OSError
    except OSError:
        print("The specified directory does not exist: {}".format(directory))
        sys.exit(1)

def loop_through_dir(directory):
    print(" {}".format(directory))
    for file in os.listdir(directory):
        if os.path.isfile(file):
            print(" └── {}".format(file))

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="the directory to look for photos in")
args = parser.parse_args()

print("Scanning: {}".format(args.directory))
print()

check_dir_exists(args.directory)
loop_through_dir(args.directory)


