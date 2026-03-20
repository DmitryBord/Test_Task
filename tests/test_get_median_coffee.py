from report_median_coffee import get_median_coffee


def test_get_median_coffee_basic(data):
    f1, f2 = data
    assert get_median_coffee([str(f1), str(f2)]) == [
        ("Алексей", 20),
        ("Дарья", 20),
        ("Артем", 5)
    ]
