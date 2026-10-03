import os
from pathlib import Path 
import pytest


from src import file_operation

def test_can_find_current_work_directory():
    current_path = str(Path().absolute())
    assumed_path = file_operation.get_current_path()

    assert(current_path == assumed_path)



def test_can_read_sample_file():
    sample_path = "/tests/mock/sample_read.md"
    abs_path = file_operation.get_current_path() + sample_path

    res = file_operation.read_file(abs_path)
    assert(res == "hey\nwhats\nup\n")

def test_can_write_to_sample_file():
    sample_path = "/tests/mock/sample_write.md"
    abs_path = file_operation.get_current_path() + sample_path

    msg = "hi\ngabe\nthis\nside"

    file_operation.write_to_file(abs_path, msg)
    res = file_operation.read_file(abs_path)
    assert(res == msg) 

def test_can_list_full_directory():
    current_path = file_operation.get_current_path()
    res = file_operation.get_files_tree(current_path)
    names = [path.name for path in res]

    print(names)

    assert("tests" in names)
    assert("file_operation.py" in names)
    assert("src" in names)


def test_can_delete_file():
    sample_path = "/tests/mock/sample_write.md"
    abs_path = file_operation.get_current_path() + sample_path

    file_operation.delete_file(abs_path)
    assert(not Path(abs_path).exists())

def test_cannot_delete_invalid_file_and_throw_error():
    sample_path = "/tests/mock/sample_write.md"
    abs_path = file_operation.get_current_path() + sample_path


    with pytest.raises(FileNotFoundError) as e:
        file_operation.delete_file(abs_path)

    assert str(e.value) == f"This is not a valid file directory"
 