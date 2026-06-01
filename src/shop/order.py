from __future__ import annotations

from shop.base_entity import BaseEntity
from shop.product import Product


class Order(BaseEntity):
    """Заказ с одним товаром, количеством и итоговой стоимостью."""

    def __init__(
        self,
        product: Product,
        quantity: int,
        total_cost: float,
    ) -> None:
        self._name = f"Заказ: {product.name}"
        self.product = product
        self.quantity = quantity
        self.total_cost = total_cost

    @property
    def name(self) -> str:
        return self._name
