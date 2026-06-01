from __future__ import annotations

from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """Общий абстрактный класс для сущностей с именем."""

    @property
    @abstractmethod
    def name(self) -> str:
        pass
