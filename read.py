def modify_content(content):
    # Example modification: Convert all text to uppercase
    return content.upper()

def main():
    # Ask user for input filename
    input_filename = input("Enter the name of the file to read: ")

    try:
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content
        modified_content = modify_content(content)

        # Create output filename
        output_filename = f"modified_{input_filename}"

        # Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
