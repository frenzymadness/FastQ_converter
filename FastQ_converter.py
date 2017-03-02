#!/usr/bin/env python3

import sys


def help():
    print('Usage: {} <input_file> <output_file>'.format(sys.argv[0]))


def convert_to_csv(in_file, out_file):
    out_file.write('"SeqID","sequence","quality"\n')
    for line in in_file:
        if not line.startswith('@'):
            continue
        seq_id = line.strip()
        sequence = next(in_file).strip()
        next(in_file)
        quality = next(in_file).strip()

        out_file.write('"{}","{}","{}"\n'.format(seq_id, sequence, quality))


def main():
    if len(sys.argv) < 3:
        help()
        sys.exit(1)
    else:
        with open(sys.argv[1]) as infd:
            with open(sys.argv[2], 'w') as outfd:
                convert_to_csv(infd, outfd)


if __name__ == '__main__':
    main()
