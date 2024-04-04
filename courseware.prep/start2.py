import os

# Specify the folder containing the files
folder_path = 'C:\\code\\Essa\\ESSA-REACT\\src\\assets\\courseware.prep'

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.md'):  # Assuming all files have the .md extension
        file_path = os.path.join(folder_path, filename)
        
        # Read the content of the file
        with open(file_path, 'r+') as file:
            current_content = file.read()
            input_file_name = os.path.basename(file_path)
            formatted_name = input_file_name.replace('-', ' - ').replace('.md', '').replace('Module', '# Module')
            
            # Write the formatted filename and content back to the file
            file.seek(0)
            file.write(formatted_name + '\n\n' + current_content)
