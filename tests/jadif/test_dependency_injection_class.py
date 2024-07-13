from abc import ABC, abstractmethod

from jadif.jadif import dependency


class BaseClass(ABC):
    @abstractmethod
    def get_processed_value(self, value: str) -> str:
        pass


class ImplementationA(BaseClass):
    def get_processed_value(self, value: str) -> str:
        return f"*{value}*"


class ImplementationB(BaseClass):
    def get_processed_value(self, value: str) -> str:
        return f"<<{value}>>"


def make_type_a_dependencies() -> None:
    dependency.add_config(BaseClass, ImplementationA)


def make_type_b_dependencies() -> None:
    dependency.add_config(BaseClass, ImplementationB)


def process_strings(input_items: list[str]) -> list[str]:
    processor_class = dependency.resolve(BaseClass)
    processor: BaseClass = processor_class()
    return [processor.get_processed_value(item) for item in input_items]


def test_dependency_injection_case_a() -> None:
    make_type_a_dependencies()

    assert process_strings(["aaa", "bbb"]) == ["*aaa*", "*bbb*"]


def test_dependency_injection_case_b() -> None:
    make_type_b_dependencies()

    assert process_strings(["aaa", "bbb"]) == ["<<aaa>>", "<<bbb>>"]
