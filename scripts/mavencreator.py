#!/usr/bin/env python3

import os
import shutil

def create_folder_structure(directory):
    if not directory.startswith('ignore-'):
        # make sure there is a java file
        java_files = [f for f in os.listdir(directory) if f.endswith('.java')]
        if java_files:
            directory_name = os.path.basename(directory)

            # create pom.xml file in the current directory
            pom_xml_path = os.path.join(directory, 'pom.xml')
            with open('pom_template.xml','r') as pom_temp:
                with open(pom_xml_path, 'a') as pom_file:
                    shutil.copyfileobj(pom_temp, pom_file)

            # Create src directory
            src_path = os.path.join(directory, 'src')
            os.makedirs(src_path, exist_ok=True)

            # Create main/java directory
            java_path = os.path.join(src_path, 'main', 'java')
            os.makedirs(java_path, exist_ok=True)

            # Copy Java files to main/java directory
            for java_file in java_files:
                src_file = os.path.join(directory, java_file)
                shutil.copy(src_file, os.path.join(java_path, java_file))

if __name__ == "__main__":
    # Specify the root directory containing Java files
    root_directory = 'Java_maven'

    # Iterate through directories and create folder structure
    for directory in os.listdir(root_directory):
        full_path = os.path.join(root_directory, directory)
        if os.path.isdir(full_path):
            create_folder_structure(full_path)

print("Folder structure creation completed.")
