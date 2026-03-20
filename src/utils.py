from typing import TypedDict, Callable, Any


class TypeReport(TypedDict):
    func: Callable[[list[str]], Any]
    headers: list[str]


class Reports:
    reports: dict[str, TypeReport] = {}

    @classmethod
    def registry(cls, name: str, headers: list[str]):
        def wrapper(func: Callable[[list[str]], list[tuple[str, float]]]):
            cls.reports[name] = {
                "func": func,
                "headers": headers
            }
            return func
        return wrapper

    @classmethod
    def get_report(cls, name: str) -> TypeReport | None:
        report: TypeReport | None = cls.reports.get(name, None)
        return report
