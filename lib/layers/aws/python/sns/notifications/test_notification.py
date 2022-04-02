from abc import abstractmethod
from sns.notifications.notification import Notification
from typing import Any, Dict


class TestNotification(Notification):
    def __init__(self, title: str, body: str, ttl: int):
        super().__init__(ttl)
        self._title = title
        self._body = body

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title) -> None:
        self._title = title

    @property
    def body(self) -> str:
        return self._body

    @body.setter
    def body(self, body) -> None:
        self._body = body

    @property
    @abstractmethod
    def apns(self) -> Dict[str, Any]:
        return {
            'aps': {
                'alert': {
                    'title': self._title,
                    'body': self._body
                }
            }
        }

    @property
    @abstractmethod
    def gcm(self) -> Dict[str, Any]:
        return {
            'data': {
                'payload': {
                    'title': self._title,
                    'body': self._body
                }
            }
        }
