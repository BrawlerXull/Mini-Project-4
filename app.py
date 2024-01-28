import os
import shutil
from helper import process_files

current_dir_path = os.getcwd()
testing_path = os.path.join(current_dir_path, 'testing')

split_files_result = process_files(testing_path)

for key, files in split_files_result.items():
    new_created_folder_path = os.path.join(testing_path, key)
    os.makedirs(new_created_folder_path, exist_ok=True)
    
    for file in files:
        source_path = os.path.join(testing_path, file)
        destination_path = new_created_folder_path
        shutil.move(source_path, destination_path)

print(current_dir_path)
print(os.listdir(testing_path))
print(split_files_result)
