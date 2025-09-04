from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    @abstractmethod
    def initialize(self) -> Any:
        """Initialize the tool with necessary configuration."""
        pass

    @abstractmethod
    def get_tool(self) -> Any:
        """Return the initialized tool object."""
        pass
