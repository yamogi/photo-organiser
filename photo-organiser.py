#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("directory", help="the directory to look for photos in")
args = parser.parse_args()

print("Scanning: %s" % args.directory)

