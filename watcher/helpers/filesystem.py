import os


def create_directories_if_non_existent(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
