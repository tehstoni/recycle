#!/usr/bin/env python3
import argparse

def read_input_file(input_file):
    with open(input_file, 'r') as file:
        input_data = file.read().replace('"', '').replace(';', '').replace('\n', '').replace(' ', '').replace('0x', '\\x').replace(',', '').replace('b', '').replace("'", '')
    return input_data


def write_output_file(output_file, hex_data):
    with open(output_file, 'w') as file:
        file.write(hex_data)


def main():
    parser = argparse.ArgumentParser(description='Process input and output files.')

    parser.add_argument('-i', '--input', help='Input file')
    parser.add_argument('-o', '--output', help='Output file')

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    input_data = read_input_file(input_file)
    print("input data:" + input_data + '\n')
    write_output_file(output_file, input_data)
    

if __name__ == "__main__":
    main()