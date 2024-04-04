import os

# Specify the folder containing the files
folder_path = 'C:\\code\\Essa\\ESSA-REACT\\src\\assets\\courseware.prep'

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.md'):  # Assuming all files have the .md extension
        file_path = os.path.join(folder_path, filename)
        
        # Read the content of the file
        with open(file_path, 'r') as file:
            content = file.read()

        # Find the start and end indices of the header
        start_index = content.find('_Notes')
        end_index = content.find('_', start_index + 1)

        # Remove the header from the content
        if start_index != -1 and end_index != -1:
            content = content[:start_index] + content[end_index + 3:]

        # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(content)
