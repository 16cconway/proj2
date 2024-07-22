# Proj 2

This is a python module for 605.202 Data Structures Lab 2. It converts 
expressions directly from prefix to postfix using recursion. For example, the 
string "-A+BC" is a prefix expression, and the program will directly convert 
it to "ABC+-" which is the equivalent postfix expression.

## Running Proj 2

1. Download and install Python 3.11 on your computer
2. Navigate to [this](.) directory (containing the README.md)
3. Run the program as a module: `python -m proj2 -h`. This will print the help message.
4. Run the program as a module (with real inputs): `python -m proj2 <some_input_file> <some_output_file>`

   IE: `python -m proj2 resources/input/RequiredInput.txt output/ReqOut.txt`

Output will be written to the specified output file after processing the input file.

### Proj 2 Usage:

```commandline
usage: python -m proj2 -h in_file out_file

positional arguments:
  in_file     Input File Pathname
  out_file    Output File Pathname

optional arguments:
  -h or --help  show this help message and exit
```

## Input
The first positional argument is the input file. The path to the input 
file should be relative to the top level proj2 directory. The input file 
should be a text file. If the input file does not exist, the program will 
error and print to the console.

### Input Handling
Each line of the input file represents a different expression. Blank lines 
are ignored, and spaces or tabs within or at the ends of a line are also 
ignored.

### Valid Inputs
Inputs should contain **operators** (+, -, /, *, ^, $) or **alphabet 
letters** only. * represents multiplication. $ and ^ both represent 
exponentiation. The number of operators must equal the number of operands 
minus 1. The expression must be in a valid prefix form where every one 
operator must be on the left of two operands.

## Output
The second positional argument is the output file. This file should be a 
text file. If the file does not exist, the program will create it.

### Output for Valid Inputs
* Inputted Prefix Expression
* Equivalent Postfix Expression
* Equivalent Infix Expression

### Output for Invalid Inputs
* Inputted Prefix Expression
* Error Explained

> **Note:** Errors are also printed to the console

### Ending Output
* Input Size (number of characters in the entire input file)
* Runtime 

## Python Packaging

### Python IDE 
I used PyCharm Community Edition for development of this project

### Python Version
Python 3.11

### Python Packages

* `argparse`
    * Used for parsing the command line arguments containing the 
      input and output text files
* `pathlib`
    * Used for creating paths from input and output arguments
* `sys`
  * Used to handle errors and printing them to the console
* `typing`
  * Used to specify type hints of TextIO for starter function
* `time`
  * Used to calculate run time metrics for later analysis
* `proj1.modify_strings`
  * Developer created script that contains functions for string manipulation 
* `proj2.runtime_metric`
  * Provided sample code for class of RuntimeMetric to contain size of an 
    input and duration of the solution
* `proj2.get_input_size`
  * Developer created script used for getting the size of the input for time 
    complexity analysis
* `proj2.get_valid_char`
  * Developer created script used to read next non whitespace character from 
    input string
* `proj2.prefix_to_infix_recursive`
  * Developer created script to convert a prefix expression to infix using 
    recursion. This script is **not** used in the project's delivery as 
    this conversion was done during prefix to postfix conversion for 
    improved time complexity.

### Project Layout

* [proj2/](.): The parent or "root" folder containing all of these files.
    * [README.md](README.md):
      The guide you're reading.
    * [proj2](proj2): 
      This is a *module* in this *package*.
      * [`__init__.py`](proj2/__init__.py) 
        This is used to expose what functions, variables, classes, etc. are 
        exposed when scripts import this module.
      * [`__main__.py`](proj2/__main__.py) 
        This file is the entrypoint to this program when ran as a program. 
        It handles command line arguments.
      * `*.py` 
        These are python scripts that perform the actual logic of the program.





