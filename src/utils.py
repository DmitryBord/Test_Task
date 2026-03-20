from typing import TypedDict, Callable
from copy import copy


class TypeReport(TypedDict):
    func: Callable[[list[str]], list[tuple[str, float]]]
    headers: list[str]


class Reports:
    reports: dict[str, TypeReport] = {}

    @classmethod
    def registry_report(cls, name: str, func: Callable[[list[str]], list[tuple[str, float]]], headers: list[str]):
        cls.reports[name] = {
            "func": func,
            "headers": headers
        }

    @classmethod
    def get_report(cls, report: str) -> TypeReport | None:
        report: TypeReport = cls.reports.get(report, None)
        return copy(report)
