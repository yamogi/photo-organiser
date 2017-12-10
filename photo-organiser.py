#!/usr/bin/env python3

import argparse
import os
import sys

import exifread


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
        fullpath = os.path.join(directory,file)
        if os.path.isfile(fullpath):
            print(" └── {}".format(file))
            read_exif_data(fullpath)


def read_exif_data(image):
    dto_tag = "EXIF DateTimeOriginal"
    with open(image, "rb") as f:
        tags = exifread.process_file(f, stop_tag=dto_tag)
    if dto_tag in tags.keys():
        print("    Tag exists")
        dto = tags[dto_tag]
        print("        {}".format(dto))
    else:
        print("    Tag does not exist")


parser = argparse.ArgumentParser()
parser.add_argument("directory", help="the directory to look for photos in")
args = parser.parse_args()

print("Scanning: {}".format(args.directory))
print()

check_dir_exists(args.directory)
loop_through_dir(args.directory)
