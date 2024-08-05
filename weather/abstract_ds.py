from abc import ABC, abstractmethod

class Service(ABC):
    """Abstract base class for services providing data."""
    @abstractmethod
    def get_data(self) -> dict:
        pass