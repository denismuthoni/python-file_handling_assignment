# file_handling_assignment.py

def main():
    filename = "my_file.txt"
    
    # File Creation and Writing
    try:
        with open(filename, 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("Here is the second line, which includes a number: 123.\n")
            file.write("And this is the third line with some more text.\n")
        print(f"Successfully created and wrote to {filename}.")
    
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while creating or writing to the file: {e}")
    
    finally:
        print("File creation and writing operation completed.")
    
    # File Reading and Display
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("\nContents of the file after writing:")
        print(content)
    
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while reading the file: {e}")
    
    finally:
        print("File reading operation completed.")
    
    # File Appending
    try:
        with open(filename, 'a') as file:
            file.write("This is an additional line of text.\n")
            file.write("Here is another appended line with numbers: 456.\n")
            file.write("And a final line of appended text.\n")
        print(f"\nSuccessfully appended to {filename}.")
    
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while appending to the file: {e}")
    
    finally:
        print("File appending operation completed.")
    
    # Reading and Displaying the File After Appending
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print("\nContents of the file after appending:")
        print(content)
    
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error while reading the file after appending: {e}")
    
    finally:
        print("File reading after appending operation completed.")

if __name__ == "__main__":
    main()