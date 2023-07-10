from pro_filer.actions.main_actions import show_details  # NOQA

correct_result = (
    "File name: projetos\n"
    "File size in bytes: 4096\n"
    "File type: directory\n"
    "File extension: [no extension]\n"
    "Last modified date: 2023-07-06"
)


def test_show_details(
    capsys, correct_path_name, wrong_path_name, my_computer_patch
):
    show_details(correct_path_name)

    captured = capsys.readouterr()
    assert captured.out.strip() == "File 'Trybe_logo.png' does not exist"

    show_details(wrong_path_name)
    captured = capsys.readouterr()
    assert captured.out.strip() == "File '????' does not exist"

    show_details(my_computer_patch)
    captured = capsys.readouterr()
    assert captured.out.strip() == correct_result
