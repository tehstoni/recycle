# Shellcode Converter

This Python script is designed to read shellcode from an input file in textual format and convert it into raw bytes, which are then written to an output file. This can be particularly useful in security research or exploitation scenarios where shellcode needs to be transformed into a binary format.
Prerequisites

    Python 3.x

## Usage

    Clone the repository or download the shellcode_converter.py script.
    Run the script using Python:

```bash
python shellcode_converter.py -i input_file.txt -o output_file.bin
```

Replace input_file.txt with the path to your input file containing shellcode in a string format, and output_file.bin with the desired name for the output file where the raw shellcode bytes will be written.
Command-line Arguments

    -i, --input: Path to the input file containing shellcode in a string format. (Required)
    -o, --output: Path to the output file where the raw shellcode bytes will be written. (Required)

## Example

Suppose you have an input file named shellcode.txt containing shellcode represented as a string:

```
\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\x50\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x48\x89\xe7\xb0\x3b\x0f\x05
```

You can convert this shellcode into raw bytes and write them to an output file named shellcode.bin using the following command:

```bash
python shellcode_converter.py -i shellcode.txt -o shellcode.bin
```

This will create a file named shellcode.bin containing the raw bytes of the shellcode.
License

This script is provided under the MIT License. Feel free to modify and distribute it as needed. Contributions are welcome!