def modify_content(content):
    # Example modification: Convert all text to uppercase
    return content.upper()

def main():
  
    input_filename = input("Enter the name of the file to read: ")

    try:
        
        with open(input_filename, 'r') as infile:
            content = infile.read()
      
        modified_content = modify_content(content)

        output_filename = f"modified_{input_filename}"

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"File successfully modified and saved as '{output_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
