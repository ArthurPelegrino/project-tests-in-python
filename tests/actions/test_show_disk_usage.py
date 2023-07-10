from pro_filer.actions.main_actions import show_disk_usage  # NOQA


correct_result = (
    "'/tmp/pytest-of-arthur/pytes...test_show_disk_usage0/teste.py':"
    "        5 (100%)\n"
    "'/tmp/pytest-of-arthur/pytes...est_show_disk_usage0/teste2.py':"
    "        0 (0%)\n"
    "Total size: 5"
)


def test_show_disk_usage(capsys, tmp_path):
    # show_disk_usage(empty_file_list)

    # captured = capsys.readouterr()
    # assert captured.out.strip() == "Total size: 0"

    # show_disk_usage(my_pc_path_file_list)
    # captured = capsys.readouterr()
    # assert captured.out.strip() == correct_result

    mocked_file = tmp_path / "teste.py"
    mocked_file.touch()
    mocked_file.write_text("teste")
    path = str(mocked_file)
    mocked_file2 = tmp_path / "teste2.py"
    mocked_file2.touch()
    path2 = str(mocked_file2)
    context_mock = {"all_files": [path, path2]}

    show_disk_usage(context_mock)
    captured = capsys.readouterr()
    assert captured.out.strip() == correct_result
