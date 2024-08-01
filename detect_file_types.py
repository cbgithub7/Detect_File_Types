import os
import magic

# ANSI escape codes for color
RED = '\033[91m'  # Red text
RESET = '\033[0m'  # Reset text color to default

def get_file_type(file_path):
    """
    Determines the MIME type of a file based on its content.
    
    Args:
        file_path (str): The path to the file whose type is to be determined.
    
    Returns:
        str: The MIME type of the file or an error message if determination fails.
    """
    try:
        # Use python-magic to determine the file type
        mime_type = magic.from_file(file_path, mime=True)
        return mime_type
    except Exception as e:
        # Return error message if the file type cannot be determined
        return f'Error: {e}'

def main():
    """
    Main function to process files in the user-specified folder, determine their types,
    and print the results with skipped files highlighted in red.
    """
    # Prompt user for the folder path
    cache_folder_path = input("Please enter the path to the folder to check: ").strip()

    # Validate the provided folder path
    if not os.path.isdir(cache_folder_path):
        print(f"{RED}Error: The specified path is not a valid directory.{RESET}")
        return

    # Get a list of all files in the specified folder
    files = os.listdir(cache_folder_path)
    total_files = len(files)
    print(f"Found {total_files} files in the folder.")

    # Initialize counters for processed and skipped files
    processed_files = 0
    skipped_files = 0

    # Iterate over each file in the folder
    for index, file_name in enumerate(files, start=1):
        # Construct the full file path
        file_path = os.path.join(cache_folder_path, file_name)
        
        # Check if it is a file (not a directory)
        if os.path.isfile(file_path):
            # Determine the file type
            file_type = get_file_type(file_path)
            if file_type.startswith('Error:'):
                # Increment skipped files counter and print in red
                skipped_files += 1
                print(f"File {index}/{total_files}: {RED}{file_name} - {file_type}{RESET}")
            else:
                # Increment processed files counter and print
                processed_files += 1
                print(f"File {index}/{total_files}: {file_name} - {file_type}")
        else:
            # Increment skipped files counter for non-files
            skipped_files += 1
            print(f"File {index}/{total_files}: {RED}Skipped (not a file){RESET}")

    # Print the summary of processed and skipped files
    print(f"File type detection complete. Processed files: {processed_files}, Skipped files: {skipped_files}")

if __name__ == "__main__":
    main()
