#!/usr/bin/env python3
import argparse

def read_input_file(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().replace('"', '').replace(';', '').replace('\n', '').replace(' ', '').replace('0x', '\\x').replace(',', '').replace('b', '').replace("'", '')
    return input_data

def write_output_file(output_file, shellcode):
    shellcode_bytes = bytes(shellcode, 'utf-8')
    with open(output_file, "wb") as file:
        file.write(shellcode_bytes)

def main():
    parser = argparse.ArgumentParser(description='Process input and output files.')
    parser.add_argument('-i', '--input', help='Input file', required=True)
    parser.add_argument('-o', '--output', help='Output file', required=True)
    args = parser.parse_args()
    shellcode = read_input_file(args.input)
    print(shellcode[:100] + "...")
    write_output_file(args.output, shellcode)

if __name__ == "__main__":
    main()
