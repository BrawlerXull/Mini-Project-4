import os
import shutil
from watchgod import watch
from datetime import datetime , timedelta

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

def delete_files_older_than(testing_path, days):
    current_time = datetime.now()
    for file in os.listdir(testing_path):
        file_path = os.path.join(testing_path, file)
        if os.path.isfile(file_path):
            file_time = datetime.fromtimestamp(os.path.getctime(file_path))
            if current_time - file_time > timedelta(days=days):
                os.remove(file_path)
                print(f"Deleted {file} (older than {days} days)")


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


def get_all_files_access_time_sorted(testing_path):
    all_files_access_time = []

    for folder in os.listdir(testing_path):
        folder_path = os.path.join(testing_path, folder)

        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file)

                if os.path.isfile(file_path):
                    access_time = datetime.fromtimestamp(os.path.getatime(file_path))
                    all_files_access_time.append((file, access_time))

    all_files_access_time_sorted = sorted(all_files_access_time, key=lambda x: x[1])

    return all_files_access_time_sorted

def get_all_files_access_time_sorted_processed(testing_path):
    file_names = []
    access_time = []
    files = get_all_files_access_time_sorted(testing_path)
    for file in files :
        file_names.append(file[0])
        access_time.append(file[1])
    return file_names , access_time