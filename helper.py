import os
import shutil
from watchgod import watch

def process_files(testing_path):
    split_files_dict = {}  

    for file in os.listdir(testing_path):
        file_path = os.path.join(testing_path, file)
        if os.path.isfile(file_path):
            split_file = file.split('.')
            key = split_file[1]
            value = split_file[0]
            if key not in split_files_dict:
                split_files_dict[key] = [file]
            else:
                split_files_dict[key].append(file)
        else:
            print("Not a file:", file)

    return split_files_dict


def move_files_on_change(testing_path):
    split_files_result = process_files(testing_path)

    for key, files in split_files_result.items():
        new_created_folder_path = os.path.join(testing_path, key)
        os.makedirs(new_created_folder_path, exist_ok=True)

        for file in files:
            source_path = os.path.join(testing_path, file)
            destination_path = os.path.join(new_created_folder_path, file)
            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {new_created_folder_path}")

    print(f"Contents of {testing_path}: {os.listdir(testing_path)}")
    print(f"Split files result: {split_files_result}")


