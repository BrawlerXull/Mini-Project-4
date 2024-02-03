import os
from helper import move_files_on_change , get_all_files_access_time_sorted_processed
from watchgod import watch

current_dir_path = os.getcwd()
# This below line is the path that will be taken as an input by the user
testing_path = os.path.join(current_dir_path , "testing")

move_files_on_change(testing_path)

print(get_all_files_access_time_sorted_processed(testing_path))

for changes in watch(testing_path):
    move_files_on_change(testing_path)
