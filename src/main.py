import sys
from tabulate import tabulate
import argparse
from src.utils import TypeReport, Reports
from src.report_median_coffee import get_median_coffee

# Метод для регистрации новых репортов
# Reports.registry_report("median-coffee", get_median_coffee,
#                         ["Student", "Median_coffee"])


def get_args_from_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", required=True, nargs="+", help="path to file.csv")
    parser.add_argument("--report", required=True, help="name of report's file")
    args = parser.parse_args()
    return args


def main():
    args = get_args_from_cli()
    report: TypeReport | None = Reports.get_report(args.report)

    if not report:
        print(f"Unknown report: {args.report}", file=sys.stderr)
        sys.exit(1)

    try:
        result: list[tuple[str, float]] = report["func"](args.files)
    except FileNotFoundError as e:
        print(f"File not found: {e}", file=sys.stderr)
        sys.exit(1)
    except (ValueError, KeyError) as e:
        print(f"Data error: {e}", file=sys.stderr)
        sys.exit(1)

    print(tabulate(result, headers=report["headers"], tablefmt="grid"))


if __name__ == "__main__":
    main()
