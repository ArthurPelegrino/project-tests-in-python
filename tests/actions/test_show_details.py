from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date

# correct_result = (
#     "File name: projetos\n"
#     "File size in bytes: 4096\n"
#     "File type: directory\n"
#     "File extension: [no extension]\n"
#     "Last modified date: 2023-07-06"
# )


def test_show_details(capsys, correct_path_name, wrong_path_name, tmp_path):
    show_details(correct_path_name)

    captured = capsys.readouterr()
    assert captured.out.strip() == "File 'Trybe_logo.png' does not exist"

    show_details(wrong_path_name)
    captured = capsys.readouterr()
    assert captured.out.strip() == "File '????' does not exist"

    # show_details(my_computer_patch)
    # captured = capsys.readouterr()
    # assert captured.out.strip() == correct_result

    file = tmp_path / "pro-filer-preview"
    file.touch()

    context = {"base_path": str(file)}

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        "File name: pro-filer-preview\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        f"Last modified date: {date.today()}\n"
    )
    assert captured.out == expected_output
