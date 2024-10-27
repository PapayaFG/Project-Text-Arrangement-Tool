# text_arranger.py

def read_file(filename):
    """Reads lines from a text file and returns them as a list."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    # Remove any extra whitespace, including newlines
    lines = [line.strip() for line in lines]
    return lines

def sort_text(lines):
    """Sorts a list of strings alphabetically."""
    return sorted(lines)

def write_file(filename, lines):
    """Writes a list of strings to a text file, each on a new line."""
    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + '\n')

def main():
    # Step 1: Read text from the input file
    input_filename = 'input.txt'
    output_filename = 'sorted_output.txt'
    
    print("Reading from", input_filename)
    lines = read_file(input_filename)
    
    # Step 2: Sort the text
    print("Sorting text")
    sorted_lines = sort_text(lines)
    
    # Step 3: Write sorted text to the output file
    print("Writing sorted text to", output_filename)
    write_file(output_filename, sorted_lines)
    print("Text sorting complete!")

# Run the program
if __name__ == "__main__":
    main()
