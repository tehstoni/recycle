import argparse
import re

def convert_string_to_bytes(shellcode_string):
    # Normalize different hex representations to a single format and remove unwanted characters
    # Remove double quotes, semicolons, and non-hex characters that are not part of the hex format
    cleaned_shellcode_string = re.sub(r'[";]', '', shellcode_string)  # Remove double quotes and semicolons
    
    # Further, remove any text that does not match hex patterns
    hex_pattern = re.compile(r'\\?0?x([0-9A-Fa-f]+)|([0-9A-Fa-f]{2})')
    matches = hex_pattern.findall(cleaned_shellcode_string)
    # Concatenate all matched hex values, ensuring we only keep valid hex characters
    hex_string = ''.join(match[0] if match[0] else match[1] for match in matches)
    
    # Convert the cleaned hex string into raw bytes
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
