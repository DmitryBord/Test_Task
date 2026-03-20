import pytest
from report_median_coffee import read_data, sort_data_desc


def test_read_data_basic(data):
    assert read_data([str(data[0])]) == {
        "Алексей": [10, 20],
        "Дарья": [20, 30]
    }


def test_read_data_multiple_files(data):
    f1, f2 = data
    assert read_data([str(f1), str(f2)]) == {
        "Алексей": [10, 20, 30],
        "Дарья": [20, 30, 10],
        "Артем": [5]
    }


def test_read_data_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_data(["no_such_file.csv"])


def test_sort_data_desc():
    data = [
        ("Алексей", 20),
        ("Дарья", 30),
        ("Артем", 50)
    ]

    assert sort_data_desc(data) == [
        ("Артем", 50),
        ("Дарья", 30),
        ("Алексей", 20),
    ]
