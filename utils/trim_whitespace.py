import os
import sys
import argparse

def trim_whitespace_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        trimmed_content = content.strip()
        
        if content != trimmed_content:
            with open(file_path, 'w') as file:
                file.write(trimmed_content)
            print(f"Trimmed whitespace in {file_path}")
        else:
            print(f"No changes needed for {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                trim_whitespace_in_file(file_path)

def main():
    parser = argparse.ArgumentParser(description="Trim whitespace from text files in a directory.")
    parser.add_argument("directory", help="The target directory containing text files to process")
    args = parser.parse_args()

    target_directory = args.directory

    if not os.path.isdir(target_directory):
        print(f"Error: {target_directory} is not a valid directory")
        sys.exit(1)

    print(f"Processing directory: {target_directory}")
    process_directory(target_directory)
    print("Processing complete.")

if __name__ == "__main__":
    main()