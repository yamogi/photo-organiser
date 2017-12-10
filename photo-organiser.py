#!/usr/bin/env python3

import argparse
import os
import sys

from datetime import datetime

import exifread


def check_dir_exists(directory):
    return os.path.isdir(directory)


def loop_through_dir(directory):
    print(" {}".format(directory))
    for file in os.listdir(directory):
        fullpath = os.path.join(directory, file)
        if os.path.isfile(fullpath):
            print(" └── {}".format(file))
            read_exif_data(fullpath)


def read_exif_data(image):
    dto_tag = "EXIF DateTimeOriginal"

    with open(image, "rb") as f:
        tags = exifread.process_file(f, stop_tag=dto_tag)
    if dto_tag in tags.keys():
        dto = tags[dto_tag]
        determine_image_date(dto)
    else:
        print("---- Tag does not exist ----")  # Need to exception handle this


def determine_image_date(date_tag):
    parsed_dto = datetime.strptime(str(date_tag), "%Y:%m:%d %H:%M:%S")

    image_year = parsed_dto.year
    image_month = parsed_dto.month
    image_day = parsed_dto.day

    print(" |   └── Year:  {:>4}".format(parsed_dto.year))
    print(" |   └── Month: {:>4}".format(parsed_dto.month))
    print(" |   └── Day    {:>4}".format(parsed_dto.day))


parser = argparse.ArgumentParser()
parser.add_argument("directory", help="the directory to look for photos in")
args = parser.parse_args()

print("Scanning: {}".format(args.directory))
print()

if not check_dir_exists(args.directory):
    print("The specified directory does not exist: {}".format(args.directory))
    sys.exit(1)

loop_through_dir(args.directory)
