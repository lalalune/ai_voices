import os
import sys
import re

def rename_files(directory):
    # Get all .wav files in the directory
    wav_files = [f for f in os.listdir(directory) if f.endswith('.wav')]
    
    # Sort the files
    wav_files.sort(key=lambda f: int(re.findall(r'\d+', f)[-1]) if re.findall(r'\d+', f) else 0)
    
    # Rename files
    for i, filename in enumerate(wav_files, start=1):
        new_filename = f'{directory}_{i:03d}.wav'
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        sys.exit(1)
    
    rename_files(directory)
    print("File renaming completed.")

rename_files(sys.argv[1])