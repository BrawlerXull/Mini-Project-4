import os

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
