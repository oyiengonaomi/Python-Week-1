def read_file(filename):
    """Read the content of a file and return it."""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")
        return None

def write_file(filename, content):
    """Write content to a new file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Successfully written to '{filename}'.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be written.")

def modify_content(content):
    """Modify the content read from the file."""
    # Example modification: Convert to uppercase
    modified_content = content.upper()
    return modified_content

def main():
    # Ask the user for the input filename
    input_filename = input("Enter the filename to read from: ")
    
    # Read the content from the file
    content = read_file(input_filename)
    
    if content is not None:
        # Modify the content
        modified_content = modify_content(content)
        
        # Ask the user for the output filename
        output_filename = input("Enter the filename to write to: ")
        
        # Write the modified content to the new file
        write_file(output_filename, modified_content)

if __name__ == "__main__":
    main()
