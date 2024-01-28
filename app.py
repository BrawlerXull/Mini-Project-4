import os
import shutil
from helper import process_files
from watchgod import watch

current_dir_path = os.getcwd()
testing_path = os.path.join(current_dir_path, 'testing')


def move_files_on_change():
    split_files_result = process_files(testing_path)

    for key, files in split_files_result.items():
        new_created_folder_path = os.path.join(testing_path, key)
        os.makedirs(new_created_folder_path, exist_ok=True)

        for file in files:
            source_path = os.path.join(testing_path, file)
            destination_path = os.path.join(new_created_folder_path, file)
            shutil.move(source_path, destination_path)
            print(f"Moved {file} to {new_created_folder_path}")

    print(f"Current directory path: {current_dir_path}")
    print(f"Contents of {testing_path}: {os.listdir(testing_path)}")
    print(f"Split files result: {split_files_result}")

def handle_changes(changes):
    print("Directory changes detected:")
    move_files_on_change()

move_files_on_change()

for changes in watch(testing_path):
    handle_changes(changes)
