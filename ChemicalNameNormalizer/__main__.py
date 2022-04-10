import argparse
import asyncio
import sys
from utils import read_input, write_output

from ChemicalNameNormalizer.normalizer import Normalizer


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i',
                        '--input',
                        type=str,
                        required=True,
                        help='Input file')

    parser.add_argument(
        '-f', '--normalization_format',
        type=str,
        required=False,
        help='Preferred chemical name format {"trivial", "iupac"}')

    parser.add_argument('-o',
                        '--output',
                        type=str,
                        required=True,
                        help='Output file')
    return parser


def main(argv):
    parser = create_parser()
    args = parser.parse_args(argv)

    input_file: str = args.input
    output_file: str = args.output
    normalization_format: str = args.normalization_format

    input_data = read_input(input_file)
    normalizer = Normalizer(normalization_format)
    normalized = asyncio.run(normalizer.normalize(input_data))

    write_output(output_file, input_data, normalized)
    print("DONE")
    return 0


if __name__ == '__main__':
    main(sys.argv[1:])