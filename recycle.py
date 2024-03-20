import argparse

def convert_string_to_bytes(shellcode_string):
    # First, ensure we remove all occurrences of "\x" which are not part of the hex value
    # Then, filter out any non-hexadecimal characters that may have sneaked into our incantation
    hex_string = ''.join(shellcode_string.split("\\x")[1:])
    hex_string = ''.join(filter(lambda x: x in '0123456789abcdefABCDEF', hex_string))
    # Now convert what remains into raw bytes
    return bytes.fromhex(hex_string)

def main():
    parser = argparse.ArgumentParser(description="This script reads shellcode from an input file in a textual format and writes the raw bytes to an output file.")
    parser.add_argument("-i", "--input", required=True, help="Input file containing shellcode in a string format.", type=str)
    parser.add_argument("-o", "--output", required=True, help="Output file to write the raw shellcode bytes to.", type=str)
    args = parser.parse_args()

    # Read the shellcode from the input file
    with open(args.input, "r") as file:
        shellcode_string = file.read()

    # Convert the string representation of the shellcode into raw bytes
    shellcode_bytes = convert_string_to_bytes(shellcode_string)

    # Write the raw bytes to the specified output file
    with open(args.output, "wb") as file:
        file.write(shellcode_bytes)
    
    print(f"Shellcode has been successfully written to {args.output}")

if __name__ == "__main__":
    main()
