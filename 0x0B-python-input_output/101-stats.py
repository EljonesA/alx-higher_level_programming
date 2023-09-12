#!/usr/bin/python3
""" Script: python """
import sys


def print_statistics(total_size, status_codes):
    print("File size: {:d}".format(total_size))
    for code in sorted(status_codes.keys()):
        count = status_codes[code]
        if count > 0:
            print("{:d}: {:d}".format(code, count))


def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0,
                    500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                if len(parts) >= 2:
                    status_code = int(parts[-2])
                    file_size = int(parts[-1])
                    total_size += file_size
                    if status_code in status_codes:
                        status_codes[status_code] += 1
            except ValueError:
                pass

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        pass

    print_statistics(total_size, status_codes)
