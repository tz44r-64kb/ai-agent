import os

def get_files_info(working_directory, directory=None):
    is_in_working_directory = os.path.join(working_directory, directory) == os.path.abspath(directory)
    print(f"is_in_working_directory: {is_in_working_directory}")
    if is_in_working_directory == False:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
