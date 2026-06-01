from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех товаров."""

    @classmethod
    @abstractmethod
    def new_product(
        cls,
        product_data: dict,
        existing_products: list[BaseProduct] | None = None,
    ) -> BaseProduct:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @abstractmethod
    def check_change_price(self, new_price: float) -> float | None:
        pass

    @abstractmethod
    def __add__(self, other: object) -> float:
        pass
