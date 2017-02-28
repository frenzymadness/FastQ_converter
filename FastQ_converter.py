#!/usr/bin/env python3

import sys


def help():
    print('Usage: {} <input_file> <output_file>'.format(sys.argv[0]))


def convert_to_csv(in_file, out_file):
    with open(in_file) as infd:
        with open(out_file, 'w') as outfd:
            outfd.write('"SeqID","sequence","quality"\n')
            for line in infd:
                if not line.startswith('@'):
                    continue
                seq_id = line.strip()
                sequence = next(infd).strip()
                next(infd)
                quality = next(infd).strip()

                outfd.write('"{}","{}","{}"\n'.format(seq_id, sequence, quality))


def main():
    if len(sys.argv) < 3:
        help()
        sys.exit(1)
    else:
        convert_to_csv(sys.argv[1], sys.argv[2])


if __name__ == '__main__':
    main()
