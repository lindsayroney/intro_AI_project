#!/usr/bin/env python3

import os
import re
import shutil

# public class name
class_pattern = re.compile(r'public\s+class\s+(\w+)')

def extract_class(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        match = class_pattern.search(contents)
        if match:
            return match.group(1)
    return None

def main():
    for filename in os.listdir('./Javatest'):
        if filename.endswith('.java'):
            java_file_path = os.path.join(root_directory, filename)
            class_name = extract_class(java_file_path)
            
            if class_name:
                # create unique id for new directory
                unique_id = os.path.splitext(filename)[0]
                
                # make new directory with og file name
                new_directory = os.path.join(root_directory, unique_id)
                os.makedirs(new_directory, exist_ok=True)
                
                # rename file to class name
                new_file_path = os.path.join(new_directory, class_name + '.java')
                shutil.move(java_file_path, new_file_path)
                print(f'Renamed {filename} to {class_name}.java in folder {unique_id}')
            else:
                print(f'No public class function in {filename}')

if __name__ == "__main__":
    main()
