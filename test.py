import os

path = "C:/Users/saira/OneDrive/Desktop/test mini project/test.py"
directory, filename = os.path.split(path)
filename_new, extension = os.path.splitext(filename)
extension_new = extension[1:]
print("Directory:", directory)
print("Filename:", filename)
print("Only Filename:", filename_new)
print("Extension:", extension_new)
final_path = os.path.join(directory,extension_new)
print(final_path)

