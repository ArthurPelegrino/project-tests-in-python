from pro_filer.actions.main_actions import show_preview  # NOQA

# import pytest
import sys

context = {"all_files": [], "all_dirs": []}
correct_dict_return = (
    "Found 3 files and 2 directories\nFirst 5 files: ['src/__init__.py',"
    + " 'src/app.py', 'src/utils/__init__.py']\nFirst 5 directories:"
    " ['src', 'src/utils']"
)

more_than_five_return = (
    "Found 5 files and 6 directories\nFirst 5 files: ['src/__init__.py',"
    + " 'src/app.py', 'src/utils/__init__.py', 'src/utils/__str__.py'"
    ", 'src/images/teste.imgsrc/utils/__teste__.py']\nFirst 5 directories:"
    " ['src', 'src/utils', 'src/css', 'src/model', 'src/controller']"
)


# @pytest.fixture
# def my_dict():
#     context = {
#         "all_files": [
#             "src/__init__.py",
#             "src/app.py",
#             "src/utils/__init__.py",
#         ],
#         "all_dirs": ["src", "src/utils"],
#     }
#     return context


def test_show_preview(capsys, empty_dict, correct_dict, more_than_five_dict):
    show_preview(empty_dict)
    captured = capsys.readouterr()
    # print("COM STRIP", captured.out)
    # print("SEM STRIP", captured.out.strip())
    sys.stdout.read()
    assert captured.out.strip() == "Found 0 files and 0 directories"

    show_preview(correct_dict)
    captured = capsys.readouterr()
    assert captured.out.strip() == correct_dict_return

    show_preview(more_than_five_dict)
    captured = capsys.readouterr()
    assert captured.out.strip() == more_than_five_return
