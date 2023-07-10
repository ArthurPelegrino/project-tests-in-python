import pytest


@pytest.fixture
def correct_dict():
    context = {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
        ],
        "all_dirs": ["src", "src/utils"],
    }
    return context


@pytest.fixture
def more_than_five_dict():
    return {
        "all_files": [
            "src/__init__.py",
            "src/app.py",
            "src/utils/__init__.py",
            "src/utils/__str__.py",
            "src/images/teste.img" "src/utils/__teste__.py",
        ],
        "all_dirs": [
            "src",
            "src/utils",
            "src/css",
            "src/model",
            "src/controller",
            "src/servise",
        ],
    }


@pytest.fixture
def empty_dict():
    return {"all_files": [], "all_dirs": []}


@pytest.fixture
def correct_path_name():
    context = {"base_path": "/home/trybe/Downloads/Trybe_logo.png"}
    return context


@pytest.fixture
def wrong_path_name():
    context = {"base_path": "/home/trybe/????"}
    return context


@pytest.fixture
def my_computer_patch():
    context = {"base_path": "/home/arthur/Trybe/python/projetos"}
    return context
