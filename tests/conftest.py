import pytest


@pytest.fixture
def data(tmp_path):
    f1 = tmp_path / "f1.csv"
    f2 = tmp_path / "f2.csv"

    f1.write_text(
        "student,coffee_spent\n"
        "Алексей,10\n"
        "Алексей,20\n"
        "Дарья,20\n"
        "Дарья,30\n"
    )

    f2.write_text(
        "student,coffee_spent\n"
        "Алексей,30\n"
        "Дарья,10\n"
        "Артем,5\n"
    )

    return f1, f2


