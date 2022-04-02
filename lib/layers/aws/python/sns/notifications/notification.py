from abc import ABC, abstractmethod
from typing import Any, Dict


class Notification(ABC):
    def __init__(self, ttl: int):
        self._ttl = ttl

    @property
    def ttl(self) -> int:
        return self._ttl

    @ttl.setter
    def ttl(self, ttl: int) -> None:
        self._ttl = ttl

    @property
    @abstractmethod
    def apns(self) -> Dict[str, Any]:
        ...

    @property
    def apns_sandbox(self) -> Dict[str, Any]:
        return self.apns

    @property
    @abstractmethod
    def gcm(self) -> Dict[str, Any]:
        ...
