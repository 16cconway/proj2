# This file is the entry point into this program when the module is executed
# as a standalone program. IE 'python -m proj1'. This file is NOT run during
# imports.

# Used to process command line arguments and 'launch' the program
from pathlib import Path
import argparse
from sys import stderr
from proj1 import convert_prefix_to_postfix

# Parse the arguments from the command line
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
args = arg_parser.parse_args()

# Convert the parsed arguments to the respective input and output path
in_path = Path(args.in_file)
out_path = Path(args.out_file)

# Open the input file in read mode, open the output file in write mode, and
# call convert function
try:
    with in_path.open('r') as input_file, out_path.open('w') as output_file:
        convert_prefix_to_postfix(input_file, output_file)
except FileNotFoundError:
    print("Error: Input file was not found", file=stderr)
