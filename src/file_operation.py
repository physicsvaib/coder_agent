import os
import pathlib 

def get_current_path():
    return os.getcwd()

def read_file(path):
    with open(path, "r") as f:
       data = f.read()
    return data 

def write_to_file(path, msg):
    with open(path, "w") as f:
        f.write(msg)
    
def get_files_tree(path):
    paths = pathlib.Path(path).rglob("*")
    return list(paths)

def delete_file(path):
    path = pathlib.Path(path)

    if not path.exists():
        raise FileNotFoundError("This is not a valid file directory")

    if path.is_file():
        path.unlink()
