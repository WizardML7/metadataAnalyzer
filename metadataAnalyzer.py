import os
import subprocess
import json

def run_program_for_file(file_path):
    # Replace 'exiftool' with the actual path to your exiftool executable
    exiftool_path = r'C:/Users/dloiacono/Downloads/exiftool-12.67/exiftool(-u -g1 -j).exe'
    
    try:
        # Run exiftool to get metadata as JSON
        result = subprocess.run([exiftool_path, file_path], capture_output=True, text=True, check=True)
        
        # Parse the JSON result
        json_result = json.loads(result.stdout)
        #print(json_result)
        # Extract the file name without extension
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        
        # Store the JSON object in the dictionary
        file_data[file_name] = json_result
        
        # Optionally, write the JSON object to a separate file
        output_file_path = os.path.join(output_directory, f'{file_name}.json')
        with open(output_file_path, 'w') as output_file:
            json.dump(json_result, output_file, indent=2)
        
    except subprocess.CalledProcessError as e:
        print(f"Error running exiftool for {file_path}: {e}")

def main():
    global file_data
    global output_directory
    
    # Replace 'C:\Path\To\Your\Directory' with the path to your directory
    directory_path = r'C:/Users/dloiacono/Downloads/C/Users/dloiacono/Pictures'
    
    # Replace 'C:\Path\To\Output\Directory' with the path to your output directory
    output_directory = r'C:/Users/dloiacono/Desktop/metadataAnalysis'
    
    # Create a dictionary to hold file data
    file_data = {}
    
    try:
        # List all files in the directory
        files = os.listdir(directory_path)
        
        # Iterate over each file and run the program
        for file in files:
            print(file)
            file_path = os.path.join(directory_path, file)
            
            # Check if the item is a file (not a subdirectory)
            if os.path.isfile(file_path):
                run_program_for_file(file_path)
                
    except FileNotFoundError:
        print(f"Directory not found: {directory_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
