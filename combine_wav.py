import os
import re
import subprocess

# Get the current working directory
directory = os.getcwd()

# Get a list of all WAV files in the directory
wav_files = [f for f in os.listdir(directory) if f.endswith('.wav')]

# Function to extract the numeric part from the filename
def extract_number(filename):
    match = re.search(r'_(\d+)_', filename)
    return int(match.group(1)) if match else float('inf')

# Sort the files using the extracted number
sorted_files = sorted(wav_files, key=extract_number)

# Create a file list for ffmpeg
filelist_path = os.path.join(directory, 'filelist.txt')
with open(filelist_path, 'w') as filelist:
    for filename in sorted_files:
        filelist.write(f"file '{os.path.join(directory, filename)}'\n")

# Combine the WAV files using ffmpeg
output_file = os.path.join(directory, 'output.wav')
subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', filelist_path, '-c', 'copy', output_file])

print(f"Combined WAV files into {output_file}")

