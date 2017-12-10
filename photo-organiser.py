#!/usr/bin/env python3

import argparse
import os
import sys

from datetime import datetime

import exifread


def photo_organiser():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="the directory to look for photos in")
    args = parser.parse_args()

    print("Scanning: {}".format(args.directory))
    print()

    if not check_dir_exists(args.directory):
        print("The specified directory does not exist: {}".format(args.directory))
        sys.exit(1)
    else:
        find_images_in_dir(args.directory)


def check_dir_exists(directory):
    return os.path.isdir(directory)


def find_images_in_dir(directory):
    print(" {}".format(directory))
    for file in os.listdir(directory):
        fullpath = os.path.join(directory, file)
        if os.path.isfile(fullpath):
            print(" └── {}".format(file))
            read_exif_data(fullpath)


def read_exif_data(image):
    dt_tag = "EXIF DateTimeOriginal"

    with open(image, "rb") as f:
        tags = exifread.process_file(f, stop_tag=dt_tag)
    if dt_tag in tags.keys():
        dt = tags[dt_tag]
        determine_image_date(dt)
    else:
        print("         Tag does not exist")  # Need to exception handle this
        print("        (Not an image file?)")


def determine_image_date(date_tag):
    parsed_dt = datetime.strptime(str(date_tag), "%Y:%m:%d %H:%M:%S")

    image_year = parsed_dt.year
    image_month = parsed_dt.month
    image_day = parsed_dt.day

    print(" │   └── Year:  {:>4}".format(parsed_dt.year))
    print(" │   └── Month: {:>4}".format(parsed_dt.month))
    print(" │   └── Day    {:>4}".format(parsed_dt.day))


if __name__ == '__main__':
    photo_organiser()
