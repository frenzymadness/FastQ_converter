#!/usr/bin/env python3

import sys


def help():
    print('Usage: {} <input_file> [output_file]'.format(sys.argv[0]))


def convert_to_csv(in_file, out_file):
    out_file.write(u'"SeqID","sequence","quality"\n')
    for line in in_file:
        if not line.startswith('@'):
            continue
        seq_id = line.strip()
        sequence = next(in_file).strip()
        next(in_file)
        quality = next(in_file).strip()
        out_file.write(u'"{}","{}","{}"\n'.format(seq_id, sequence, quality))


def main():
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    else:
        in_file = sys.argv[1]
        if len(sys.argv) >= 3:
            # If we have it, take name of output from parameters
            out_file = sys.argv[2]
        else:
            # else make it from input file name
            out_file = '.'.join(in_file.split('.')[:-1]) + '.csv'

        with open(in_file) as infd:
            with open(out_file, 'w') as outfd:
                convert_to_csv(infd, outfd)


if __name__ == '__main__':
    main()
