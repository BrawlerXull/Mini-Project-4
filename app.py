import os
from helper import move_files_on_change
from watchgod import watch

current_dir_path = os.getcwd()
# This below line is the path that will be taken as an input by the user
testing_path = os.path.join(current_dir_path , "testing")

move_files_on_change(testing_path)

for changes in watch(testing_path):
    move_files_on_change(testing_path)
