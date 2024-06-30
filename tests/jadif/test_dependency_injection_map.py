from abc import ABC, abstractmethod

from jadif.jadif import DependencyInjectionMap


def test_dependency_injection_map() -> None:

    class Abstract(ABC):
        @abstractmethod
        def perform(self) -> None:
            pass

    class ConcreteAlfa(Abstract):
        def perform(self) -> None:
            pass

    class ConcreteBeta(Abstract):
        def perform(self) -> None:
            pass

    di = DependencyInjectionMap()

    di.add_config(Abstract, ConcreteAlfa())
    assert isinstance(di.resolve(Abstract), ConcreteAlfa)

    di.add_config(Abstract, ConcreteBeta())
    assert isinstance(di.resolve(Abstract), ConcreteBeta)
