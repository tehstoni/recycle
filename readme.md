# Python Shellcode to Bin Tool

This tool, `recycle.py`, is crafted to read the contents of an input file, cleanse it by removing specific characters, and transform the data into a sanitized hexadecimal string. This string is then written to an output file. It's particularly useful for data sanitization and preparation in contexts where hexadecimal representation is required.

## Features

- **Data Sanitization**: Removes problematic characters (such as quotes, semicolons, and spaces) and ensures the data is in a clean state.
- **Hexadecimal Conversion**: Formats the sanitized data into a hexadecimal string, facilitating its use in environments where hex representation is crucial.

## Prerequisites

Before using this script, you should have the following:
- Python 3.x installed on your computer.

## Installation

No formal installation is necessary. Simply download the `recycle.py` file to a directory of your choice on your local machine.

## Usage

To use this tool, open your terminal or command prompt, navigate to the folder containing `recycle.py`, and execute the following command:

```shell
./recycle.py -i <input_file> -o <output_file>
```

    Replace <input_file> with the path to your original data file.
    Replace <output_file> with the path where you want the hexadecimal-formatted data to be stored.

## Command Line Arguments

    -i or --input: The input file path.
    -o or --output: The output file path where the processed hex data will be saved.

## Example Command
To convert example.txt into a hexadecimal format and save it as formatted.hex:
```shell
./recycle.py -i example.txt -o formatted.hex
```
## Contributing
Your contributions are welcome! If you'd like to improve the recycle.py script, please fork the repository, commit your changes or improvements, and initiate a pull request.
License
This script is released under the MIT License, making it freely available for both personal and commercial use.