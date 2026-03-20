import statistics
import csv


def read_data(files: list[str]) -> dict[str, list[float]]:
    student_spending: dict[str, list[float]] = {}
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                amount = float(row["coffee_spent"])
                student_spending.setdefault(row["student"], []).append(amount)
    return student_spending


def calculate_median(amounts: list[float]) -> float | list:
    if amounts:
        amounts = statistics.median(amounts)
    return amounts


def sort_data_desc(data: list[tuple[str, float]]) -> list[tuple[str, float]]:
    return sorted(data, key=lambda x: x[1], reverse=True)


def get_median_coffee(files: list[str]) -> list[tuple[str, float]]:
    data: dict[str, list[float]] = read_data(files)
    result: list[tuple[str, float]] = [
        (key, calculate_median(value))
        for key, value in data.items()
    ]

    return sort_data_desc(result)
