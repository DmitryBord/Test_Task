import pytest
from subprocess import run


@pytest.mark.parametrize(
    "name",
    [
        ("Алексей   |              20"),
        ("Дарья     |              20"),
        ("Артем     |               5")
    ]
)
def test_cli_basic(data, name):
    f1, f2 = data
    result = run(
        ["python", "main.py", "--files", str(f1), str(f2), "--report", "median-coffee"],
        cwd="src",
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert name in result.stdout


def test_cli_unknown_report(data):
    file = data[0]

    result = run(
        ["python",  "main.py", "--files", str(file), "--report", "unknown"],
        cwd="src",
        capture_output=True, text=True
    )

    assert result.returncode != 0
    assert "Unknown report" in result.stderr
